
from numpy import linspace,cos,pi, meshgrid
import numpy as np
import matplotlib.pyplot as plt

x = linspace(0,9,10)+.5
y = linspace(0,9,10)+.5   # your array
x,y=meshgrid(x,y)
x=x.flatten()
y=y.flatten()

fig = plt.figure()
ax = fig.add_subplot(111)

line, = ax.plot(x, y, 'b',picker=10)
line.set_visible(False)
ax.pcolormesh(np.random.randn(10,10))

def onpick(event):

    if event.artist!=line:  #check that you clicked on the object you wanted
        return True     
    if not len(event.ind):  #check the index is valid
        return True
    ind = event.ind[0]

    ax.plot(x[ind],y[ind],'ro')

    fig.canvas.draw() 
    return True

fig.canvas.mpl_connect('pick_event', onpick)
plt.show()