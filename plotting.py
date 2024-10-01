def plot_one(filename,filename2):
    
    import numpy as np
    import matplotlib.pyplot as plt
    
    data = np.loadtxt(filename)
    data2=np.loadtxt(filename2)
    
    x1=np.array([0,0.25])
    y1=np.array([0,0])
    x2=np.array([0.25,0.25])
    y2=np.array([0,1])
    x3=np.array([0.25,0.75])
    y3=np.array([1,1])
    x4=np.array([0.75,0.75])
    y4=np.array([1,0])
    x5=np.array([0.75,1])
    y5=np.array([0,0])
# load data, first column is x, second column is u
        
    qc1, = plt.plot(data[:,0],data[:,1], linewidth = 1.0, label='Courant factor = 0.5', c = 'red') #plot and assigning legend handles
    qc2, = plt.plot(data2[:,0],data2[:,1],linewidth = 1.0, label='Courant factor = 0.8', c = 'blue') # plot and assign legend handles
    plt.plot(x1,y1, linewidth=1.0, linestyle='--', c = 'black', label = 'IC') # Plot initial conditions for comparison
    plt.plot(x2,y2, linewidth=1.0, linestyle='--', c = 'black')
    plt.plot(x3,y3, linewidth=1.0, linestyle='--', c = 'black')
    plt.plot(x4,y4, linewidth=1.0, linestyle='--', c = 'black')
    plt.plot(x5,y5, linewidth=1.0, linestyle='--', c = 'black')
## Use the following line instead if you want to create a legend later on
#    qc1, = plt.plot(data[:,0],data[:,1],label='insert legend label here')
    plt.xlabel('x') # Don't forget to label the plot axes!
    plt.ylabel('u')
    plt.ylim([-0.2,1.4]) # leave room for legend
    plt.xlim([0,1])
#    plt.ylim([-1,1.1]) # leave room for legend
    plt.legend(handles=[qc1,qc2])

    plt.show()
    plt.savefig('myplot1.pdf')







def plot_two(filename,filename2):
    
    import numpy as np
    import matplotlib.pyplot as plt
    
    data = np.loadtxt(filename)
    data2=np.loadtxt(filename2)
# load data, first column is x, second column is u
        
    # create data for initial sine wave
    time=np.arange(-3*np.pi, 3*np.pi, 0.01)
    amplitude=np.sin(2*time*np.pi)       
    
    qc1, = plt.plot(data[:,0],data[:,1], linewidth = 1.0, label='Fromm', c = 'red') #plot and assigning legend handles
    qc2, = plt.plot(data2[:,0],data2[:,1],linewidth = 1.0, label='MC', c = 'blue') # plot and assign legend handles
    plt.plot(time,amplitude, linewidth = 1.0, linestyle='--', c = 'black') # plot initial sine wave
## Use the following line instead if you want to create a legend later on
#    qc1, = plt.plot(data[:,0],data[:,1],label='insert legend label here')
    plt.xlabel('x') # Don't forget to label the plot axes!
    plt.ylabel('u')

    plt.ylim([-1.1,-0.8]) # leave room for legend
    plt.xlim([0.7,0.8])
    plt.legend(handles=[qc1,qc2])

    plt.show()
    plt.savefig('myplot2.pdf')


    


def plot_four(filename,filename2,filename3,filename4):
    
    import numpy as np
    import matplotlib.pyplot as plt
    
    x1=np.array([0,0.25])
    y1=np.array([0,0])
    x2=np.array([0.25,0.25])
    y2=np.array([0,1])
    x3=np.array([0.25,0.75])
    y3=np.array([1,1])
    x4=np.array([0.75,0.75])
    y4=np.array([1,0])
    x5=np.array([0.75,1])
    y5=np.array([0,0])
    
    data = np.loadtxt(filename)
    data2 = np.loadtxt(filename2)
    data3 = np.loadtxt(filename3)
    data4 = np.loadtxt(filename4)
# load data, first column is x, second column is u
        
