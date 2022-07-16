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
        self.evolve()
        

       
    def evolve(self):
        for i in range(self.iterations):
            print(i)
            self.model.update()
            self.history += [self.model.lattice.copy()]


    def animate(self):
        fig = plt.figure()
        images = []
        count = 0
        for array2D in self.history:
            count+=1
            print(count)
            plt.title("Ising Model: ", fontsize=16)
            renderImage = plt.pcolor(array2D, cmap=colors.ListedColormap(["Red", "Green"]), edgecolors='k', linewidth=2,
                                     animated=True)
            images.append([renderImage])
            redLabel = patches.Patch(color='red', label='Down')
            greenLabel = patches.Patch(color='green', label='Up')
            plt.legend(handles=[redLabel, greenLabel])
        ani = animation.ArtistAnimation(fig, images, interval=0.01, blit=True, repeat=False)
        plt.show()

    def display(self):
        plt.axis('off')
        plt.title("Ising Model: ", fontsize=16)
        redLabel = patches.Patch(color='red', label='Down')
        greenLabel = patches.Patch(color='green', label='Up')
        plt.legend(handles=[redLabel, greenLabel])
        plt.pcolor(self.model.lattice, cmap=colors.ListedColormap(["Red", "Green"]), edgecolors='k', linewidth=2)
        plt.show()