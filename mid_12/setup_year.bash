fyear=1993
echo "Model year = $fyear"
cd ./INPUT
ln -sf /center1/AKWATERS/kshedstrom/JRA_padded/JRA55DO_1.5_Pair_${fyear}.nc JRA_psl.nc
ln -sf /center1/AKWATERS/kshedstrom/JRA_padded/JRA55DO_1.5_Tair_${fyear}.nc JRA_tas.nc
ln -sf /center1/AKWATERS/kshedstrom/JRA_padded/JRA55DO_1.5_Qair_${fyear}.nc JRA_huss.nc
ln -sf /center1/AKWATERS/kshedstrom/JRA_padded/JRA55DO_1.5_Uwind_${fyear}.nc JRA_uas.nc
ln -sf /center1/AKWATERS/kshedstrom/JRA_padded/JRA55DO_1.5_Vwind_${fyear}.nc JRA_vas.nc
ln -sf /center1/AKWATERS/kshedstrom/JRA_padded/JRA55DO_1.5_lwrad_down_${fyear}.nc JRA_rlds.nc
ln -sf /center1/AKWATERS/kshedstrom/JRA_padded/JRA55DO_1.5_swrad_${fyear}.nc JRA_rsds.nc
ln -sf /center1/AKWATERS/kshedstrom/JRA_padded/JRA55DO_1.5_rain_${fyear}.nc JRA_prra.nc
ln -sf /center1/AKWATERS/kshedstrom/JRA_padded/JRA55DO_1.5_snow_${fyear}.nc JRA_prsn.nc

ln -sf  /import/c1/AKWATERS/kate/ESMG/ESMG-configs/Arctic6/mid_12/INPUT/obc/${fyear}/salt_001.nc .
ln -sf  /import/c1/AKWATERS/kate/ESMG/ESMG-configs/Arctic6/mid_12/INPUT/obc/${fyear}/salt_002.nc .
ln -sf  /import/c1/AKWATERS/kate/ESMG/ESMG-configs/Arctic6/mid_12/INPUT/obc/${fyear}/salt_003.nc .
ln -sf  /import/c1/AKWATERS/kate/ESMG/ESMG-configs/Arctic6/mid_12/INPUT/obc/${fyear}/salt_004.nc .
ln -sf  /import/c1/AKWATERS/kate/ESMG/ESMG-configs/Arctic6/mid_12/INPUT/obc/${fyear}/temp_001.nc .
ln -sf  /import/c1/AKWATERS/kate/ESMG/ESMG-configs/Arctic6/mid_12/INPUT/obc/${fyear}/temp_002.nc .
ln -sf  /import/c1/AKWATERS/kate/ESMG/ESMG-configs/Arctic6/mid_12/INPUT/obc/${fyear}/temp_003.nc .
ln -sf  /import/c1/AKWATERS/kate/ESMG/ESMG-configs/Arctic6/mid_12/INPUT/obc/${fyear}/temp_004.nc .
ln -sf  /import/c1/AKWATERS/kate/ESMG/ESMG-configs/Arctic6/mid_12/INPUT/obc/${fyear}/zeta_001.nc .
ln -sf  /import/c1/AKWATERS/kate/ESMG/ESMG-configs/Arctic6/mid_12/INPUT/obc/${fyear}/zeta_002.nc .
ln -sf  /import/c1/AKWATERS/kate/ESMG/ESMG-configs/Arctic6/mid_12/INPUT/obc/${fyear}/zeta_003.nc .
ln -sf  /import/c1/AKWATERS/kate/ESMG/ESMG-configs/Arctic6/mid_12/INPUT/obc/${fyear}/zeta_004.nc .
ln -sf  /import/c1/AKWATERS/kate/ESMG/ESMG-configs/Arctic6/mid_12/INPUT/obc/${fyear}/uv_001.nc .
ln -sf  /import/c1/AKWATERS/kate/ESMG/ESMG-configs/Arctic6/mid_12/INPUT/obc/${fyear}/uv_002.nc .
ln -sf  /import/c1/AKWATERS/kate/ESMG/ESMG-configs/Arctic6/mid_12/INPUT/obc/${fyear}/uv_003.nc .
ln -sf  /import/c1/AKWATERS/kate/ESMG/ESMG-configs/Arctic6/mid_12/INPUT/obc/${fyear}/uv_004.nc .
ln -sf /import/c1/AKWATERS/kate/ESMG/ESMG-configs/Arctic6/mid_12/INPUT/runoff/glofas_hill_${fyear}_v4.1.nc glofas_runoff.nc
