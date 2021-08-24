import time
import solar
import stations
from pixel import *

def update( ):
    # Retrieve current time
    t = time.localtime( )

    # Estimate solar irradiance by time of year
    I = solar.irradiation( t )
    print( I )

    # Don't check after sunset or before sunrise
    if I <= 0:
        pixel_clear( )
        time.sleep(600)
        return

    # Scan through stations and give insolation metrics
    suns, I_fracs, I_tots = stations.station_scan( I )

    # Show quantities on pixels (will need to change for continuous operation)
    pixel_sun(suns)
    time.sleep(5)
    pixel_I_frac(I_fracs)
    time.sleep(5)
    pixel_I_tot(I_tots)
    time.sleep(5)
    pixel_clear( )

if __name__ == "__main__":
    update( )