## Use the following line instead if you want to create a legend later on
    qc1, = plt.plot(data[:,0],data[:,1], linewidth = 1.0, label='Godonov (flat slopes)', c = 'red') #plot and assigning legend handles
    qc2, = plt.plot(data2[:,0],data2[:,1],linewidth = 1.0, label='Fromms (centred slopes)', c = 'blue') # plot and assign legend handles
    qc3, = plt.plot(data3[:,0],data3[:,1],linewidth = 1.0, label='Beam-Warming (left-sided slopes)', c = 'orange')
    qc4, = plt.plot(data4[:,0],data4[:,1],linewidth = 1.0, label='Lax-Wendroff (right-sided slopes)', c = 'green')
    plt.plot(x1,y1, linewidth=1.0, linestyle='--', c = 'black', label = 'IC') # Plot initial conditions for comparison
    plt.plot(x2,y2, linewidth=1.0, linestyle='--', c = 'black')
    plt.plot(x3,y3, linewidth=1.0, linestyle='--', c = 'black')
    plt.plot(x4,y4, linewidth=1.0, linestyle='--', c = 'black')
    plt.plot(x5,y5, linewidth=1.0, linestyle='--', c = 'black')
    plt.xlabel('x') # Don't forget to label the plot axes!
    plt.ylabel('u')
    #plt.title('Modelling the Advection Equation using a Finite Volume Scheme')

    plt.ylim([-0.5,1.5]) # leave room for legend
    plt.xlim([0.0,1.0])
    plt.legend(handles=[qc1,qc2,qc3,qc4]) ## legend using assigned legend handles

    plt.show()
    plt.savefig('myplot4.pdf')    

import numpy as np
import matplotlib.pyplot as plt




def plot_five(filename,filename2,filename3,filename4):
    
    import numpy as np
    import matplotlib.pyplot as plt
    
    x1=np.array([0,0.25])
    y1=np.array([0,0])
    x2=np.array([0.25,0.25])
    y2=np.array([0,1])
    x3=np.array([0.25,0.75])
    y3=np.array([1,1])
    x4=np.array([0.75,0.75])
    y4=np.array([1,0])
    x5=np.array([0.75,1])
    y5=np.array([0,0])
    
    data = np.loadtxt(filename)
    data2 = np.loadtxt(filename2)
    data3 = np.loadtxt(filename3)
    data4 = np.loadtxt(filename4)
# load data, first column is x, second column is u
        
## Use the following line instead if you want to create a legend later on
    qc1, = plt.plot(data[:,0],data[:,1], linewidth = 1.0, label='Godunov', c = 'red') #plot and assigning legend handles
    qc2, = plt.plot(data2[:,0],data2[:,1],linewidth = 1.0, label='Minmod', c = 'darkviolet') # plot and assign legend handles
    qc3, = plt.plot(data3[:,0],data3[:,1],linewidth = 1.0, label='van Leer', c = 'cyan')
    qc4, = plt.plot(data4[:,0],data4[:,1],linewidth = 1.0, label='MC', c = 'lime')
    plt.plot(x1,y1, linewidth=1.0, linestyle='--', c = 'black', label = 'IC') # Plot initial conditions for comparison
    plt.plot(x2,y2, linewidth=1.0, linestyle='--', c = 'black')
    plt.plot(x3,y3, linewidth=1.0, linestyle='--', c = 'black')
    plt.plot(x4,y4, linewidth=1.0, linestyle='--', c = 'black')
    plt.plot(x5,y5, linewidth=1.0, linestyle='--', c = 'black')
    plt.xlabel('x') # Don't forget to label the plot axes!
    plt.ylabel('u')
#    plt.title('Modelling the Advection Equation using Slope Limiters')

    plt.ylim([-0.5,1.5]) # leave room for legend
    plt.xlim([0,1])
    plt.legend(handles=[qc1,qc2,qc3,qc4]) ## legend using assigned legend handles
    plt.show()
    plt.savefig('myplot5.pdf')    





