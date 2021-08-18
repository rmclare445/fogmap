import time
import solar
import stations
from selenium import webdriver

def update( ):
    # Retrieve current time
    t = time.localtime( )
    
    # Calculate which day of the year from y/m/d
    n = solar.day_of_year( t[0], t[1], t[2] )
    #n = solar.day_of_year( t[0], 4, 15 )
    print( n )
    
    # Estimate solar irradiance by time of year
    I = solar.irradiation( n, t )
    print( I )
    
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