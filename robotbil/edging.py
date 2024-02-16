from Hardware import motorstyrring as M
from Hardware import ReadSensor as S
from time import sleep

def cbt():
    while True:
        M.UpdatePWM(1200,dutyL=0.4,dutyR=0.4)   
        print("start")
        b = 0
        distance = S.measureDistance() 
        while b < 25:
            distance = S.measureDistance()
            if distance < 110:
                b=31
                if distance < 10:
                    M.turnright()
                    sleep(0.25 - distance/100)
                    M.stop()
                else:
                    M.turnleft()
                    sleep(distance/100)
                    M.stop()
            M.turnright()
            b+=1   
        M.UpdatePWM(1000,dutyL=0.615,dutyR=0.6)   
        reflection = S.measureReflection()
        while reflection <= 40000:
            print(reflection)
            M.forward()
            reflection = S.measureReflection()
        M.back()
        sleep(0.05)
        print("return")
        M.UpdatePWM(1000,dutyL=0.52,dutyR=0.5)   
        M.back()
        sleep(1)
        M.stop()
        M.turnright()
        sleep(0.5)
        M.stop()

cbt()