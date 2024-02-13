#skal kunne følge en varierende væg og dreje så bilen kan følge væggen
#skeletkode
from Hardware import ReadSensor as SA
from Hardware import motorstyrring as ms
from time import sleep
def SUMO():
    while True:
        while SA.measureDistance > 100:
            ms.onspotturnleft()
        while refleks == gulv:
            ms.forward()
        ms.stop()
        ms.onspotturnleft()