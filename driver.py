import time
import days
import solar
from selenium import webdriver


t = time.localtime()

doy = days.day_of_year(t[0], t[1], t[2])
#doy = days.day_of_year(t[0], 4, 15)

print(doy)

t_frac = t[3] + (t[4]/60.)
#t_frac = 12.

I = solar.irradiation(doy, t_frac)

print(I)

#           Asilomar        PG HS         Lovers Pt.    New Monterey   Old Town Mont.  Carmel
stations = ["KCAPACIF126", "KCAPACIF189", "KCAPACIF27", "KCAMONTE133", "KCAMONTE140", "KCACARME142"]

options = webdriver.firefox.options.Options()
options.add_argument('--headless')
driver = webdriver.Firefox(executable_path=r'C:\Users\Ryan\Documents\GitHub\investment-interface\geckodriver.exe', options=options)

for st in stations:
    print(st)
    
    driver.get("https://www.wunderground.com/dashboard/pws/%s" % st)
    
    content = driver.find_element_by_xpath('/html/body/app-root/app-dashboard/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/section[1]/div[1]/div/section/div/div/div/div[10]/div/lib-tile-solar-radiation/div/div[2]/div/div[2]/div/div[2]')
    
    print(content.text)
    
    I_wu = float(content.text[:-8])
    
    print(I_wu)
    
    if I_wu > max(0.7 * I, 350.):
        sun = True
    else:
        sun = False
        
    print("sun = " + str(sun))
















