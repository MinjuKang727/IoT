import spidevRead as sr
import time

try:
    while True :
        readData = sr.analog_read(0)
        print(f'readData : {readData}')
        time.sleep(0.01)
except KeyboardInterrupt :
    gp.cleanup()
