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
    animation = Animation(100, 2, 10000*4,0)
    animation.all_animations()
main()
