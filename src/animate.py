from model import Model
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import colors
from matplotlib import patches
class animate(object):
    def __init__(self, dimension, Temperature, iterations):
        self.model = Model(dimension,Temperature)
        self.model.set_up_random_state()
        self.iterations = iterations
        self.history = np.array([[]])
        self.history = [self.model.lattice.copy()]
        

       
    def evolve(self):
        for i in range(self.iterations):
            print(i)
            self.model.update()
            self.history += [self.model.lattice.copy()]


    def animate(self):
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
        for i in range(self.iterations):
            print(i)
            self.model.update()
        plt.axis('off')
        plt.title("Ising Model: ", fontsize=16)
        plt.imshow(self.model.lattice)
        plt.show()
    def updatefig(self,i):
        self.model.update()
        self.im.set_array(self.model.lattice)
        return [self.im]
    def init(self):
        self.im = plt.imshow(self.model.lattice)
        return [self.im]
    def animation(self):
        
        fig = plt.figure()
        ani = animation.FuncAnimation(fig, self.updatefig,init_func=self.init,interval = 0.01, blit = True)
        plt.show()
    def update(self,num,x,y, line):
        x += [num]
        self.model.update()
        y += [Model.get_energy(self.model.lattice)]
        line.set_data(x, y)
        line.axes.axis([0, self.iterations, -10000, 0])
        return line,
    def energy_animation(self):
        fig, ax = plt.subplots()
        x = []
        y = []
        line, = ax.plot([], [], color='k')
        ani = animation.FuncAnimation(fig, self.update, frames =self.iterations,fargs=[x,y,line],
                              interval=0.1, blit=True,repeat=False)
        plt.show()

        
