from model_variable_temperature import Model_variable_temperature
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
from matplotlib import colors
from model import Model
from matplotlib import patches
np.set_printoptions(threshold=sys.maxsize)

class Animation_variable_temperature(object):
    def __init__(self, dimension, T_max, T_min, delta_T, iterations, H):
        """
        Consturctor of the Animation class
        """
        self.model = Model_variable_temperature(dimension, T_max, T_min, delta_T, H)
        self.model.set_up_random_state()
        self.iterations = iterations
        self.history = np.array([[]])
        self.history = [self.model.lattice.copy()]
        self.H = H
    def evolve(self):
        """
        Method used to evolve the model one step
        """
        for i in range(self.iterations):
            print(i)
            self.model.update()
            self.history += [self.model.lattice.copy()]


    def updatefig(self,i,ax2):
        """
        Method used to update the system for animation
        """
        self.model.update()
        self.im.set_array(self.model.lattice)
        self.temp.set_height(self.model.T)
        return [self.im,self.temp]
    def animate(self):
        """
        Method used to create an animation of the model
        """
        x = []
        y = []
        fig,(ax1,ax2) = plt.subplots(1,2)
        self.im = ax1.imshow(self.model.lattice)
        self.temp, = ax2.bar('Temperature',self.model.T)
        ani = animation.FuncAnimation(fig, self.updatefig,interval = 0.01, blit = True, fargs=[ax2])
        plt.show()

    def update(self,num,x,y, line):
        """
        Method used to update the model to get the energy for animation
        """
        x += [num]
        self.model.update()
        y += [Model.get_energy(self.model.lattice)]
        line.set_data(x, y)
        line.axes.axis([0, self.iterations, -4*self.model.N*self.model.N, 0])
        return line,

    def energy_animation_save(self):
        """
        Method used to create an animation of the energy of the system. It saves the animation
        """
        fig, ax = plt.subplots()
        x = []
        y = []
        line, = ax.plot([], [], color='k')
        ani = animation.FuncAnimation(fig, self.update, frames =self.iterations,fargs=[x,y,line],
                              interval=0.1, blit=True,repeat=False)
        ani.save('animation.gif', writer='imagemagick', fps=120)

    def energy_animation(self):
        """
        Method used to create an animation of the energy of the system. It saves the animation
        """
        fig, ax = plt.subplots()
        x = []
        y = []
        line, = ax.plot([], [], color='k')
        ani = animation.FuncAnimation(fig, self.update, frames =self.iterations,fargs=[x,y,line],
                              interval=0.1, blit=True,repeat=False)
        plt.show()

    def get_energy(self):
        """
        Method used to update the system a set number of iterations to get the final energy of the system.
        """
        for i in range(self.iterations):
            self.model.update()
            print(Model.get_energy(self.model.lattice,self.model.H))

    def get_lattice(self):
        """
        Method used to update the system a set number of iterations to get the final matrix
        """
        for i in range(self.iterations):
            self.model.update() 
        return self.model.lattice
    
    def update_magnet(self,num,x,y, line):
        """
        Method used to update the model to get the energy for animation
        """
        x += [num]
        self.model.update()
        y += [self.model.get_magnetisation()]
        line.set_data(x, y)
        line.axes.axis([0, self.iterations, -self.model.N**2, self.model.N**2])
        return line,
    
    def magnet_animation(self):
        """
        Method used to create an animation of the energy of the system. It saves the animation
        """
        fig, ax = plt.subplots()
        x = []
        y = []
        line, = ax.plot([], [], color='k')
        ani = animation.FuncAnimation(fig, self.update_magnet, frames =self.iterations,fargs=[x,y,line],
                              interval=0.1, blit=True,repeat=False)
        plt.show()
    
    def magnet_animation_change_temp(self):
        """
        Method used to create an animation of the energy of the system. It saves the animation
        """
        fig, ax = plt.subplots()
        x = []
        y = []
        line, = ax.plot([], [], color='k')
        ani = animation.FuncAnimation(fig, self.update_magnet_temp, frames =self.iterations,fargs=[x,y,line],
                              interval=0.1, blit=True,repeat=False)
        plt.show()
    
    def update_magnet_temp(self,num,x,y, line):
        """
        Method used to update the model to get the energy for animation
        """
        x += [num]
        self.model.update_with_no_constant_temperature(0.001)
        print(self.model.T)
        y += [self.model.get_magnetisation()]
        line.set_data(x, y)
        line.axes.axis([0, self.iterations, -self.model.N**2, self.model.N**2])
        return line,
    def update_all(self,num, x_energy, y_energy, x_magnet, y_magnet, line_energy,line_magnet):
        x_energy += [num]
        x_magnet += [num]
        self.model.update()
        y_energy += [Model.get_energy(self.model.lattice,self.H)]
        y_magnet += [self.model.get_magnetisation()]
        line_energy.set_data(x_energy, y_energy)
        line_magnet.set_data(x_magnet, y_magnet)
        self.im.set_array(self.model.lattice)
        self.temp.set_height(self.model.T)
        line_magnet.axes.axis([0, self.iterations, -self.model.N**2, self.model.N**2])
        line_energy.axes.axis([0, self.iterations, -4*self.model.N*self.model.N, 0])

        return [self.im, self.temp, line_energy,line_magnet]

        
    def all_animations(self):
        fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2)
        x_energy = []
        y_energy = []
        line_energy, = ax3.plot([],[],color ='k')
        x_magnet = []
        y_magnet = []
        line_magnet, = ax4.plot([],[],color='k')
        self.im = ax1.imshow(self.model.lattice)
        self.temp, = ax2.bar('Temperature',self.model.T)
        ani = animation.FuncAnimation(fig, self.update_all, frames =self.iterations,fargs=[x_energy,y_energy,x_magnet,y_magnet,line_energy,line_magnet],
                              interval=0.1, blit=True,repeat=False)
        plt.show()


        
