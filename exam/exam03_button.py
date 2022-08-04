import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)
gp.setup(18, gp.OUT)
gp.setup(21, gp.IN)

try :
    while True :
        btn = gp.input(21)
        print(f'btn : {btn}')
        if btn == 1:
            gp.output(18,gp.HIGH)
        else :
            gp.output(18, gp.LOW)
        time.sleep(0.01)
except KeyboardInterrupt :
    gp.cleanup()