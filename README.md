Arctic6 is a pan-arctic domain, covering a larger extent than my previous Arctic grids. These are some of the files needed to run it with MOM6-SIS2.

The hindcast directory contains files for a typical long hindcast.

check_mask is from: https://github.com/NOAA-GFDL/FRE-NCtools

check_mask --grid_file INPUT/ocean_mosaic.nc --ocean_topog INPUT/ocean_topog.nc --min_pe 300 --max_pe 400 --halo 4 --model ocean

The idealized\_0 directory contains files for an idealized unforced spin-up.
