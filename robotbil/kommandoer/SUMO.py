#skal kunne følge en varierende væg og dreje så bilen kan følge væggen
#skeletkode
from Hardware import ReadSensor as S
from Hardware import motorstyrring as M
from Hardware import Poweroffbutton as B
from time import sleep
def SUMO():
    while B.button() != "ON":
        while S.measureDistance > 100:
            if B.button() == "ON":
                break
            else:
                M.turnleft()
        while S.measureQA() == gulv:
            if B.button() == "ON":
                break
            else:
                M.forward()
        M.stop()
        M.turnleft()