#skal kunne følge en varierende væg og dreje så bilen kan følge væggen
#skeletkode
import robotbil.Hardware.ReadSensor as SA
import robotbil.Hardware.motorstyrring as ms
import robotbil.Hardware.Poweroffbutton as pob
from time import sleep
def SUMO():
    while pob.button() != "ON":
        while SA.measureDistance > 100:
            if pob.button() == "ON":
                break
            else:
                ms.onspotturnleft()
        while SA.measureQA() == gulv:
            if pob.button() == "ON":
                break
            else:
                ms.forward()
        ms.stop()
        ms.onspotturnleft()