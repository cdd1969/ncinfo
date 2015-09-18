#! user/bin/env python

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np


def plot(crd1, crd2, title, **kwargs):
    arlen = 10
    lons, lats = get_lonlat_trans(crd1, crd2, arlen)
    
    fig = plt.figure()
    fig.suptitle(title)

    map = Basemap(**kwargs)

    map.drawcoastlines()
    y, x = map(lats, lons)
    map.scatter(x, y, marker='D', color='m')
    map.plot(x, y, color='m')
    map.plot((x[0], x[-1]), (y[0], y[-1]), 'm--')
    plt.show()

def get_lonlat_trans(crd1, crd2, arlen):
    d_lat = crd2[0] - crd1[0]
    d_lon = crd2[1] - crd1[1]
    step_lat = d_lat/float(arlen-1)
    step_lon = d_lon/float(arlen-1)
    lats = np.array([crd1[0] + step_lat*x for x in xrange(arlen)])
    lons = np.array([crd1[1] + step_lon*x for x in xrange(arlen)])
    
    return(lons, lats)

def plot1():
    crd1 = [10., 10.]
    crd2 = [50., 50.]

    arlen = 10
    lons, lats = get_lonlat_trans(crd1, crd2, arlen)
    
    fig = plt.figure()
    fig.suptitle('Lambert Conformal Conic')

    map = Basemap( projection='lcc',
                   lat_0=40,
                   lon_0=40, 
                   resolution='l',
                   llcrnrlon=0,
                   llcrnrlat=0,
                   urcrnrlon=80,
                   urcrnrlat=80, )

    map.drawcoastlines()
    y, x = map(lats, lons)
    map.scatter(x, y, marker='D', color='m')
    map.plot(x, y, color='m')
    map.plot((x[0], x[-1]), (y[0], y[-1]), 'm--')
    plt.show()


def plot2():
    crd1 = [3., 52.]
    crd2 = [8., 55.]
    arlen = 10
    lons, lats = get_lonlat_trans(crd1, crd2, arlen)

    fig = plt.figure()
    fig.suptitle('Lambert Conformal Conic')

    map = Basemap( projection='lcc',
                   lat_0=54.0,
                   lon_0=6.,
                   resolution='l',
                   llcrnrlon=-2,
                   llcrnrlat=50,
                   urcrnrlon=10,
                   urcrnrlat=56, )

    map.drawcoastlines()
    x, y = map(lats, lons)
    map.scatter(x, y, marker='D', color='m')
    map.plot(x, y, color='m')
    map.plot((x[0], x[-1]), (y[0], y[-1]), 'm--')
    plt.show()


def plot3():
    plot([3., 52.], [8., 55.], 'Lambert Conformal Conic', 
        projection='lcc', lat_0=54.0, lon_0=6., resolution='l', llcrnrlon=-2, llcrnrlat=50, urcrnrlon=10, urcrnrlat=56)
def plot4():
    plot([10., 10.], [50., 50.], 'Lambert Conformal Conic', 
        projection='lcc', lat_0=40, lon_0=40,  resolution='l', llcrnrlon=0, llcrnrlat=0, urcrnrlon=80, urcrnrlat=80 )
if __name__=="__main__":
    plot1()  # example Lambert conic conformal
    plot4()
    plot2()  # example Lambert conic conformal
    plot3()  # example Lambert conic conformal
