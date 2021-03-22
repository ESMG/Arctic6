from subprocess import call
import numpy as np
import xarray
import sys

data = np.zeros((1392,1080))
data[-1,:] = 1.e-5
field = xarray.Dataset({'rate': (['ny', 'nx'], data)})

# Choose where to save the results from this script
output_file = 'INPUT/ice_outflow.nc'

# Save file, making sure that time is the unlimited dimension.
compress = True
if compress:
   fileformat, zlib, complevel, area_dtype = 'NETCDF4', True, 1, 'f4'
else:
   fileformat, zlib, complevel, area_dtype = 'NETCDF3_64BIT_OFFSET', None, None, 'd'

comp = dict(zlib=zlib, complevel=complevel)
encoding = {var: comp for var in field.data_vars}
field.to_netcdf(
    output_file,
    format=fileformat,
    encoding=encoding
)

# Delete the _FillValue attribute.
# MOM will crash if this attribute is present.
# I can't find how to get xarray to not write it.
# Need to have NCO in your path or module load nco before running this script.
# Get rid of all of them:
#call(f'ncatted -h -O -a _FillValue,,d,, {output_file}', shell=True)
