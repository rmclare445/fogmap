import board
import neopixel

gpio_pin = board.D18
num_pixels = 51

pixels = neopixel.NeoPixel( gpio_pin, num_pixels )

def pixel_sun( pixnum, value ):
    if value == True:
        pixels[pixnum] = (0, 0, 255)
    else:
        pixels[pixnum] = (255, 0, 150)
        
def pixel_I_frac( pixnum, value ):
    return

def pixel_I_tot( pixnum, value ):
    return
