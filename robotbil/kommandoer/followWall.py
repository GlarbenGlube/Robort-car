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
    leftspeed = 0
    rightspeed = 0

    counter = 0
    # Sets the speed of the motors
    ms.UpdatePWM(0.4, 0.4)

    # Prints "start" message
    print("start")

    # Measures the distance from the wall

    # Checks if button is pressed
    while pob.readbutton() != 1:
        dis = RS.measureDistance()
        #while within distance limits it drives forward
        while dis <= 60 and dis >= 50 and pob.readbutton() != 1:
            ms.forward()
            ms.UpdatePWM(0.4, 0.4)
            ms.VariableSpeed(20, 20)
            dis = RS.measureDistance()
            print("life is a highway")
        #it is no longer within limits. it now checks which limit it broke
        if dis < 50:
            #checks if we have a case of a small bump
            if dis > 20:
                leftspeed = 15
                ms.VariableSpeed(leftspeed,rightspeed)
                ms.forward()
                print("bump")
            #it has met a wall
            else:
                while dis < 50 and pob.readbutton() != 1:
                    # Adjusts the right motor speed based on distance and stops
                    leftspeed = 15
                    rightspeed = 20
                    ms.VariableSpeed(leftspeed,rightspeed)
                    dis = RS.measureDistance()
                    print("wall")
        #it broke limit for far away
        else:
            #is it still within acceptable distances for a bump
            if dis < 75:
                ms.VariableSpeed(20,15)
                ms.forward()
                print("hole")
            #it has dropped off a cliff
            else:
                while dis > 60 and pob.readbutton() != 1:
                    # Adjusts the left motor speed based on distance and stops
                    ms.VariableSpeed(20,15)
                    dis = RS.measureDistance()
                    print("cliff")
    ms.stop()
# tænder sensoren
# læser afstanden
# gør noget afhængig af afstand. hvis den er mindre end grænseværdien drej til venstre og ret op hvis den er større end grænseværdien drej til venstre
# hvis afstanden er endnu højere eller lavere end de 2 grænseværdier. drej hårdere.bb
