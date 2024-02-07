#skal kunne give kommando valg til brugeren
#skal kunne modtage et input
#skal kunne oversætte et input til en mode og køre moden
def konsol():
    while True:
        brugerinput = input("""Robotbil terminal
"manuel"
"follow wall"
"SUMO"
Vælg venligst en mode: """)

        programvalg = {"manuel": 1, "follow wall": 2, "SUMO": 3}
        if brugerinput in programvalg:
            print("du har valgt", brugerinput)
            return programvalg.get(brugerinput)

        else:
            print("er du dum eller hva'? er du gris? eller hva?")
konsol()