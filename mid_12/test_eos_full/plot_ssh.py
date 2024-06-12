#!/usr/bin/env python
import numpy as np
import os
import sys
import subprocess
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import scipy.io
import xarray as xr
import pandas as pd
import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature

def outline_my_domain(ax,plon,plat):
    #Arctic DOMAIN OUTLINE
    for j in range(plat.shape[0]-1):
        ax.plot((plon[j,0],plon[j+1,0]),(plat[j,0],plat[j+1,0]),linewidth=1.5,color='k',transform=ccrs.PlateCarree(),zorder=42)
        ax.plot((plon[j,-1],plon[j+1,-1]),(plat[j,-1],plat[j+1,-1]),linewidth=1.5,color='k',transform=ccrs.PlateCarree(),zorder=42)
    for ii in range(plat.shape[1]-1):
        ax.plot((plon[0,ii],plon[0,ii+1]),(plat[0,ii],plat[0,ii+1]),linewidth=1.5,color='k',transform=ccrs.PlateCarree(),zorder=42)
        ax.plot((plon[-1,ii],plon[-1,ii+1]),(plat[-1,ii],plat[-1,ii+1]),linewidth=1.5,color='k',transform=ccrs.PlateCarree(),zorder=42)


lst_file = []

lst = subprocess.getoutput('ls run44/20120101.ocean_daily.nc')
lst = lst.split()
lst_file = lst_file + lst

grd = xr.open_dataset('sea_ice_geometry.nc')
lat = grd.geolat
lon = grd.geolon
clat = grd.geolatb.data
clon = grd.geolonb.data
dims = clat.shape

levels = np.arange(-2.0, 2.0, 0.1)
cmap = plt.cm.get_cmap("seismic")

for file in lst_file:
    print("Plotting "+file)
    nc = xr.open_dataset(file)
    times = nc.time.data
    ntimes = len(times)
    for it in range(ntimes):
        date_tag = pd.to_datetime(times[it]).strftime('%H:%M, %d %B %Y')
        var_val = nc.ssh.data[it,:,:]
        fig, axs = plt.subplots(1,1,sharex='col', sharey='row',gridspec_kw={'hspace': 0.01, 'wspace': 0.01},
                                 subplot_kw=dict(projection=ccrs.NorthPolarStereo(central_longitude=160.0)),
                                 figsize=(10,8))
        C = axs.pcolormesh(clon, clat, var_val, transform=ccrs.PlateCarree(), zorder=3,
                                vmin=-.6, vmax=0.6, cmap='seismic')

#       CS = axs.contour(clon,clat,var_val,levels, colors='k', transform=ccrs.PlateCarree())
        axs.set_extent([-180, 180, 49, 90], ccrs.PlateCarree())
        cbar = plt.colorbar(C, orientation='vertical', shrink=.5, pad=.05, aspect=20)
        cbar.ax.tick_params(labelsize=15)

#       axs.clabel(CS, levels[::2], manual=False, inline=True, inline_spacing = 0,
#                       fmt='%1.1f',fontsize='smaller')
        axs.add_feature(cfeature.LAND,color='blanchedalmond',zorder=50)
        axs.coastlines(zorder=50)
        outline_my_domain(axs,clon,clat)

        # ADDING GRID LINES AND GRID LABELS
        gl = axs.gridlines(draw_labels=True)

        gl.xlocator = mticker.FixedLocator([150, 180, -150, -120, -90, -60])
        gl.ylocator = mticker.FixedLocator([50, 65, 80])

        gl.xlabel_style = {'size': 15}
        gl.ylabel_style = {'size': 15}
        plt.suptitle('Sea Surface Height (m)')

        plt.title(date_tag, fontsize=20)
#       fig.text(140.0, 70.0, plt_lab, transform=ccrs.PlateCarree(), fontsize=25, ha='center', zorder=53)
        fname = ('movie_ssh/frame_%(number)04d.png'%{'number': it})
        print(date_tag)
        cbar.ax.tick_params(labelsize=15)

        plt.savefig(fname)
        plt.close()

    nc.close()
