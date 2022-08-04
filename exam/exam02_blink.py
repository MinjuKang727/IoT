import RPi.GPIO as gp
import time

gp.setmode(gp.BCM) #header index : NAME
# 다른 방법으로 pinMode() 설정하기(Pin# 번호를 이용하기)
# gp.setmode(go.BOARD) # header index : PIN#
gp.setup(18, gp.OUT)
try :
    while True :
        gp.output(18, gp.HIGH) # gp.output(18,1)
        time.sleep(1) # 단위 : 초
        gp.output(18, gp.LOW)
        time.sleep(1)
except KeyboardInterrupt : # Ctrl+C 누르면 예외 처리
    gp.cleanup()
    