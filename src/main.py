"""
Main file
"""
from animate import Animation
from animate_variable_temperature import Animation_variable_temperature
from model import Model
import matplotlib.pyplot as plt
import numpy as np
def main():
    """
    Main method
    """
    animation = Animation(600, 10000*4, 100,0)
    animation.display()
main()
