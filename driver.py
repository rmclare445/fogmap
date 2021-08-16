import time
import days
import solar
import stations
from selenium import webdriver

# Retrieve current time
t = time.localtime()

# Calculate which day of the year from y/m/d
doy = days.day_of_year(t[0], t[1], t[2])
#doy = days.day_of_year(t[0], 4, 15)
print(doy)
print(t[3], ":", (t[4]/60.))

# Estimate solar irradiance by time of year
I = solar.irradiation(doy, t)
print(I)

# Set up browser connection
options = webdriver.firefox.options.Options()
options.add_argument('--headless')
driver = webdriver.Firefox(executable_path=r'C:\Users\Ryan\Documents\GitHub\investment-interface\geckodriver.exe', options=options)

# Scan through stations and give insolation metrics
stations.station_scan( driver, I )