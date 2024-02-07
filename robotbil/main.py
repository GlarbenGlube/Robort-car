from Hardware import motorStyring as motor
from UserInterface import konsol as kons
from UserInterface import kommandoer as komm
from Hardware import SensorAflæsning as SA


def main_robotbil():
    reset = False
    program = kons.konsol()
    if program == 1:
        manuel()
    elif program == 2:
        followWall()
    else:
        SUMO()

    print(program)
    while reset != True:
        pass

while True:
    main_robotbil()

SA.measureDistance()