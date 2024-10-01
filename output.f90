MODULE output

  IMPLICIT NONE

  PUBLIC
  
CONTAINS

  SUBROUTINE output_to_file (x, u, nx, istep,recon,slopemethod)

    IMPLICIT NONE

    INTEGER, INTENT (IN) :: nx, istep
    REAL, INTENT (IN) :: x (1:nx), u (1:nx)
    INTEGER :: i, recon
    CHARACTER (LEN=4) :: num,recon_charac,slopemethod

    WRITE(num,'(I4.4)') istep
    WRITE(recon_charac, '(I4.4)') recon
    
    OPEN (30, FILE ='step_'//slopemethod//'_'//num//'.dat', FORM = 'FORMATTED')
   !(30, FILE = 'step_lax_w'//num//'.dat', FORM = 'FORMATTED')
    
    DO i = 1, nx
       WRITE (30,*) x (i), u (i)
    END DO

    RETURN

  END SUBROUTINE output_to_file
    
END MODULE output
