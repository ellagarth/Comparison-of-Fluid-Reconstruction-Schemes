# Comparison-of-Fluid-Reconstruction-Schemes
Fortran and Python code for computing and visualising solutions to different first and second-order fluid mechanical reconstruction schemes.

This code allows users to select different reconstruction schemes (Godunov's, Fromm's, Beam-Warming, Lax-Wendroff) with and without the choice of slope limiters (Minmod, van Leer, MC) to model fluid mechanical problems on both step functions and smooth wavefronts using the 1D advection equation and the second-order time accuracte characterstic correction of upwind states reconstruction method. 

Users should select their modelling preferences at the top of the advec.f90 file, save it and run the Makefile, then plot the output .txt file contents using the plotting script (plotting.py), which is provided as an example but should be modified as required. 
