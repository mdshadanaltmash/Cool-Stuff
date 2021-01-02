'''It keep your system awake when you are not available but don't
    want to appear away either. And when you are back just press
    ctrl+c on the terminal.'''

import mouse
import time

while True:
    time.sleep(10)
    mouse.move(0,50,absolute=False,duration=3)
    mouse.move(50,0,absolute=False,duration=3)
    mouse.move(0,-50,absolute=False,duration=3)
    mouse.move(-50,0,absolute=False,duration=3)
