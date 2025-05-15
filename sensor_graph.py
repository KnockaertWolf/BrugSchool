import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from settings import *  
from data import getDataToShow  

matplotlib.use("TkAgg")
root = plt.figure()
fig1 = root.add_subplot(1, 1, 1)

line, = fig1.plot([], [], color=fig1_C)

fig1.set(title=fig1_T, xlabel=fig1_X, ylabel=fig1_Y)

def animate(i):
    """Animatie functie"""
    try:
        xArray, yArray = getDataToShow(fig1_F)

        if len(xArray) != len(yArray):
            raise ValueError("Lengte van x en y komen niet overeen")
        line.set_data(xArray, yArray)

  
        fig1.relim()
        fig1.autoscale_view()

ani = anim.FuncAnimation(root, animate, interval=fig1_U, cache_frame_data=False)

plt.show()

