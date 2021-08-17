import read_nl as nl

# Xpath to solar radiation on Weather Underground station dashboard page
sol_rad_xpath = '/html/body/app-root/app-dashboard/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/section[1]/div[1]/div/section/div/div/div/div[10]/div/lib-tile-solar-radiation/div/div[2]/div/div[2]/div/div[2]'

def station_scan( driver, I ):
    
    # Read namelist, get 'stations'
    stations = nl.read_nl( )['stations']
    
    # Cycle thru stations, access dashboards, get solar radiation
    for st in stations:
        print( st )
        
        # Retrieve webpage
        driver.get( "https://www.wunderground.com/dashboard/pws/%s" % st )
        
        # Retrieve solar radiation quantity
        content = driver.find_element_by_xpath( sol_rad_xpath )
        print( content.text )
        I_wu = float( content.text[:-8] )
        print( I_wu )
        
        # Crude estimate of whether the sun is out
        if I_wu > max( 0.7 * I, 250. ):
            sun = True
        else:
            sun = False
        
        # Insolation as a fraction of clear day estimate at time t
        I_frac = I_wu / I
        # Insolation as a fraction of a consistent total
        I_tot  = I_wu / 900.
            
        print( "sun = "    + str(sun) )
        print( "I_frac = " + str(I_frac) )
        print( "I_tot  = " + str(I_tot) )