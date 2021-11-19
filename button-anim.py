# Add your Python code here. E.g.
from microbit import *

def anim():             
    display.show(Image('98765:'
                   '56789:'
                   '44444:'
                   '56789:'
                   '98765:'))
    sleep(750)
    display.show(Image('56789:'
                   '98765:'
                   '44444:'
                   '98765:'
                   '56789:'))
    sleep(750)
    display.show(Image('95459:'
                   '86468:'
                   '77477:'
                   '68486:'
                   '59495:'))
    sleep(750)
    display.show(Image('59495:'
                   '68486:'
                   '77477:'
                   '86468:'
                   '95459:'))
    sleep(750)
    display.show(Image('95459:'
                   '59495:'
                   '45954:'
                   '59495:'
                   '95459:'))
    sleep(750)
    
def backwardanim():
    display.show(Image('59495:'
                   '68486:'
                   '77477:'
                   '86468:'
                   '95459:'))
    sleep(750)
    display.show(Image('95459:'
                   '86468:'
                   '77477:'
                   '68486:'
                   '59495:'))
    sleep(750)
    display.show(Image('56789:'
                   '98765:'
                   '44444:'
                   '98765:'
                   '56789:'))
    sleep(750)
    display.show(Image('98765:'
                   '56789:'
                   '44444:'
                   '56789:'
                   '98765:'))
    sleep(750)
    display.show(Image('95459:'
                   '59495:'
                   '45954:'
                   '59495:'
                   '95459:'))
    sleep(750)
    
    
    
while True:
    if button_a.is_pressed() and button_b.is_pressed():
        break   
    
    elif button_a.is_pressed():
        anim()
    
    elif button_b.is_pressed():
        backwardanim()
    
    
display.scroll("bye")