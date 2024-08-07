import numpy as np
import netCDF4
import os
import sys
import subprocess
import pyroms
from pyroms_toolbox import jday2date
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# draw line around map projection limb.
# color background of map projection region.
# missing values over land will show up this color.
# plot sst, then ice with pcolor
# add a title.
#year = int(sys.argv[1])
#lst_year = [year]

lst_file = []

#for year in lst_year:
#    year = np.str(year)
#lst = subprocess.getoutput('ls clima/*.nc')
lst = subprocess.getoutput('ls run04/19800104.ice_daily.nc')
#lst = subprocess.getoutput('ls months/1991_04.nc')
lst = lst.split()
lst_file = lst_file + lst

grd = netCDF4.Dataset('sea_ice_geometry.nc', "r")

clat = grd.variables["geolat"][:]
clon = grd.variables["geolon"][:]

m = Basemap(projection='stere', lat_0=90, lon_0=160, llcrnrlon=-230,
    llcrnrlat=44, urcrnrlon=-65, urcrnrlat=40, resolution='h')
x, y = m(clon, clat)
levels = np.arange(0.0, 0.0010, 0.0005)
cmap = plt.cm.get_cmap("YlOrRd")
#cmap = plt.cm.get_cmap("bone")

for file in lst_file:
    print("Plotting "+file)
    nc = netCDF4.Dataset(file, "r")
    times = nc.variables["time"][:]
    ntimes = len(times)
    for it in range(ntimes):
        m = Basemap(projection='stere', lat_0=90, lon_0=160, llcrnrlon=-230,
            llcrnrlat=44, urcrnrlon=-65, urcrnrlat=40, resolution='h')
        fig = plt.figure(figsize=(8,9))

        m.drawcoastlines()
        m.drawmapboundary(fill_color='#99ffff')
        m.fillcontinents(color='0.3',lake_color='0.3')
#   m.fillcontinents(color='coral',lake_color='aqua')
        aice = nc.variables["sispeed"][it,:,:]
        cs = m.contourf(x, y, aice, levels=levels, cmap=cmap, extend='both')
        parallels = np.arange(45.,90,15.)
        # labels = [left,right,top,bottom]
        m.drawparallels(parallels)
        meridians = np.arange(0.,360.,15.)
        m.drawmeridians(meridians,labels=[1, 0, 0, 1])
#   csa = m.contour(x, y, aice, levels=levels, linewidths=(1,), colors='k')
#   csa = m.contour(x, y, aice, levels=levels, colors=('k',))

        myday = jday2date(times[it]/24.)
        date_tag = myday.strftime('%d %B %Y')
        plt.title(date_tag, fontsize=20)
        fname = myday.strftime('movie_ispeed/frame_%(number)04d.png'%{'number': it})
        print(date_tag)
        cbar = plt.colorbar(cs, orientation='vertical')
        cbar.ax.tick_params(labelsize=15)

        plt.savefig(fname)
        plt.close()

    nc.close()
