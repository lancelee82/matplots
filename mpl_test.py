"""
"""

import math
import random
import time

import numpy as np
from matplotlib import pyplot as plt

import matplots as mpl


def mpl_test_gen_data_0():
    x = []
    y = []
    for i in range(20):
        x.append(random.random())
        y.append(random.random())
    return x, y

def mpl_test_gen_data_1():
    xx, yy = np.meshgrid(np.arange(0, 1, 0.01),
                         np.arange(0, 1, 0.01))
    c = np.ndarray(xx.shape)
    #print c.shape
    for i in range(c.shape[0]):
        for j in range(c.shape[1]):
            if i > j:
                c[i][j] = 1
            elif i > j / 3:
                c[i][j] = 2
            else:
                c[i][j] = 0

    print xx.shape

    return xx, yy, c

def mpl_test_1():
    xx, yy, c = mpl_test_gen_data_1()

    f = plt.pcolormesh(xx, yy, c)
    print f

    #colors = np.arange(0.0, 1.0, 1.0/len(x))
    #f, a = mpl.plot_scatter(None, None, x, y, c=colors)

    plt.show()


def mpl_test_2():
    xx, yy, c = mpl_test_gen_data_1()

    f, a = mpl.plot_figure_axes()

    ##a.pcolormesh(xx, yy, c)
    f, a = mpl.plot_pcolormesh(f, a, xx, yy, c)

    x, y = mpl_test_gen_data_0()
    colors = np.arange(0.0, 1.0, 1.0/len(x))
    f, a = mpl.plot_scatter(f, a, x, y, c=colors)

    mpl.plot_show()


# http://stackoverflow.com/questions/11874767/real-time-plotting-in-while-loop-with-matplotlib
def randomwalk(dims=(256, 256), n=20, sigma=5, alpha=0.95, seed=1):
    """ A simple random walk with memory """

    r, c = dims
    gen = np.random.RandomState(seed)
    pos = gen.rand(2, n) * ((r,), (c,))
    old_delta = gen.randn(2, n) * sigma

    while True:
        delta = (1. - alpha) * gen.randn(2, n) * sigma + alpha * old_delta
        pos += delta
        for ii in xrange(n):
            if not (0. <= pos[0, ii] < r):
                pos[0, ii] = abs(pos[0, ii] % r)
            if not (0. <= pos[1, ii] < c):
                pos[1, ii] = abs(pos[1, ii] % c)
        old_delta = delta
        yield pos


def run(niter=1000, doblit=True):
    """
    Display the simulation using matplotlib, optionally using blit for speed
    """

    #fig, ax = plt.subplots(1, 1)
    fig, ax = mpl.plot_figure_axes()

    ax.set_aspect('equal')
    ax.set_xlim(0, 255)
    ax.set_ylim(0, 255)
    ax.hold(True)

    rw = randomwalk()
    x, y = rw.next()

    plt.show(False)
    plt.draw()

    if doblit:
        # cache the background
        background = fig.canvas.copy_from_bbox(ax.bbox)

    ##points = ax.plot(x, y, 'o')[0]
    points = ax.plot(x, y, 'g-')[0]
    print points

    tic = time.time()

    for ii in xrange(niter):

        # update the xy data
        x, y = rw.next()
        points.set_data(x, y)

        if doblit:
            # restore background
            fig.canvas.restore_region(background)

            # redraw just the points
            # AttributeError: draw_artist can only be used after
            # an initial draw which caches the render
            #x#ax.draw_artist(points)
            #x#ax.draw(points)
            fig.canvas.draw()

            # fill in the axes rectangle
            fig.canvas.blit(ax.bbox)

        else:
            # redraw everything
            fig.canvas.draw()

    plt.close(fig)
    print "Blit = %s, average FPS: %.2f" % (
        str(doblit), niter / (time.time() - tic))


def plot_anim(rw, lnstyle='g-', xlim=255, ylim=255,
              niter=1000, doblit=True, auto_close=True):

    #fig, ax = plt.subplots(1, 1)
    fig, ax = mpl.plot_figure_axes()

    ax.set_aspect('equal')
    ax.set_xlim(0, xlim)
    ax.set_ylim(0, ylim)
    ax.hold(True)

    ##rw = randomwalk()
    x, y = rw.next()

    plt.show(False)
    plt.draw()

    if doblit:
        # cache the background
        background = fig.canvas.copy_from_bbox(ax.bbox)

    points = ax.plot(x, y, 'o')[0]
    ##points = ax.plot(x, y, lnstyle)[0]
    print points

    tic = time.time()

    for ii in xrange(niter):

        # update the xy data
        x, y = rw.next()
        points.set_data(x, y)

        if doblit:
            #x#fig.canvas.draw()

            # restore background
            fig.canvas.restore_region(background)

            # redraw just the points
            # AttributeError: draw_artist can only be used after
            # an initial draw which caches the render
            #x#ax.draw_artist(points)
            #x#ax.draw(points)
            fig.canvas.draw()

            # fill in the axes rectangle
            fig.canvas.blit(ax.bbox)

        else:
            # redraw everything
            fig.canvas.draw()

    if auto_close:
        plt.close(fig)
    
    print "Blit = %s, average FPS: %.2f" % (
        str(doblit), niter / (time.time() - tic))


def mpl_test_4():
    rw = randomwalk()
    #plot_anim(rw)
    mpl.plot_anim(None, None, rw, lnstyle='go')


if __name__ == '__main__':
    #mpl_test_1()
    #mpl_test_2()

    #run(doblit=True)
    #run(doblit=False)

    mpl_test_4()
