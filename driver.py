import time
import solar
import stations
from selenium import webdriver

def update( ):
    # Retrieve current time
    t = time.localtime( )
    
    # Estimate solar irradiance by time of year
    I = solar.irradiation( t )
    print( I )
    
    # Don't check after sunset or before sunrise
    if I <= 0.:
        return
    
    try:
        # Set up browser connection
        options = webdriver.firefox.options.Options( )
        options.add_argument( '--headless' )
        driver = webdriver.Firefox(executable_path=r'C:\Users\Ryan\Documents\GitHub\investment-interface\geckodriver.exe',
                                   options=options)
    except:
        print( "Could not open browser connection." )
        return
    
    # Scan through stations and give insolation metrics
    stations.station_scan( driver, I )


if __name__ == "__main__":
    update( )