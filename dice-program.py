# Add your Python code here. E.g.
from microbit import *
import random

while True:
    if accelerometer.was_gesture('shake'):
        num=random.randrange(1,6)
        
        if (num==1):
            display.show(Image("00000:"
                        "00000:"
                        "00900:"
                        "00000:"
                        "00000:"))
        elif (num==2):
            display.show(Image("00000:"
                        "09000:"
                        "00000:"
                        "00090:"
                        "00000:"))
        elif (num==3):
            display.show(Image("00000:"
                        "09000:"
                        "00900:"
                        "00090:"
                        "00000:"))
        elif (num==4):
            display.show(Image("00000:"
                        "09090:"
                        "00000:"
                        "09090:"
                        "00000:"))
        elif (num==5):
            display.show(Image("00000:"
                        "09090:"
                        "00900:"
                        "09090:"
                        "00000:"))
        elif (num==6):
            display.show(Image("00000:"
                        "09990:"
                        "00000:"
                        "09990:"
                        "00000:"))
            
