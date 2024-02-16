#skal kunne følge en varierende væg og dreje så bilen kan følge væggen
#skeletkode
from Hardware import ReadSensor as S
from Hardware import motorstyrring as M
from Hardware import Poweroffbutton as B
from time import sleep
reflectionThreshold = 40000

def SUMO():
    i = 0

    while B.button() != "ON":
        
        dutycycleR = 0.5
        M.UpdatePWM(None, dutycycleR)
        o = 0
        while S.measureDistance > 100 and B.button() != "ON":
            i += 1
            M.turnright()
            sleep(0.5)
            if i == 20:
                while S.measureQA() <= reflectionThreshold or o > 5:
                    o += 1
                    forward()

        M.UpdatePWM(None, 1)
        
        while S.measureQA() <= reflectionThreshold and B.button() != "ON":
            M.forward()
        
        M.stop()
        M.turnleft()
