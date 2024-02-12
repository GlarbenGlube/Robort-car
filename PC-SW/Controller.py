import pygame
from Remote import send_coordinates

def readController():
    # Initialize pygame
    pygame.init()

    # Initialize the joystick
    pygame.joystick.init()

    try:
        # Attempt to setup the joystick
        joystick = pygame.joystick.Joystick(0)  # Assumes only one joystick is connected
        joystick.init()
        print(f"Initialized joystick: {joystick.get_name()}")
    except pygame.error:
        print("Failed to initialize the joystick")
        return

    # Main loop to read inputs
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN and event.button == 7:
                running = False
            elif event.type == pygame.JOYAXISMOTION:
                print(f"Joystick axis motion. Axis: {event.axis}, Value: {event.value}")
                y = round(event.value*100)
                if  y <= -10 or y >= 10:
                    send_coordinates(event.axis, y)
                elif (-10 < y < -5) or (5<y<10):
                    send_coordinates(event.axis, 0)

                
            
        # Other controller actions/buttons
            # elif event.type == pygame.JOYBUTTONDOWN:
            #     print(f"Joystick button pressed. Button: {event.button}")
            # elif event.type == pygame.JOYBUTTONUP:
            #     print(f"Joystick button released. Button: {event.button}")
            # elif event.type == pygame.JOYHATMOTION:
            #     print(f"Joystick hat motion. Hat: {event.hat}, Value: {event.value}")


    # Quit pygame
    pygame.quit()