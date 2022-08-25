import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve,generate_binary_structure
from sympy import Mod
import random
import math

class Model_variable_temperature(object):
    """
    Class to represent the Ising Model
    """
    def __init__(self,N,T_max, T_min, delta_T ,H) -> None:
        """
        Constructor of the class
        """
        self.N = N
        self.lattice = np.ones((self.N,self.N))
        self.T = T_max
        self.T_min = T_min
        self.delta_T = delta_T
        self.k = 1
        self.H = H
        self.beta = 1/(self.k*self.T)
        
    def __str__(self) -> str:
        """
        Override to string method for printing
        """
        return str(self.lattice)

    def set_up_random_state(self) -> None:
        """
        Method used to set up the model in a random state with 50% of the spins up and
        50% of the spins down
        """
        random = np.random.random((self.N,self.N))
        self.lattice[random>=0.50] = 1
        self.lattice[random<=0.50] = -1

    def show_state(self) -> None:
        """
        Method used to show the state with a plot
        """
        plt.imshow(self.lattice)
        plt.show()

    @staticmethod
    def get_energy(lattice, H) -> float:
        """
        Method used to get the energy of the system
        """
        kernel = generate_binary_structure(2,1)
        kernel[1][1] = False
        energy_array = - lattice*convolve(lattice,kernel,mode='constant',cval=0)
        magnetic_energy = -H * lattice.sum()
        return energy_array.sum()+magnetic_energy

    @staticmethod
    def generate_new_state(lattice) -> np.array:
        """
        Method used to generate a new state aka Glouber Dynamics
        """
        new_lattice =np.copy(lattice)
        position = np.random.randint(len(new_lattice),size = 2)
        if  new_lattice[position[0],position[1]] == 1:
            new_lattice[position[0],position[1]] = -1
        else:
            new_lattice[position[0],position[1]] = 1
        return new_lattice

    def update(self) -> None:
        """
        Method used to generate a new state aka Metropolis Algorithm
        """
        while True:
            candidate_state = Model_variable_temperature.generate_new_state(self.lattice)
            delta_E =  Model_variable_temperature.get_energy(candidate_state,self.H)-Model_variable_temperature.get_energy(self.lattice,self.H)
            if delta_E < 0:
                self.lattice = candidate_state
                break
            else:
                if random.random() <= math.e**(-self.beta*delta_E):
                    self.lattice = candidate_state
                    break
        if self.T - self.delta_T <self.T_min:
            pass
        else:
            self.T -= self.delta_T
            self.beta = 1/(self.k*self.T)

    def get_magnetisation(self) -> float:
        """
        Method used to get the magnetisation of the lattice
        """
        return self.lattice.sum()