def plot_six(filename,filename2,filename3,filename4):
    
    import numpy as np
    import matplotlib.pyplot as plt
    import math
 
    
    data = np.loadtxt(filename)
    data2 = np.loadtxt(filename2)
    data3 = np.loadtxt(filename3)
    data4 = np.loadtxt(filename4)
    #data5 = np.loadtxt(filename5)
    #data6 = np.loadtxt(filename6)
    #data7 = np.loadtxt(filename7)
# load data, first column is x, second column is u

# create data for initial sine wave
    time=np.arange(-3*np.pi, 3*np.pi, 0.01)
    amplitude=np.sin(2*time*np.pi)   

## Use the following line instead if you want to create a legend later on
    qc1, = plt.plot(data[:,0],data[:,1], linewidth = 1.0, label='Godonov (flat slopes)', c = 'red') #plot and assigning legend handles
    qc2, = plt.plot(data2[:,0],data2[:,1],linewidth = 1.0, label='Fromms (centred slopes)', c = 'blue') # plot and assign legend handles
    qc3, = plt.plot(data3[:,0],data3[:,1],linewidth = 1.0, label='Beam-Warming (left-sided slopes)', c='orange') #orange
    qc4, = plt.plot(data4[:,0],data4[:,1],linewidth = 1.0, label='Lax-Wendroff (right-sided slopes)', c='green') #green
    #qc1, = plt.plot(data5[:,0],data5[:,1], linewidth = 1.0, label='Godunov', c = 'red') #plot and assigning legend handles
    #qc5, = plt.plot(data5[:,0],data5[:,1],linewidth = 1.0, label='Minmod', c = 'darkviolet') # plot and assign legend handles
    #qc6, = plt.plot(data6[:,0],data6[:,1],linewidth = 1.0, label='van Leer', c = 'cyan')
    #qc7, = plt.plot(data7[:,0],data7[:,1],linewidth = 1.0, label='MC', c = 'lime')
    plt.plot(time,amplitude, linewidth = 1.0, linestyle='--', c = 'black') # plot initial sine wave
    plt.xlabel('x') # Don't forget to label the plot axes!
    plt.ylabel('u')
    #plt.title('Modelling the Advection Equation with Sine Wave Initial Conditions')

    plt.ylim([-0.5,1.5]) # leave room for legend
    plt.xlim([0,1])
    plt.legend(handles=[qc1,qc2,qc3,qc4]) ## legend using assigned legend handles

    plt.show()
    plt.savefig('myplot6.pdf')    












def animate1():
    
    import numpy as np
    import matplotlib.pyplot as plt
    import glob
    import os


    files = glob.glob('step_min2*.dat') # Search for all output files


    for file in files: # Loop over files
        data = np.loadtxt(file)
        plt.clf()
        plt.plot(data[:,0],data[:,1])
        plt.ylim([-1.5,1.5])
        plt.show(block=False)
        plt.pause(0.02) # Wait a little while before plotting the next time step so that the animation isn't too fast
        plt.savefig(file[:-3]+'png')

    # Convert the PNG files to an animated gif. You need to have ImageMagick installed to do this.
    #os.system('convert -delay 20  -loop 0   step_godu*.png   animation.gif')
    
def animate2():
    
    import numpy as np
    import matplotlib.pyplot as plt
    import glob
    import os


    files = glob.glob('step_From*.dat') # Search for all output files


    for file in files: # Loop over files
        data = np.loadtxt(file)
        plt.clf()
        plt.plot(data[:,0],data[:,1])
        plt.ylim([-1.5,1.7])
        plt.show(block=False)
        plt.pause(0.02) # Wait a little while before plotting the next time step so that the animation isn't too fast
        plt.savefig(file[:-3]+'png')

    # Convert the PNG files to an animated gif. You need to have ImageMagick installed to do this.
    os.system('convert -delay 20  -loop 0   step_From*.png   animation.gif')    
    

    
