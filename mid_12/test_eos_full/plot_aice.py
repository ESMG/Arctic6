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

#lst = subprocess.getoutput('ls run44/20120101.ocean_daily.nc')
#lst = lst.split()
#lst_file = lst_file + lst
lst_file = ["19930101.boem_aice.nc"]

grd = xr.open_dataset('geometry_subset.nc')
lat = grd.geolat.data
lon = grd.geolon.data
lon = np.where(lon < 0.0, lon+360., lon)
clat = grd.geolatb.data
clon = grd.geolonb.data
clon = np.where(clon < 0.0, clon+360., clon)
dims = clat.shape


for file in lst_file:
    print("Plotting "+file)
    nc = xr.open_dataset(file)
    times = nc.time.data
    ntimes = len(times)
#   for it in range(ntimes):
    for it in range(-1,0):
        date_tag = pd.to_datetime(times[it]).strftime('%H:%M, %d %B %Y')
        aice = nc.aice.data[it,:,:]
        plt.figure(figsize=(12,9))
        ax = plt.subplot(1, 1, 1, projection=ccrs.Mercator(central_longitude=190.0))
#       ax = plt.subplot(1, 1, 1)

        ax.set_extent([175, 230, 66, 76], ccrs.PlateCarree())
        ax.add_feature(cartopy.feature.OCEAN, zorder=0)
        ax.add_feature(cartopy.feature.LAND, color='blanchedalmond', zorder=0, edgecolor='black')

        ax.gridlines()

        C = ax.pcolormesh(clon, clat, aice, transform=ccrs.PlateCarree(), zorder=3,
                          vmin=0, vmax=1.0, cmap='bone')
        cbar = plt.colorbar(C, orientation='horizontal', shrink=.5, pad=.05, aspect=20)
        cbar.ax.tick_params(labelsize=15)

        ax.coastlines(zorder=50)
#       outline_my_domain(ax,clon,clat)

        gl = ax.gridlines(draw_labels=True)

        gl.xlocator = mticker.FixedLocator([180, -170, -160, -150, -140, -130])
        gl.ylocator = mticker.FixedLocator([70, 75, 80])

        gl.xlabel_style = {'size': 15}
        gl.ylabel_style = {'size': 15}
        plt.suptitle('Sea Ice Concentration', fontsize=20)

        plt.title(date_tag, fontsize=18)
#       fig.text(140.0, 70.0, plt_lab, transform=ccrs.PlateCarree(), fontsize=25, ha='center', zorder=53)
#       fname = ('movie_ovel/frame_%(number)04d.png'%{'number': it})
        fname = ('siconc.png')
        print(date_tag)
#       cbar.ax.tick_params(labelsize=15)

        plt.savefig(fname)
        plt.close()

    nc.close()
