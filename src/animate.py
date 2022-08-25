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
        self.H = H
        
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
        self.temp, = ax2.bar(' ',self.model.T)
        ax2.set_title('Temperature')
        ax1.set_title('Ising Model')
        ax3.set_title('Energy')
        ax4.set_title('Magnetization')
        ani = animation.FuncAnimation(fig, self.update_all, frames =self.iterations,fargs=[x_energy,y_energy,x_magnet,y_magnet,line_energy,line_magnet],
                              interval=0.1, blit=True,repeat=False)
        plt.show()

    