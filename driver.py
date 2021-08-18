import time
import solar
import stations
from selenium import webdriver

# Retrieve current time
t = time.localtime( )

# Calculate which day of the year from y/m/d
n = solar.day_of_year( t[0], t[1], t[2] )
#n = solar.day_of_year( t[0], 4, 15 )
print( n )
print( t[3], ":", (t[4]/60.) )

# Estimate solar irradiance by time of year
I = solar.irradiation( n, t )
print( I )

try:
    # Set up browser connection
    options = webdriver.firefox.options.Options( )
    options.add_argument( '--headless' )
    driver = webdriver.Firefox(executable_path=r'C:\Users\Ryan\Documents\GitHub\investment-interface\geckodriver.exe', options=options)
    
    # Scan through stations and give insolation metrics
    stations.station_scan( driver, I )
except:
    pass