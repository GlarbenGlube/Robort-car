#skal kunne følge en varierende væg og dreje så bilen kan følge væggen
#skeletkode
from Hardware import ReadSensor as S
from Hardware import motorstyrring as M
from Hardware import Poweroffbutton as B
from time import sleep
reflectionThreshold = 40000
""""
def SUMO():
    i = 0

    while B.button() != "ON":
        M.stop()
        dutycycleR = 0.5
        M.UpdatePWM(None, dutycycleR)
        o = 0
        while S.measureDistance > 100 and B.button() != "ON":
            i += 1
            M.turnright()
            sleep(0.2)
            if i == 20:
                M.stop()
                #den har ikke set noget
                while S.measureQA() <= reflectionThreshold or o > 5:
                    o += 1
                    M.forward()
                    sleep(0.2)

        M.turnleft()
        sleep(0.4)
        M.UpdatePWM(None, 1)
        
        while S.measureQA() <= reflectionThreshold and B.button() != "ON":
            M.forward()
        
        M.stop()
        M.back()
        sleep(0.6)
        M.turnright()
        sleep(0.2)
"""""
def Sumo():
    # set initial motor speed and direction
    while B.readbutton() != 1:
        M.UpdatePWM(0.22,0.22)
        print("start")
        b = 0
        # measures distance to obstacle
        distance = S.measureDistance()
        while b < 15 and B.readbutton != 1:
            # Continuously measure distance to adjust movement
            distance = S.measureDistance()
            if distance < 93:
                b=31
                # If obstacle is far, turn left with a delay proportional to distance
                if distance > 10:
                    M.turnright()
                    sleep(-0.1 + distance/100*.6)
                    M.stop()
                else:
                    M.stop()
            # Increment counter for number of turns
            M.turnleft()
            b+=1
        # Adjust motor speed for obstacle avoidance
        M.UpdatePWM(0.4,0.4)
        reflection = S.measureReflection()
        # Move forward until an object is detected
        while reflection <= reflectionThreshold and B.readbutton() != 1:
            print(reflection)
            M.forward()
            reflection = S.measureReflection()
        # Back off slightly
        M.back()
        sleep(0.05)
        print("return")
        # Adjust motor speed for returning back
        M.UpdatePWM(0.40,0.40)
        M.back()
        sleep(0.50)
        M.stop()
        # Turn left before restarting the loop
        M.UpdatePWM(0.30,0.30)
        M.turnleft()
        sleep(0.3)
        M.stop()