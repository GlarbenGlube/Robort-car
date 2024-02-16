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
        M.stop()
        dutycycleR = 0.5
        M.UpdatePWM(None, dutycycleR)
        o = 0
        while S.measureDistance > 100 and B.button() != "ON":
            i += 1
            M.turnright()
            sleep(0.2)
            if i == 20:
                M.stop()
                #den har ikke set noget
                while S.measureQA() <= reflectionThreshold or o > 5:
                    o += 1
                    M.forward()
                    sleep(0.2)

        M.turnleft()
        sleep(0.4)
        M.UpdatePWM(None, 1)
        
        while S.measureQA() <= reflectionThreshold and B.button() != "ON":
            M.forward()
        
        M.stop()
        M.back()
        sleep(0.6)
        M.turnright()
        sleep(0.2)
