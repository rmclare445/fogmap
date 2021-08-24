import board
import neopixel

# Pixel strip configuration
gpio_pin = board.D18
num_pixels = 51

# Max brightness
b = 127

pixels = neopixel.NeoPixel( gpio_pin, num_pixels )

def pixel_sun( suns ):
    for i, sun in enumerate(suns):
        if sun == True:
            pixels[i] = (40, 40, 10)
        elif sun == False:
            pixels[i] = (0, 0, 15)
        else:
            pixels[i] = (0, 0, 0)

def pixel_I_frac( I_fracs ):
    for i, I_frac in enumerate(I_fracs):
        In = max(min(I_frac, 1.0), 0.01)
        pixels[i] = ( int(b*I_frac), 0, int(b-b*I_frac))

def pixel_I_tot( I_tots ):
    for i, I_tot in enumerate(I_tots):
        In = max(min(I_tot, 1.0), 0.01)
        pixels[i] = (int(b*0.65*In), int(b*In), 0)

def pixel_clear( ):
    pixels.fill( (0, 0, 0) )
