from Hardware import motorstyrring as M
from Hardware import ReadSensor as S
from time import sleep

def cbt():
    while True:
        if S.measureReflection() <= 40000:
            M.forward()
        else:
            M.back()
            sleep(1)
            M.stop()
            M.turnright()
            sleep(0.5)
            M.stop()