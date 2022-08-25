from model import Model
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
from matplotlib import colors
from matplotlib import patches
np.set_printoptions(threshold=sys.maxsize)

class Animation(object):
    def __init__(self, dimension, Temperature, iterations, H):
        """
        Consturctor of the Animation class
        """
        self.model = Model(dimension,Temperature, H)
        self.model.set_up_random_state()
        self.iterations = iterations
        self.history = np.array([[]])
        self.history = [self.model.lattice.copy()]
        
    def evolve(self):
        """
        Method used to evolve the model one step
        """
        for i in range(self.iterations):
            print(i)
            self.model.update()
            self.history += [self.model.lattice.copy()]

    def animate(self):
        """
        Method used to create an animation of the system, it will first make all the updates
        and then it will create the animation
        """
        self.evolve()
        fig = plt.figure()
        images = []
        count = 0
        for array2D in self.history:
            count+=1
            print(count)
            plt.title("Ising Model: ", fontsize=16)
            renderImage = plt.imshow(array2D)
            images.append([renderImage])
        ani = animation.ArtistAnimation(fig, images, interval=0.01, blit=True, repeat=False)
        plt.show()

    def display(self):
        """
        Method used to update the system a set number of iterations and to display the final 
        result
        """
        for i in range(self.iterations):
            print(i)
            self.model.update()
        plt.axis('off')
        plt.title("Ising Model: ", fontsize=16)
        plt.imshow(self.model.lattice)
        plt.savefig('Ising Model')

    def updatefig(self,i):
        """
        Method used to update the system for animation
        """
        self.model.update()
        self.im.set_array(self.model.lattice)
        return [self.im]
    def init(self):
        """
        Method used to init the animation
        """
        self.im = plt.imshow(self.model.lattice)
        return [self.im]
    def init_T(self):
        """
        Method used to init the animation
        """
        self.im = plt.imshow(self.model.lattice)
        self.temp = plt.plot([], [], color='k')
        return [self.im,self.temp]

    def animation(self):
        """
        Method used to create an animation of the model
        """
        fig, (ax1,ax2) = plt.subplots(1,2)
        fig = plt.figure()
        ani = animation.FuncAnimation(fig, self.updatefig,init_func=self.init, blit = True)
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
    