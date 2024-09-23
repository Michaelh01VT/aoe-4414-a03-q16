# sez_to_ecef.py
#
# Usage: python3 sez_to_ecef.py o_lat_deg o_lon_deg o_hae_km s_km e_km z_km
# Converts SEZ coordinates to ECEF Coordinates
# Parameters:
# o_lat_deg: Observer's geodetic latitude in degrees
# o_lon_deg: Observer's geodetic longitude in degrees
# o_hae_km: Observer's height above the ellipsoid (HAE) in kilometers
# s_km: SEZ South coordinate in kilometers
# e_km: SEZ East coordinate in kilometers
# z_km: SEZ Zenith coordinate in kilometers
# 
# Output:
# Prints resulting ECEF coordinates in kilometers
#
# Written by Michael Hoffman
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.
# import Python modules
# e.g., import math # math module
import sys # argv
# "constants"
# e.g., R_E_KM = 6378.137
# helper functions
## function description
# def calc_something(param1, param2):
# pass
# initialize script arguments
# arg1 = '' # description of argument 1
# arg2 = '' # description of argument 2
# parse script arguments
# if len(sys.argv)==3:
# arg1 = sys.argv[1]
# arg2 = sys.argv[2]
# ...
# else:
# print(\
# 'Usage: '\
# 'python3 arg1 arg2 ...'\
# )
# exit()
# write script below this line
import math

# Earth radius
R_E_KM = 6378.137

# Helper function to convert degrees to radians
def deg_to_rad(deg):
    return deg * math.pi / 180.0

# Parse script arguments
if len(sys.argv) != 7:
    print('Usage: python3 sez_to_ecef.py o_lat_deg o_lon_deg o_hae_km s_km e_km z_km')
    sys.exit()

o_lat_deg = float(sys.argv[1])  # Observer's lat in deg
o_lon_deg = float(sys.argv[2])  # Observer's long in deg
o_hae_km = float(sys.argv[3])   # Observer's hae in km
s_km = float(sys.argv[4])       # SEZ S coordinate in km
e_km = float(sys.argv[5])       # SEZ E coordinate in km
z_km = float(sys.argv[6])       # SEZ Z coordinate in km

# Observer lat and long from deg to rad
lat_rad = deg_to_rad(o_lat_deg)
lon_rad = deg_to_rad(o_lon_deg)

# Compute ECEF coordinates 
ecef_x_km = (math.cos(lon_rad) * math.sin(lat_rad) * s_km + 
             math.cos(lon_rad) * math.cos(lat_rad) * z_km - 
             math.sin(lon_rad) * e_km)

ecef_y_km = (math.sin(lon_rad) * math.sin(lat_rad) * s_km + 
             math.sin(lon_rad) * math.cos(lat_rad) * z_km + 
             math.cos(lon_rad) * e_km)

ecef_z_km = (-math.cos(lat_rad) * s_km + math.sin(lat_rad) * z_km)

# Output ECEF coordinates
print(ecef_x_km)
print(ecef_y_km)
print(ecef_z_km)
