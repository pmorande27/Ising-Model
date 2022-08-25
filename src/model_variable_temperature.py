import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve,generate_binary_structure
from sympy import Mod
import random
import math
from model import Model

class Model_variable_temperature(Model):
    """
    Class to represent the Ising Model
    """
    def __init__(self,N,T_max, T_min, delta_T ,H) -> None:
        """
        Constructor of the class
        """
        super().__init__(N,T_max,H)
        self.T_min = T_min
        self.delta_T = delta_T
    def update(self) -> None:
        """
        Method used to generate a new state aka Metropolis Algorithm
        """
        super().update()
        if self.T - self.delta_T <self.T_min:
            pass
        else:
            self.T -= self.delta_T
            self.beta = 1/(self.k*self.T)
