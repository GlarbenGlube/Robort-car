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
        if dis <= 70 and dis >= 45 and pob.readbutton() != 1:
            ms.forward()
            ms.UpdatePWM(0.4, 0.4)
            ms.VariableSpeed(30, 30)
            dis = RS.measureDistance()
            print("life is a highway")
        #it is no longer within limits. it now checks which limit it broke
        elif dis < 45:
            #checks if we have a case of a small bump
            if dis > 35:
                leftspeed = 20
                rightspeed = 50
                ms.VariableSpeed(leftspeed,rightspeed)
                print("bump")
            #it has met a wall
            else:
                count = 0
                while dis < 50 and pob.readbutton() != 1:
                    # Adjusts the right motor speed based on distance and stops
                    if dis > 30:
                        leftspeed = 0
                        rightspeed = 30
                        ms.VariableSpeed(leftspeed,rightspeed)
                        dis = RS.measureDistance()
                    else:
                        if count == 0:
                            leftspeed = -30
                            rightspeed = -30
                            ms.VariableSpeed(leftspeed,rightspeed)
                            sleep(0.4)
                            count += 1
                        else:
                            leftspeed = -25
                            rightspeed = 25
                            ms.VariableSpeed(leftspeed,rightspeed)
                            dis = RS.measureDistance()
                    print("wall")
                ms.stop()
        #it broke limit for far away
        else:
            #is it still within acceptable distances for a bump
            #if dis < 90:
             #   ms.VariableSpeed(30,25)
              #  ms.forward()
               # print("hole")
            #it has dropped off a cliffæ
            count = 30
            while (dis > 65 or count < 40) and pob.readbutton() != 1:
                # Adjusts the left motor speed based on distance and stops
                count += 0.2
                ms.VariableSpeed(count,25)
                dis = RS.measureDistance()
                print("cliff")
                if count < 50:
                    count = 49
            ms.stop()
# tænder sensoren
# læser afstanden
# gør noget afhængig af afstand. hvis den er mindre end grænseværdien drej til venstre og ret op hvis den er større end grænseværdien drej til venstre
# hvis afstanden er endnu højere eller lavere end de 2 grænseværdier. drej hårdere.bb
