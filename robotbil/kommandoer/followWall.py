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
    # Checks if button is pressed
    while pob.readbutton != "ON":
        # Sets the speed of the motors
        ms.UpdatePWM(1200, dutyL=0.4, dutyR=0.4)

        # Prints "start" message
        print("start")

        # Measures the distance from the wall
        dis = RS.measureDistance()

        # If the measured distance is greater than 100
        if dis > 100:
            # Measures the distance again
            dis = RS.measureDistance()

            # If the distance is greater than 100 and less than 50
            if dis > 100 and dis < 50:
                # Adjusts the left motor speed based on distance and moves forward
                ms.VariableLeft(RS.measureDistance() * 0.5)
                ms.forward()
                sleep(1)
                ms.stop()
            else:
                # Adjusts the left motor speed based on distance and stops
                ms.VariableLeft(RS.measureDistance() * 0.5)
                sleep(1)
                ms.stop()
        # If the measured distance is less than 100
        else:
            # Measures the distance again
            dis = RS.measureDistance()

            # If the distance is less than 100 and greater than 150
            if dis < 100 and dis > 150:
                # Adjusts the left motor speed based on distance and moves forward
                ms.VariableLeft(RS.measureDistance() * 0.5)
                ms.forward()
                sleep(1)
                ms.stop()
            else:
                # Adjusts the left motor speed based on distance and stops
                ms.VariableLeft(RS.measureDistance() * 0.5)
                sleep(1)
                ms.stop()
# tænder sensoren
# læser afstanden
# gør noget afhængig af afstand. hvis den er mindre end grænseværdien drej til venstre og ret op hvis den er større end grænseværdien drej til venstre
# hvis afstanden er endnu højere eller lavere end de 2 grænseværdier. drej hårdere.
