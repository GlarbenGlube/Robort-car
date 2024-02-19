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
def SUMO():
    # set initial motor speed and direction
    while True:
        M.UpdatePWM(1200,dutyL=0.4,dutyR=0.4)
        print("start")
        b = 0
        # measures distance to obstacle
        distance = S.measureDistance()
        while b < 25:
            # Continuously measure distance to adjust movement
            distance = S.measureDistance()
            if distance < 110:
                b=31
                if distance < 10:
                    # If obstacle is very close, turn right with a delay proportional to distance
                    M.turnright()
                    sleep(0.25 - distance/100)
                    M.stop()
                else:
                    # If obstacle is near, turn left with a delay proportional to distance
                    M.turnleft()
                    sleep(distance/100)
                    M.stop()
            # Increment counter for number of turns
            M.turnright()
            b+=1
        # Adjust motor speed for obstacle avoidance
        M.UpdatePWM(1000,dutyL=0.615,dutyR=0.6)
        reflection = S.measureReflection()
        # Move forward until an object is detected
        while reflection <= 40000:
            print(reflection)
            M.forward()
            reflection = S.measureReflection()
        # Back off slightly
        M.back()
        sleep(0.05)
        print("return")
        # Adjust motor speed for returning back
        M.UpdatePWM(1000,dutyL=0.52,dutyR=0.5)
        M.back()
        sleep(1)
        M.stop()
        # Turn right before restarting the loop
        M.turnright()
        sleep(0.5)
        M.stop()