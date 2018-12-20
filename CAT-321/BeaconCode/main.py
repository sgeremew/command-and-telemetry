from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light =  True


white = (255,255,255)
yellow = (249,191,0)
green = (0,255,1)
nothing = (0,0,0)


def GmuLogo():
    W = nothing 
    Y = yellow 
    G = green 
    
    logo = [
    W, W, W, W, W, W, W, Y,
    W, W, W, W, W, W, Y, G,
    G, G, W, W, W, W, G, W,
    W, G, G, G, W, G, G, W,
    W, G, W, G, W, G, G, W,
    W, G, W, W, G, W, G, W,
    W, G, W, G, W, W, G, W,
    W, G, W, W, W, W, G, W
    ]
    return logo

def beaconOff():
    n = nothing 

    logo = [
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n

    ]
    return logo



images = [GmuLogo,beaconOff]
count = 0

while True: 
    s.set_pixels(images[count % len(images)]())
    time.sleep(.5)
    count += 1