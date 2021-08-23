import time
import solar
import stations

def update( ):
    # Retrieve current time
    t = time.localtime( )
    
    # Estimate solar irradiance by time of year
    I = solar.irradiation( t )
    print( I )
    
    # Don't check after sunset or before sunrise
    if I <= 0.:
        return
    
    # Scan through stations and give insolation metrics
    stations.station_scan( I )


if __name__ == "__main__":
    update( )