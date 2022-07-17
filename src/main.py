from model import Model
from animate import animate
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import colors
from matplotlib import patches
def main():
    a = animate(50,1,10000)
    a.energy_animation_save()

main()
'''
model = Model(150,1)
model.set_up_random_state()
im = plt.imshow(model.lattice,animated=True)
fig = plt.figure()

def updatefig(i):
    model.update()
    im.set_array(model.lattice)
    return [im]
ani = animation.FuncAnimation(fig, updatefig,interval = 50, blit = True)
plt.show()
'''
