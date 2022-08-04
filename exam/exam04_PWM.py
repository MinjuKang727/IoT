import RPi.GPIO as gp
import time

gp.setmode(gp.BCM) # header index : NAME
gp.setup(18, gp.OUT)

p = gp.PWM(18, 500)
p.start(0)

while True :
     for i in range(0, 10) :
         p.ChangeDutyCycle(i)
         time.sleep(0.03)
     for i in range(100, -1, -1):
         p.ChangeDutyCycle(i)
         time.sleep(0.03)
 except KeyboardInterrupt :
    gp.cleanup()
