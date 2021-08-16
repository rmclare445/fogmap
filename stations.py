import yaml

sol_rad_xpath = '/html/body/app-root/app-dashboard/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/section[1]/div[1]/div/section/div/div/div/div[10]/div/lib-tile-solar-radiation/div/div[2]/div/div[2]/div/div[2]'

def station_scan( driver, I ):
    
    stream = open( "namelist.yaml", 'r' )
    dictionary = yaml.safe_load( stream )
    stations = dictionary['stations']
    
    for st in stations:
        print( st )
    
        driver.get( "https://www.wunderground.com/dashboard/pws/%s" % st )
        
        # Retrieve solar radiation quantity
        content = driver.find_element_by_xpath( sol_rad_xpath )
        print( content.text )
        I_wu = float( content.text[:-8] )
        print( I_wu )
        
        if I_wu > max( 0.7 * I, 300. ):
            sun = True
        else:
            sun = False
        
        I_frac = I_wu / I
        I_tot  = I_wu / 900.
            
        print( "sun = "    + str(sun) )
        print( "I_frac = " + str(I_frac) )
        print( "I_tot  = " + str(I_tot) )