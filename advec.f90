PROGRAM advection

  USE output
  
  IMPLICIT NONE

  INTEGER, PARAMETER :: nx = 100
  INTEGER, PARAMETER :: mode = 0 ! 0: square wave, 1: sine wave
  INTEGER, PARAMETER :: recon = 4 ! 0: upwind, 1: central (Fromm), 2: right slopes, 3: left slopes (Beam-Warming), 4: minmod, 5: van Leer, 6: MC
  CHARACTER (LEN=4) ::  slopemethod = 'min3'
  REAL, PARAMETER :: vel = 1.0
  REAL, PARAMETER :: cfac = 0.8 !safety (CFL) factor for time step
  REAL, PARAMETER :: tlast = 1.0 !run until time == tlast
  REAL, PARAMETER :: dtout = 0.05 !time between writing outputs
  REAL, PARAMETER :: pi = 4.0 * ATAN (1.0)

  
  REAL :: u (0:nx+1), unew (0:nx+1) ! solution with one buffer zone ("ghost zone") at each end
  REAL :: u_if (0:nx)   ! solution at cell interfaces
  REAL :: slope (0:nx+1) ! slopes in each cell
  REAL :: sleft, sright ! left and right slopes
  REAL :: time, dt, dx, x (1:nx)
  REAL :: tout_next
  INTEGER :: i, istep
  
  
  !read(*,*) recon

  !define grid
  DO i = 1, nx
     x (i) = (REAL (i)-0.5) / REAL(nx)
  END DO
  dx = 1.0 / REAL (nx)
  
  dt = cfac * dx / vel

  !define initial conditions
  DO i = 1, nx
     IF (mode .EQ. 0) THEN
        IF (x(i) >0.25 .and. x(i)<=0.75) THEN
           u (i) = 1.0
        ELSE
           u (i) = 0.0
        END IF
     ELSE IF (mode .EQ. 1) THEN
        u (i) = SIN (2.0 * pi * x (i))
     ELSE
        STOP 'Incorrect mode'
     END IF
  END DO
     
  time = 0.0
  istep = 0

  !first output - note that we're passing only the array elements 1:nx!
  CALL output_to_file (x (1:nx), u (1:nx), nx, istep,recon,slopemethod)

  tout_next = dtout
  
  !loop over time
  DO WHILE (time <= 1.0)
     
     !set boundary conditions
     u (nx+1) = u (1) !periodic
     u (0) = u (nx)

! slope schemes
     DO i = 1, nx
     sleft=(u(i) - u(i-1))/dx
     sright=(u(i+1)-u(i))/dx
        IF (recon .EQ. 0) THEN
           !upwind -- flat reconstruction          
           slope(i) = 0.0
        ELSE IF (recon .EQ. 1) THEN
           !centred - Fromm's method											! Fromm's scheme
           slope(i) = (u(i+1) - u(i-1))/(2.0*dx)										 
        ELSE IF (recon .EQ. 2) THEN
           ! right-sided slopes													! Right sided/Lax-Wendroff scheme
           slope(i)=sright													
        ELSE IF (recon .EQ. 3) THEN
           ! left-sided slopes (Beam-Warming)								! Left sided/Beam-Warming scheme
           slope(i)=sleft 														
        ELSE IF (recon .EQ. 4) THEN
           !minmod															      ! minmod limiter
              if ((sleft>0) .and. (sright>0)) then
                    slope(i)=min(abs(sleft),abs(sright))   
              else if ((sleft<0) .and. (sright<0)) then
                    slope(i)=-min(abs(sleft),abs(sright)) 
              else
                    slope(i)=0      
                   !sleft  = ((u(i)-u(i-1))/dx
                   !sright = (u(i+1)-u(i))/dx
                   !slope(i) = ???
              end if     
        ELSE IF (recon .EQ. 5) THEN
              !van Leer limiter
              if (sleft*sright>0) then											! van Leer limiter
                    slope(i)=2.0*sleft*sright/(sleft+sright)
              else
                    slope=0  
              end if       
        ELSE IF (recon .EQ. 6) THEN
           !MC limiter															   ! MC limiter 
                 if ((sleft>0) .and. (sright>0)) then
                 	slope(i)=min(min(2.0*abs(sleft),2.0*abs(sright)),abs(sleft+sright)/2.0)
                 else if  ((sleft<0.0) .and. (sright<0.0)) then
                        slope(i)=-min(min(2.0*abs(sleft),2*abs(sright)),abs(sleft+sright)/2.0)
                 else
                 	slope(i)=0.0
                 end if	       
        ELSE
                 STOP 'Reconstruction method undefined.'
        END IF
     END DO
     
     !set boundary conditions for slopes as well
     slope (nx+1) = slope (1) !periodic
     slope (0) = slope (nx)
     
     

     ! calculate interface values, advanced by half a time step
     DO i = 0, nx													
        u_if (i) = u(i) + slope(i)*((dx/2.0) - (vel*dt/2.0)) 				!u_if (i) = u(i) +slope(i)*((dx/2.0) - (vel*dt/2.0))   u_if (i) = u(i) + (slope(i)*(dx/2.0))
     END DO

     DO i = 1, nx
        unew (i) = u(i) + (dt/dx)*(vel*u_if(i-1) - vel*u_if(i))
     END DO

     u (:) = unew (:) ! new solution becomes old solution for next time step
     
     time = time + dt
     istep = istep + 1
     
     !PRINT *,'Time', istep, time

     !next output
     IF (time >= tout_next) THEN
        !PRINT *,'Output at t =',time," and istep =", istep
        CALL output_to_file (x (1:nx), u (1:nx), nx, istep,recon,slopemethod)
        tout_next = tout_next + dtout
     END  IF
        
  END DO


  
END PROGRAM advection
