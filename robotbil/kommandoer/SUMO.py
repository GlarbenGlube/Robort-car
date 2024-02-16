#skal kunne følge en varierende væg og dreje så bilen kan følge væggen
#skeletkode
from Hardware import ReadSensor as S
from Hardware import motorstyrring as M
from Hardware import Poweroffbutton as B
from time import sleep
reflectionThreshold = 40000

def SUMO():
    while B.button() != "ON":
        
        dutycycleR = 0.5
        M.UpdatePWM(None, dutycycleR)
        
        while S.measureDistance > 100 and B.button() != "ON":
            M.turnleft()
            sleep(0.5)

        M.UpdatePWM(None, 1)
        
        while S.measureQA() <= reflectionThreshold and B.button() != "ON":
            M.forward()
        
        M.stop()
        M.turnleft()
