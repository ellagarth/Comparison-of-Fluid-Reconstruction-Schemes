# Comparison-of-Fluid-Reconstruction-Schemes
Fortran and Python code for computing and visualising solutions to different first and second-order fluid mechanical reconstruction schemes.

This code allows users to select different reconstruction schemes (Godunov's, Fromm's, Beam-Warming, Lax-Wendroff) with and without the choice of slope limiters (Minmod, van Leer, MC) to model fluid mechanical problems using the 1D advection equation and the second-order time accuracte characterstic correction of upwind states reconstruction method. 

Users should select their modelling preferences in the advec.f90 file, run the Makefile, and plot the output file using plotting.py 
