#skal kunne følge en varierende væg og dreje så bilen kan følge væggen
#skeletkode
#frontalvæg
#væg der forsvinder i siden
from Hardware import ReadSensor as RS
from Hardware import motorstyrring as ms
from Hardware import Poweroffbutton as pob
import math
from time import sleep

def follow():
    while pob.button() != 1:
        # how far from wall
        distance = RS.measureDistance()
        if 200 > distance > 100:
            ms.VariableSpeed(25,20)
        elif distance >= 200:
            ms.VariableSpeed(35,20)
        else:
            left,right = custom_transform(distance)
            print(f"{left} {right}")
            ms.VariableSpeed(left*0.4,right*0.4)
    ms.stop()

def custom_transform(x):
    # Implementing the sigmoid function using the math library for exp
    sigmoid = 1 / (1 + math.exp(-(x - 50) / 11))
    
    # Scale the sigmoid output to fit the desired output range
    y1 = sigmoid * 100
    
    # Calculate the second output as the complement to 100
    y2 = 100 - y1
    
    return y1, y2




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
                leftspeed = 25
                rightspeed = 50
                ms.VariableSpeed(leftspeed,rightspeed)
                print("bump")
            #it has met a wall
            else:
                count = 0
                while dis < 45 and pob.readbutton() != 1:
                    # Adjusts the right motor speed based on distance and stops
                    if dis > 30:
                        leftspeed = 0
                        rightspeed = 35
                        ms.VariableSpeed(leftspeed,rightspeed)
                        dis = RS.measureDistance()
                    else:
                        if count == 0:
                            leftspeed = -30
                            rightspeed = -30
                            ms.VariableSpeed(leftspeed,rightspeed)
                            sleep(0.2)
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
            count = 30
            while dis > 65 and pob.readbutton() != 1:
                # Adjusts the left motor speed based on distance and stops
                count += 0.2
                ms.VariableSpeed(count,25)
                dis = RS.measureDistance()
                print("cliff")
                if count >= 40:
                    count = 40
            ms.stop()
# tænder sensoren
# læser afstanden
# gør noget afhængig af afstand. hvis den er mindre end grænseværdien drej til venstre og ret op hvis den er større end grænseværdien drej til venstre
# hvis afstanden er endnu højere eller lavere end de 2 grænseværdier. drej hårdere.bb
