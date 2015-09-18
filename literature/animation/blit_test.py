import matplotlib.pyplot as plt
import numpy as np
import time
"""
x = np.arange(0, 2*np.pi, 0.1)
y = np.sin(x)

fig, axes = plt.subplots(nrows=6)

styles = ['r-', 'g-', 'y-', 'm-', 'k-', 'c-']
def plot(ax, style):
    return ax.plot(x, y, style, animated=True)[0]
lines = [plot(ax, style) for ax, style in zip(axes, styles)]

# Let's capture the background of the figure

fig.show()
backgrounds = [fig.canvas.copy_from_bbox(ax.bbox) for ax in axes]

# We need to draw the canvas before we start animating...
fig.canvas.draw()

tstart = time.time()
for i in xrange(1, 2000):
    items = enumerate(zip(lines, axes, backgrounds), start=1)
    for j, (line, ax, background) in items:
        fig.canvas.restore_region(background)
        line.set_ydata(np.sin(j*x + i/10.0))
        ax.draw_artist(line)
        fig.canvas.blit(ax.bbox)

"""
fig = plt.figure()
ax = fig.add_subplot(111)

y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)
x = np.linspace(0, 2 * np.pi, 120)

def f(x, y):
    return np.sin(x) + np.cos(y)


im = ax.imshow(f(x, y), cmap=plt.get_cmap('jet'))
global im
fig.show()

background = [fig.canvas.copy_from_bbox(ax.bbox)]

print background
# We need to draw the canvas before we start animating...
fig.canvas.draw()

def updatefig(*args):
    global x, y, im
    print 'im is :', im
    x += np.pi / 15.
    y += np.pi / 20.
    im.set_data(f(x, y))
    return im,

for i in xrange(1, 2000):
    print i
    print '-'*50
    # im = updatefig()
    x += np.pi / 15.
    y += np.pi / 20.
    im.set_data(f(x, y))
    #fig.canvas.update()
    ax.draw_artist(im)
    fig.canvas.restore_region(background)
    fig.canvas.blit(ax.bbox)


#print 'FPS:' , 2000/(time.time()-tstart)