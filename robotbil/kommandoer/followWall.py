#skal kunne følge en varierende væg og dreje så bilen kan følge væggen
#skeletkode
#frontalvæg
#væg der forsvinder i siden
from Hardware import ReadSensor as RS
from Hardware import motorstyrring as ms
from Hardware import Poweroffbutton as pob
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
    else:
    while pob.readbutton != "ON":
        while RS.measureDistance() > 100 and pob.readbutton != "ON":
                ms.VariableRight(RS.measureDistance()*0.5)
                ms.forward()
                sleep(1)
                ms.stop()
    pass
"""
def followwall():
    while pob.readbutton != "ON":
        ms.UpdatePWM(1200,dutyL=0.4,dutyR=0.4)
        print("start")
        dis = RS.measureDistance()
        if dis > 100:
            dis = RS.measureDistance()
            if dis > 100 and dis < 50:
                ms.VariableLeft(RS.measureDistance() * 0.5)
                ms.forward()
                sleep(1)
                ms.stop()
            else:
                ms.VariableLeft(RS.measureDistance() * 0.5)
                sleep(1)
                ms.stop()
        else:
            dis = RS.measureDistance()
            if dis < 100 and dis > 150:
                ms.VariableLeft(RS.measureDistance() * 0.5)
                ms.forward()
                sleep(1)
                ms.stop()
            else:
                ms.VariableLeft(RS.measureDistance() * 0.5)
                sleep(1)
                ms.stop()
# tænder sensoren
# læser afstanden
# gør noget afhængig af afstand. hvis den er mindre end grænseværdien drej til venstre og ret op hvis den er større end grænseværdien drej til venstre
# hvis afstanden er endnu højere eller lavere end de 2 grænseværdier. drej hårdere.
