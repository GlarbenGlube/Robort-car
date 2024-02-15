#skal kunne følge en varierende væg og dreje så bilen kan følge væggen
#skeletkode
from Hardware import ReadSensor as S
from Hardware import motorstyrring as M
from Hardware import Poweroffbutton as B
from time import sleep
reflectionThreshold = 40000

def SUMO():
    while B.button() != "ON":
        dutycycleL = 100
        M.UpdatePWM()
        while S.measureDistance > 100:
            if B.button() == "ON":
                break
            else:

                M.turnleft()
                sleep(0.5)
        dutycycleL = 200
        M.UpdatePWM()
        while S.measureQA() <= reflectionThreshold:
            if B.button() == "ON":
                break
            else:
                M.forward()
        M.stop()
        M.turnleft()
