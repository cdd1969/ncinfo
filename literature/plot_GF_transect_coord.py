"""
from a 2-D geo-referenced field, extracts a transect across 2 specified coordinate points
author:onur.kerimoglu@hzg.de
"""
import os
import pickle
import LatLon
import netCDF4
import numpy as np
from scipy import interpolate
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


def main():
    #define coordinates of 2 points defining a transect
    crd1=[54.02,6.58]
    crd2=[55.00,6.8]
    arlen=100 #resulting array length

    fname='/home/onur/WORK/projects/GB/maecs/3d/simout/noBO/Ndep-kw1-02fzt-newpar-2002x2/extract_allL_sns-noBO-Ndep-kw1-02fzt-newpar.2003.nc'
    fname_topo='/home/onur/WORK/projects/GB/data/topo/topo_sns.nc'
    varname='hzg_maecs_phyC'
    tind=10
    lind=19

    fpath=os.path.dirname(fname)

    #original value map (for a given time&level)
    val_org,titlestr=getvar_ffile(fname,varname,tind,lind) #(98,140)

    #get a projection
    proj=get_proj(fpath)

    #original lat&lon (xc&yc) of the grid (corners)
    lon_org,lat_org=get_lonlat_org(fname_topo)

    #lat-lon of the transect
    lon_tr,lat_tr=get_lonlat_trans(crd1,crd2,arlen)

    #get cartesian projections
    xx,yx=proj(lon_org,lat_org)
    #grid centers
    xc=0.25*(xx[:-1,:-1]+xx[:-1,1:]+xx[1:,:-1]+xx[1:,1:])
    yc=0.25*(yx[:-1,:-1]+yx[:-1,1:]+yx[1:,:-1]+yx[1:,1:])
    xc_tr,yc_tr=proj(lon_tr,lat_tr)

    #interpolate
    val_tr=nn_interpolation(xc,yc,val_org,xc_tr,yc_tr,missing_value=-9999)

    #make plots
    makeplots(fpath,proj,xc,yc,val_org,xc_tr,yc_tr,val_tr,titlestr)

    return((xc_tr,yc_tr,val_tr))

def makeplots(fpath,proj,xc,yc,val_org,xc_tr,yc_tr,val_tr,titlestr):

    f = plt.figure(figsize=(8,4), dpi=96)
    f.text(0.5,0.96,titlestr, horizontalalignment='center')

    #2-D plot:
    ax=plt.subplot(1,2,1)
    #background:
    plot2Dmap(f,ax,[0,100],xc,yc,val_org,proj)
    #mark the transect:
    proj.plot(xc_tr,yc_tr)

    #1-D plot:
    ax=plt.subplot(1,2,2)
    plt.plot(np.arange(0,len(val_tr)),val_tr)

    plt.savefig(os.path.join(fpath,'transect-values.png'),dpi=300)

def plot2Dmap(f,ax,clim,x,y,v0,proj):
    #dim(latx)=dim(lonx)=98,139
    v=v0[:,:-1]

    #clim=[np.amin(v),np.amax(v)] #[np.amax(v)*.8,np.amax(v)] #
    pcf=proj.pcolormesh(x,y,v,cmap=plt.get_cmap('YlOrRd'),vmin=clim[0], vmax=clim[1])

    #coastlines, etc
    proj.drawcoastlines(color=(0.3,0.3,0.3),linewidth=0.5)
    proj.fillcontinents((1.0,1.0,1.0),lake_color=(0.9,0.9,1.0))
    ax.patch.set_facecolor((0.9,0.9,1.0))
    #retrieve the axes position to set the colorbar position
    pos1 = ax.get_position()

    cb=plt.colorbar(pcf)

def nn_interpolation(lon,lat,values,newlon,newlat,missing_value=-9999):
    #take all as 1-D arrays
    lon1=np.reshape(lon,lon.size)
    lat1=np.reshape(lat,lon.size)
    val1=np.reshape(values,lon.size)

    #find indices to keep:
    ikeep=np.where((lon1>=newlon.min()-0.5) & (lon1<=newlon.max()+0.5) &
                   (lat1>=newlat.min()-0.5) & (lat1<=newlat.max()+0.5))
    #trim the arrays
    lon1=lon1[ikeep]
    lat1=lat1[ikeep]
    val1=val1[ikeep]

    if val1.size==0:
	    return

    coords = np.asarray(zip(lon1,lat1))
    f = interpolate.NearestNDInterpolator(coords, val1)
    #f = interpolate.LinearNDInterpolator(coords, asarray(valuelist),fill_value=missing_value)
    res = f(newlon,newlat)
    #for whatever the reason, for indices falling out the data coverage,
    #interpolation doesn't result in nan by -8.??e+38
    maskdef=np.zeros(res.shape,dtype=bool)
    if hasattr(res,'mask'):
        maskdef=res.mask
    #res[where((maskdef) | (isnan(res)) | (res<0) | (extramask) )]=missing_value
    res[np.where((maskdef) | (np.isnan(res)) | (res<0) )]=missing_value
    return np.ma.masked_equal(res,missing_value)

def getvar_ffile(f,varname,tind,lind):
    nc=netCDF4.Dataset(f)
    var=nc.variables[varname]
    val_org=var[tind,lind,:,:-1]
    titlestr=var.long_name+' ['+var.units+']'
    return((val_org,titlestr))

def get_lonlat_org(fname_topo):
    topo=get_getm_bathymetry(fname_topo)
    return((topo['lons'],topo['lats']))

def get_getm_bathymetry(fname):
    ncB=netCDF4.Dataset(fname)
    ncBv=ncB.variables
    #bathymetry from topo_sns.nc
    lons=ncBv['lonx'][1:,:] #[98,139]  (originally [100,140])
    lats=ncBv['latx'][1:,:] #[98,139]  (originally [100,140])
    H = ncBv['bathymetry'][1:,:] #[98,139] (originally [99,139])
    topo={'H':H,'lats':lats, 'lons':lons,'Hunit':ncBv['bathymetry'].units}
    ncB.close()
    return(topo)

def get_lonlat_trans(crd1,crd2,arlen):
    ll1=LatLon.LatLon(crd1[0],crd1[1])
    ll2=LatLon.LatLon(crd2[0],crd2[1])
    stepvec=(ll2-ll1)/(arlen-1)
    steps=[ll1+x*stepvec for x in range(0,arlen)]
    lats=np.array([step.lat.decimal_degree for stepno,step in enumerate(steps)])
    lons=np.array([step.lon.decimal_degree for stepno,step in enumerate(steps)])
    return((lons,lats))

def get_proj(projpath):
    try:
        f=open(os.path.join(projpath,'proj.pickle'),'rb')
        (proj,)=pickle.load(f)
        f.close()
        print 'loaded '+projpath+'proj.pickle'
    except:
        #sns
        proj=Basemap(projection='lcc',
                           resolution='h',
                           llcrnrlon=-0.8,
                           llcrnrlat=50.7,
                           urcrnrlon=9.7,
                           urcrnrlat=55.7,
                           lat_0=54.0,
                           lon_0=6.)

    #pickle for later use:
    f=open(os.path.join(projpath,'proj.pickle'),'wb')
    pickle.dump((proj,),f) #,protocol=-1
    f.close()
    return(proj)

if __name__=="__main__":
    main()