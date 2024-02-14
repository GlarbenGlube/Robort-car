#skal kunne følge en varierende væg og dreje så bilen kan følge væggen
#skeletkode
import robotbil.Hardware.ReadSensor as RS
import robotbil.Hardware.motorstyrring as ms
import robotbil.Hardware.Poweroffbutton as pob
from time import sleep
def follow():
    #side = input("what side is the wall on? left or right: ")
    """if side == "left":
        while True:
            if pob.readbutton == "ON":
                break
            elif RS.measureDistance() > 100:
                ms.VariableLeft(RS.measureDistance()*0.5)
                ms.forward()
                sleep(1)
                ms.stop()
    else:"""
    while pob.readbutton != "ON":
        while RS.measureDistance() > 100:
            if pob.readbutton == "ON":
                break
            else:
                ms.VariableRight(RS.measureDistance()*0.5)
                ms.forward()
                sleep(1)
                ms.stop()
    pass