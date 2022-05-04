import subprocess
import os.path
import netCDF4

num = input("Restart number? ")
file_path = "$AKDRIVE/Arctic_12k/run01/restart_" + num
if os.path.exists(file_path):
    print("directory exists already:", file_path)
    exit()
else:
    cmd = "mkdir " + file_path
    subprocess.call([cmd], shell=True)

cmd = "cp RESTART/* " + file_path
subprocess.call([cmd], shell=True)
cmd = "mv RESTART/* INPUT"
subprocess.call([cmd], shell=True)
#vi ocean_arctic4.in
#mv 201*.nc $AKDRIVE/Arctic_12k/run01
