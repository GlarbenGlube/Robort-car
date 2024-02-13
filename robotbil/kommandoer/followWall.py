#skal kunne følge en varierende væg og dreje så bilen kan følge væggen
#skeletkode
from Hardware import ReadSensor as RS
from Hardware import motorstyrring as ms
from time import sleep
def follow():
    side = input("what side is the wall on? left or right: ")
    if side == left:
        while True:
            if #readin == stopsignal:
                break
            elif RS.measureDistance() > 100:
                ms.turnleft(RS.measureDistance()*0.5)
                ms.forward()
                sleep(1)
                ms.stop()
    else:
        while True:
            if #readin == stopsignal:
                break
            elif RS.measureDistance() > 100:
                ms.turnright(RS.measureDistance()*0.5)
                ms.forward()
                sleep(1)
                ms.stop()
    pass