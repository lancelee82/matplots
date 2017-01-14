#!/usr/bin/env python
# coding=utf-8

"""
Matplotlib Function Wrappers.
"""

import os.path
import random
import time


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# font file for chinese
SIMSUN_FILE = os.path.join(BASE_DIR, 'font', 'simsun.ttc')
from matplotlib.font_manager import FontProperties
MPL_FONT_SIMSUN = FontProperties(fname=SIMSUN_FILE, size=10) 


from matplotlib import pyplot
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator

import numpy as np
#from numpy import arange


MPL_PLOT_LINE_STYLE_YO_ = 'yo-'
MPL_PLOT_LINE_STYLE_GO_ = 'go-'
MPL_PLOT_LINE_STYLE_BO_ = 'bo-'
MPL_PLOT_LINE_STYLE_RO_ = 'ro-'
MPL_PLOT_LINE_STYLE_G__ = 'g--'
MPL_PLOT_LINE_STYLE_G_ = 'g-'
MPL_PLOT_LINE_STYLE_B_ = 'b-'
MPL_PLOT_LINE_STYLE_Y_ = 'y-'
MPL_PLOT_LINE_STYLE_R_ = 'r-'


COLORS = [
    '#ff0000', '#00ff00', '#0000ff', '#0ff000', '#000ff0',
    '#ee0000', '#00ee00', '#0000ee', '#0ee000', '#000ee0',
]


def plot_fig_get_name_by_time(s=''):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    fname = os.path.join(BASE_DIR, 'images', s + str(time.time()) + '.jpg')
    return fname


def plot_color_char_rand():
    c = hex(random.randint(1, 15))[2:]
    return c


def plot_color_get_by_rand(n=6):
    clr = '#'
    for i in range(n):
        clr += plot_color_char_rand()
    return clr


def plot_color_get_by_char(c='1'):
    clr = '#' + c * 6
    return clr


def plot_ylim_find_max(y):
    if isinstance(y[0], (list, tuple, set)):
        yy = [plot_ylim_find_max(yi) for yi in y]
        return max(yy)
    else:
        return max(y)


def plot_figure_axes(f=None, a=None):
    if not f:
        f = pyplot.figure(figsize=(7,7))
        a = f.add_subplot(111)

    if not a:
        a = f.add_subplot(111)

    return f, a


def plot_line(f=None, a=None, x=None, y=None, xlbs=None, ylbs=None,
              xticks=None, title=None, xlim=True, ylim=True,
              line_style=MPL_PLOT_LINE_STYLE_YO_, color=None,
              *args, **kwargs):
    f, a = plot_figure_axes(f, a)

    if color:
        a.plot(x, y, line_style, c=color)
    else:
        a.plot(x, y, line_style)

    if xlim:
        a.set_xlim(min(x)-1, max(x)+1)
    if ylim:
        # a.ylim(min(y)-1, max(y)+1)
        a.set_ylim(0, 500)

    if title:
        a.set_title(title, fontproperties=MPL_FONT_SIMSUN)
    if xlbs:
        a.set_xlabel(xlbs, fontproperties=MPL_FONT_SIMSUN)
    if ylbs:
        a.set_ylabel(ylbs, fontproperties=MPL_FONT_SIMSUN)

    if xticks:
        width = 0.3
        xr = range(len(x))
        xt = [i + width / 2.0 for i in xr]
        a.set_xticks(xr)  #xt)

        a.set_xticklabels(xticks,
                          horizontalalignment='right', #'center', #'left',
                          rotation=60,
                          fontproperties=MPL_FONT_SIMSUN)

    return f, a


def plot_bar(f=None, a=None, data=None, labels=None,
             xlbs=None, ylbs=None, title=None,
             *args, **kwargs):
    f, a = plot_figure_axes(f, a)

    pos = np.arange(len(data))
    b = a.bar(pos, data)
    a.set_xticks(pos)
    a.set_xticklabels(labels, horizontalalignment='left',
                      fontproperties=MPL_FONT_SIMSUN)

    if title:
        a.set_title(title, fontproperties=MPL_FONT_SIMSUN)
    if xlbs:
        a.set_xlabel(xlbs, fontproperties=MPL_FONT_SIMSUN)
    if ylbs:
        a.set_ylabel(ylbs, fontproperties=MPL_FONT_SIMSUN)

    def autolabel(rects):
        # attach some text labels
        for rect in rects:
            height = rect.get_height()
            a.text(rect.get_x() + rect.get_width() / 2.,
                   1.05 * height, '%d' % int(height),
                   ha='center', va='bottom')

    i = 6
    clr = '#'
    for bi in b:
        i += 1
        c = hex(i % 16)[2:]
        clr = '#fe' + c * 4
        bi.set_facecolor(clr)

    autolabel(b)

    return f, a


