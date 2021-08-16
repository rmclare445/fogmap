import time
import days
import solar
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

#           Asilomar        PG HS         Lovers Pt.    New Monterey   Old Town Mont.  Carmel
stations = ["KCAPACIF126", "KCAPACIF189", "KCAPACIF27", "KCAMONTE133", "KCAMONTE140", "KCACARME142"]

# Set up browser connection
options = webdriver.firefox.options.Options()
options.add_argument('--headless')
driver = webdriver.Firefox(executable_path=r'C:\Users\Ryan\Documents\GitHub\investment-interface\geckodriver.exe', options=options)

for st in stations:
    print(st)
    
    driver.get("https://www.wunderground.com/dashboard/pws/%s" % st)
    
    # Retrieve solar radiation quantity
    content = driver.find_element_by_xpath('/html/body/app-root/app-dashboard/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/section[1]/div[1]/div/section/div/div/div/div[10]/div/lib-tile-solar-radiation/div/div[2]/div/div[2]/div/div[2]')
    print(content.text)
    I_wu = float(content.text[:-8])
    print(I_wu)
    
    ## Should make two modes, one which checks insolation as a fraction of forecast
    ##  and one which just adheres to a hard cutoff
    if I_wu > max(0.7 * I, 300.):
        sun = True
    else:
        sun = False
    
    I_frac = I_wu / I
    I_tot  = I_wu / 900.
        
    print("sun = " + str(sun))
    print("I_frac = " + str(I_frac))
    print("I_tot  = " + str(I_tot))



