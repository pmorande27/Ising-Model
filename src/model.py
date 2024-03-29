"""
Model module
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve,generate_binary_structure
from sympy import Mod
import random
import math
class Model(object):
    """
    Class to represent the Ising Model
    """
    def __init__(self,N,T,H) -> None:
        """
        Constructor of the class
        """
        self.N = N
        self.lattice = np.ones((self.N,self.N))
        self.T = T
        self.k = 1
        self.H = H
        self.beta = 1/(self.k*T)
        
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
        return energy_array.sum()/2+magnetic_energy

    @staticmethod
    def generate_new_state(lattice) -> np.array:
        """
        Method used to generate a new state aka Glouber Dynamics
        """
        new_lattice =np.copy(lattice)
        position = np.random.randint(len(new_lattice),size = 2)
        new_lattice[position[0],position[1]] = -1*new_lattice[position[0],position[1]]
        return new_lattice
    def get_magnetisation(self) -> float:
        """
        Method used to get the magnetisation of the lattice
        """
        return self.lattice.sum()
    '''
    def update(self) -> None:
        """
        Method used to generate a new state aka Metropolis Algorithm
        """
        if abs(self.get_magnetisation()) == self.N**2:
            print('material completely magnetized')
            return
        while True:
            candidate_state = Model.generate_new_state(self.lattice)
            delta_E =  Model.get_energy(candidate_state,self.H)-Model.get_energy(self.lattice,self.H)
            if delta_E < 0:
                self.lattice = candidate_state
                break
            else:
                if random.random() <= math.e**(-self.beta*delta_E):
                    self.lattice = candidate_state
                    break
    
    '''
  
        
    
    def update(self):
        if abs(self.get_magnetisation()) == self.N**2:
            print('material completely magnetized')
            return
        while True:
            x,y = np.random.randint(self.N,size = 2)
            spin_i = self.lattice[x,y] #initial spin
            spin_f = spin_i*-1 #proposed spin flip
            # compute change in energy
            E_i = 0
            E_f = 0
            if x>0:
                E_i += -spin_i*self.lattice[x-1,y]
                E_f += -spin_f*self.lattice[x-1,y]
            if x<self.N-1:
                E_i += -spin_i*self.lattice[x+1,y]
                E_f += -spin_f*self.lattice[x+1,y]
            if y>0:
                E_i += -spin_i*self.lattice[x,y-1]
                E_f += -spin_f*self.lattice[x,y-1]
            if y<self.N-1:
                E_i += -spin_i*self.lattice[x,y+1]
                E_f += -spin_f*self.lattice[x,y+1]
            delta_E = E_f-E_i
            if delta_E < 0:
                self.lattice[x,y] = spin_f
                break
            else:
                if random.random() <= math.e**(-self.beta*delta_E):
                    self.lattice[x,y] = spin_f
                    break

        


    