def plot_pie(f=None, a=None, data=None, labels=None, colors=None,
             *args, **kwargs):
    f, a = plot_figure_axes(f, a)

    pies = a.pie(data,
                 colors=colors,
                 #labels=labels,
                 autopct='%1.2f%%')
                 #radius=0.7)
                 #x#textprops=MPL_FONT_SIMSUN)

    #a.legend(pies[0], labels, loc='best', prop=MPL_FONT_SIMSUN)
    a.legend(pies[0], labels,
             loc='upper right', bbox_to_anchor=(1.1, 1.1),
             prop=MPL_FONT_SIMSUN)

    return f, a


def plot_multi_lines(f=None, a=None, x=None, ys=None, xlbs=None, ylbs=None,
                     xticks=None, legends=None, title=None, xlim=True, ylim=True,
                     line_style=MPL_PLOT_LINE_STYLE_YO_,
                     *args, **kwargs):
    f, a = plot_figure_axes(f, a)

    lines = []
    for y in ys:
        line = a.plot(x, y, line_style, color=plot_color_get_by_rand())
        lines.append(line)

    if xlim:
        a.set_xlim(min(x)-1, max(x)+1)
    if ylim:
        # a.ylim(min(y)-1, max(y)+1)
        a.set_ylim(0, 500)

    if title:
        a.set_title(title, fontproperties=MPL_FONT_SIMSUN)
    if xlbs:
        a.set_xlabel(xlbs, fontproperties=MPL_FONT_SIMSUN)
    if ylbs:
        a.set_ylabel(ylbs, fontproperties=MPL_FONT_SIMSUN)

    if xticks:
        width = 0.3
        xr = range(len(x))
        xt = [i + width / 2.0 for i in xr]
        a.set_xticks(xr)#xt)

        a.set_xticklabels(xticks,
                          horizontalalignment='right', #'center', #'left',
                          rotation=60,
                          fontproperties=MPL_FONT_SIMSUN)

    if legends:
        a.legend([line[0] for line in lines], legends, prop=MPL_FONT_SIMSUN)
        #a.legend(legends)
        #a.legend(legends, prop=MPL_FONT_SIMSUN)

        #for i, line in enumerate(lines):
        #    line[0].set_label(legends[i])
        #a.legend()

    return f, a


def plot_multi_bar(f=None, a=None, data=None, labels=None,
                   xlbs=None, ylbs=None, legends=None, title=None,
                   *args, **kwargs):
    f, a = plot_figure_axes(f, a)

    pos = np.arange(len(data[0]))

    bars = []
    for i, y in enumerate(data):
        stp = 1.0 / len(data)
        b = a.bar(pos + i * stp, y, width=stp - 0.05,
                  color=plot_color_get_by_rand())
        bars.append(b)

    # a.set_xlim(min(x)-1, max(x)+1)
    # a.ylim(min(y)-1, max(y)+1)
    a.set_ylim(0, plot_ylim_find_max(data) + 4)

    a.set_xticks(pos)
    a.set_xticklabels(labels, horizontalalignment='left',
                      fontproperties=MPL_FONT_SIMSUN)

    if title:
        a.set_title(title, fontproperties=MPL_FONT_SIMSUN)
    if xlbs:
        a.set_xlabel(xlbs, fontproperties=MPL_FONT_SIMSUN)
    if ylbs:
        a.set_ylabel(ylbs, fontproperties=MPL_FONT_SIMSUN)

    def autolabel(rects):
        # attach some text labels
        for rect in rects:
            height = rect.get_height()
            a.text(rect.get_x() + rect.get_width() / 2.,
                   1.05 * height, '%d' % int(height),
                   ha='center', va='bottom')

    for b in bars:
        autolabel(b)

    if legends:
        try:
            legends = [lgd.decode('utf=8') for lgd in legends]
        except:
            pass

        a.legend([b[0] for b in bars], legends, prop=MPL_FONT_SIMSUN)

    return f, a


def plot_scatter(f=None, a=None, x=None, y=None, s=20, c=None, alpha=None, 
                 xlbs=None, ylbs=None, xticks=None, title=None,
                 *args, **kwargs):
    f, a = plot_figure_axes(f, a)

    a.scatter(x, y, s=s, c=c, alpha=alpha)

    #a.set_xlim(min(x)-1, max(x)+1)
    # a.ylim(min(y)-1, max(y)+1)
    #a.set_ylim(0, 500)

    if title:
        a.set_title(title, fontproperties=MPL_FONT_SIMSUN)
    if xlbs:
        a.set_xlabel(xlbs, fontproperties=MPL_FONT_SIMSUN)
    if ylbs:
        a.set_ylabel(ylbs, fontproperties=MPL_FONT_SIMSUN)

    return f, a


