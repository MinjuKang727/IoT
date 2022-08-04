import picamera as pc
import time

camera = pc.PiCamera() # PiCamera 클래스 객체 생성
camera.start_preview()
time.sleep(5)

for i in range(3) :
    camera.capture(f'../images/image{i}.jpg')
    time.sleep(1)

camera.stop_preview()

camera.close() # 카메라 해제