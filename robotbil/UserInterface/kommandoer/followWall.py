#skal kunne følge en varierende væg og dreje så bilen kan følge væggen
#skeletkode
from Hardware import ReadSensor as SA
from Hardware import motorstyrring as ms
from time import sleep
def follow():
    side = input("what side is the wall on? left or right: ")
    if side == left:
        while True:
            if #readin == stopsignal:
                break
            elif SA.measureDistance() > 100:
                ms.turnleft(SA.measureDistance()*0.5)
                ms.forward()
                sleep(1)
                ms.stop()
    else:
        while True:
            if #readin == stopsignal:
                break
            elif SA.measureDistance() > 100:
                ms.turnright(SA.measureDistance()*0.5)
                ms.forward()
                sleep(1)
                ms.stop()
    pass