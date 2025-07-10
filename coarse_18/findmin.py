import numpy as np
import netCDF4
import sys

ncfile = sys.argv[1]
nc = netCDF4.Dataset(ncfile, 'r')

v = nc.variables['vice'][70,:,:]

dims = v.shape

#vmin = v[0,0,0]
#imin = 0
#jmin = 0
#kmin = 0
#for k in range(dims[0]):
#  for j in range(dims[1]):
#    for i in range(dims[2]):
#      if (v[k,j,i] < vmin):
#        vmin = v[k,j,i]
#        imin = i
#        jmin = j
#        kmin = k
#
#print(imin, jmin, kmin, vmin)
#
#vmax = v[0,0,0]
#imax = 0
#jmax = 0
#kmax = 0
#for k in range(dims[0]):
#  for j in range(dims[1]):
#    for i in range(dims[2]):
#      if (v[k,j,i] > vmax):
#        vmax = v[k,j,i]
#        imax = i
#        jmax = j
#        kmax = k
#
#print(imax, jmax, kmax, vmax)

vmin = v[2,400]
imin = 0
jmin = 0
for j in range(dims[0]):
  for i in range(dims[1]):
    if (not np.isnan(v[j,i]) and v[j,i] < vmin):
      vmin = v[j,i]
      imin = i
      jmin = j

print(imin, jmin, vmin)

vmax = v[2,400]
imax = 0
jmax = 0
for j in range(dims[0]):
  for i in range(dims[1]):
    if (not np.isnan(v[j,i]) and v[j,i] > vmax):
      vmax = v[j,i]
      imax = i
      jmax = j

print(imax, jmax, vmax)
