from pixel import *
import read_nl as nl
from urllib.request import Request, urlopen

# Header definitions for urllib Request
web_headers = {'User-Agent': 'Mozilla/5.0'}

def station_scan( I ):
    # Get data and calculate insolation metrics
    
    # Read namelist, get 'stations'
    stations = nl.read_nl( )['stations']
    
    # Cycle thru stations, access dashboards, get solar radiation
    for st in stations:
        print( st )
        
        try:
            # Retrieve raw webpage bytes
            station_url = "https://www.wunderground.com/dashboard/pws/%s" % st
            req = Request( station_url, headers = web_headers )
            webpage = urlopen( req ).read()
            
            # Get solar radiation data from webpage
            I_wu = get_radiation( webpage )
            print(I_wu)
            
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
            for i in range(len(stations)):
                pixel_sun( i, sun)
            print( "I_frac = " + str(I_frac) )
            print( "I_tot  = " + str(I_tot) )
        
        except:
            print( "Unable to retrieve station data." )
            
def get_radiation( webpage ):
    sol_unit = webpage.find(b"watts/m")
    content = webpage[sol_unit-9:sol_unit].decode()
    return float(content[content.find(">")+1:]) 
    
if __name__ == "__main__":
    station_scan( 900. )
