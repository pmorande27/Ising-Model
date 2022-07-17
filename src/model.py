import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve,generate_binary_structure
from sympy import Mod
import random 
import math
class Model(object):
    def __init__(self,N,T) -> None:
        self.N = N
        self.lattice = np.ones((self.N,self.N))
        self.T = T
        self.k = 1
        self.beta = 1/(self.k*T)
    def __str__(self) -> str:
        return str(self.lattice)
    def set_up_random_state(self):
        random = np.random.random((self.N,self.N))
        self.lattice[random>=0.50] = 1
        self.lattice[random<=0.50] = -1

    def show_state(self):
        plt.imshow(self.lattice)
        plt.show()
    @staticmethod
    def get_energy(lattice):
        kernel = generate_binary_structure(2,1)
        kernel[1][1] = False
        energy_array = - lattice*convolve(lattice,kernel,mode='constant',cval=0)
        return energy_array.sum()
    @staticmethod
    def generate_new_state(lattice):
        new_lattice =np.copy(lattice)
        position = np.random.randint(len(new_lattice),size = 2)
        if  new_lattice[position[0],position[1]] == 1:
            new_lattice[position[0],position[1]] = -1
        else:
            new_lattice[position[0],position[1]] = 1
        return new_lattice

            

       
        return lattice
    def update(self):
        while True:
            candidate_state = Model.generate_new_state(self.lattice)
            delta_E =   Model.get_energy(candidate_state)-Model.get_energy(self.lattice)
            if delta_E < 0:
                self.lattice = candidate_state
                break
            else:
                if random.random() <= math.e**(-self.beta*delta_E):
                    self.lattice = candidate_state
                    break
    



    

