"""
Main file
"""
from animate import Animation
from animate_variable_temperature import Animation_variable_temperature
from model import Model
import matplotlib.pyplot as plt
def main():
    """
    Main method
    """
    animation = Animation_variable_temperature(100, 10,2, 0.001, 10000*4,0)
    animation.all_animations()
main()
