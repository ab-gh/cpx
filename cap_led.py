#CircuitPlaygroundExpress_CapTouch

import touchio
import board
import time
import neopixel
from digitalio import DigitalInOut, Direction, Pull


pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)
pixels.fill((0,0,0))
pixels.show()
pixels.brightness=1
touch1 = touchio.TouchIn(board.A1)
touch2 = touchio.TouchIn(board.A2)
touch3 = touchio.TouchIn(board.A3)
touch4 = touchio.TouchIn(board.A4)
touch5 = touchio.TouchIn(board.A5)
touch6 = touchio.TouchIn(board.A6)
touch7 = touchio.TouchIn(board.A7)
a1=0
a1step=1
a2=0
a2step=1
a3=0
a3step=1




while True:
    if touch1.value:
        if a1step==1:               # rising
            if a1<128:              # rising
                a1=a1+a1step        # bump
            elif a1==128:           # catch
                a1step=-1           # flip
                a1=128              # bounce
        elif a1step==-1:            # falling
            if a1>0:                # falling
                a1=a1+a1step        # push
            elif a1==0:             # bounce
                a1step=1            # flip
                a1=a1+a1step        # catch
        print("r: ", a1)
    if touch2.value:
        if a2step==1:               # rising
            if a2<128:              # rising
                a2=a2+a2step        # bump
            elif a2==128:           # catch
                a2step=-1           # flip
                a2=128              # bounce
        elif a2step==-1:            # falling
            if a2>0:                # falling
                a2=a2+a2step        # push
            elif a2==0:             # bounce
                a2step=1            # flip
                a2=a2+a2step        # catch
        print("g: ", a2)
    if touch3.value:
        if a3step==1:               # rising
            if a3<128:              # rising
                a3=a3+a3step        # bump
            elif a3==128:           # catch
                a3step=-1           # flip
                a3=128              # bounce
        elif a3step==-1:            # falling
            if a3>0:                # falling
                a3=a3+a3step        # push
            elif a3==0:             # bounce
                a3step=1            # flip
                a3=a3+a3step        # catch
        print("b: ", a3)
    a1, a2, a3 = int(a1), int(a2), int(a3)
    pixels.fill((a1,a2,a3))
    pixels.show()
    time.sleep(0.04)
