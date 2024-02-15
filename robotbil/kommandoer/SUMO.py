#skal kunne følge en varierende væg og dreje så bilen kan følge væggen
#skeletkode
from Hardware import ReadSensor as SA
from Hardware import motorstyrring as ms
from Hardware import Poweroffbutton as pob
from time import sleep
def SUMO():
    gulv = 0
    while pob.button() != "ON":
        while SA.measureDistance > 100:
            if pob.button() == "ON":
                break
            else:
                ms.turnleft()
        while SA.measureQA() < 60000:
            if pob.button() == "ON":
                break
            else:
                ms.forward()
        ms.stop()
        ms.turnleft()