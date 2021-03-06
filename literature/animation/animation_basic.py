"""
Matplotlib Animation Example

author: Jake Vanderplas
email: vanderplas@astro.washington.edu
website: http://jakevdp.github.com
license: BSD
Please feel free to use and modify this, but keep the above information. Thanks!
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 5), ylim=(0, 5))
#line, = ax.plot([], [], lw=2)
a=np.random.random((5,5))
im=plt.imshow(a,interpolation='none')

# initialization function: plot the background of each frame
def init():
    im.set_data(np.random.random((5,5)))
    return [im]

# animation function.  This is called sequentially
def animate(i):
    a=im.get_array()
    #a=a*np.exp(-0.001*i)    # exponential decay of the values
    a=np.random.random((5,5))
    im.set_array(a)
    return [im]

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200000, interval=10, blit=True)



plt.show()