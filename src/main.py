"""
Main file
"""
from animate import Animation
from animate_variable_temperature import Animation_variable_temperature
def main():
    """
    Main method
    """
    animation = Animation_variable_temperature(100, 10,2, 0.001, 10000*2,0)
    animation.animate()

main()