def km_data_ys_gen_circle_top(xs, cp=(0.0, 0.0), radius=1.0):
    ys = []
    for i, x in enumerate(xs):
        #x#ang = math.pi * ((0.0 + i) / len(xs))
        xdis = math.fabs(x - cp[0])
        ang = math.acos(xdis / radius)
        y = cp[1] + radius * math.sin(ang)
        ys.append(y)

    return ys


def km_data_ys_gen_circle_bottom(xs, cp=(0.0, 0.0), radius=1.0):
    ys = []
    for i, x in enumerate(xs):
        #x#ang = -math.pi * ((0.0 + i) / len(xs))
        xdis = math.fabs(x - cp[0])
        ang = math.acos(xdis / radius)
        ang = math.pi * 2 - ang
        y = cp[1] + radius * math.sin(ang)
        ys.append(y)

    return ys


def plot_line_circle(f=None, a=None, cp=(0.0, 0.0), radius=1.0): # line_style

    cxs = np.arange(-radius, radius, 0.01)
    cxs = [cp[0] + cx for cx in cxs]
    cys = km_data_ys_gen_circle_top(cxs, cp=cp, radius=radius)
    #print cxs
    #print cys
    #dis = [km_geo_dist_pp(cp, (cxs[i], cys[i])) for i in range(len(cxs))]
    #print dis
    f, a = plot_line(f, a, cxs, cys, xlim=False, ylim=False,
                     line_style=MPL_PLOT_LINE_STYLE_G_)
    cys = km_data_ys_gen_circle_bottom(cxs, cp=cp, radius=radius)
    f, a = plot_line(f, a, cxs, cys, xlim=False, ylim=False,
                     line_style=MPL_PLOT_LINE_STYLE_G_)

    return f, a


def plot_line_rect():
    pass


def plot_line_shape(f=None, a=None, points=None, closed=True,
                    line_style=MPL_PLOT_LINE_STYLE_G_, color=None):

    if not points or len(points) <= 1:
        return

    x = [p[0] for p in points]
    y = [p[1] for p in points]

    if closed:
        x.append(points[0][0])
        y.append(points[0][1])

    f, a = plot_line(f, a, x, y, xlim=False, ylim=False,
                     line_style=line_style, color=color)

    return f, a


#def plot_pcolormesh(x, y, c):
def plot_pcolormesh(f=None, a=None, *args, **kwargs):
    f, a = plot_figure_axes(f, a)

    ##a.pcolormesh(*args, **kwargs)

    x = kwargs.get('x')
    y = kwargs.get('y')
    z = kwargs.get('z')

    levels = MaxNLocator(nbins=15).tick_values(z.min(), z.max())
    # pick the desired colormap, sensible levels, and define a normalization
    # instance which takes data values and translates those into levels.
    cmap = pyplot.get_cmap('PiYG')
    norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)

    #im = a.pcolormesh(x, y, z, cmap=cmap, norm=norm)
    im = a.pcolormesh(x, y, z)

    show_colorbar = kwargs.pop('show_colorbar', False)
    if show_colorbar:
        f.colorbar(im, ax=a)

    #a.set_title('pcolormesh with levels')

    return f, a


def plot_anim(f=None, a=None, rw=None, lnstyle='g-',
              xlim=[0, 255], ylim=[0, 255],
              niter=1000, doblit=True, auto_close=True):

    #fig, ax = mpl.plot_figure_axes()
    fig, ax = plot_figure_axes(f, a)

    ax.set_aspect('equal')
    ax.set_xlim(xlim[0], xlim[1])
    ax.set_ylim(ylim[0], ylim[1])
    ax.hold(True)

    x, y = rw.next()

    pyplot.show(False)
    pyplot.draw()

    if doblit:
        # cache the background
        background = fig.canvas.copy_from_bbox(ax.bbox)

    # Line2D(_line0)
    points = ax.plot(x, y, lnstyle)[0]

    for ii in xrange(niter):

        try:
            x, y = rw.next()
        except Exception as e:
            break
        # update the xy data
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

    if auto_close:
        pyplot.close(fig)
    else:
        pyplot.show(True)


def plot_imshow(*args, **kwargs):
    pyplot.imshow(*args, **kwargs)


def plot_show():
    # adjust spacing between subplots so `ax1` title and `ax0` tick labels
    # don't overlap
    #fig.tight_layout()

    pyplot.show()


def plot_savefig(*args, **kwargs):
    pyplot.savefig(*args, **kwargs)


if __name__ == '__main__':
    pass
