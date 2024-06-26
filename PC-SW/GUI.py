import PySimpleGUI as sg
import Remote
from Controller import readController as controller
from time import sleep
import os

# ImageDirectory will get the users current path and is used in layout to make sure every user
# can see the images
ImageDirectory = os.getcwd()
print(ImageDirectory)

 # setting the theme for GUI
sg.theme('DarkGrey15')

# Dictionary mapping GUI button texts to corresponding commands
# in other words, it translates the button text into a command the program can execute
commands = {"Follow Wall":"wallfollow", "Push Object": "boxpush",
            "controlOn": "controller", "controlOff": "manual",
            "forwardGo": "forward", "forwardStop": "stop",
            "leftGo": "left", "leftStop": "stop",
            "Stop": "stop",
            "rightGo": "right", "rightStop": "stop",
            "backGo": "backward", "backStop": "stop",
            "Update Battery": "getbattery",
            }

# updates the battery level and current voltage
def UpdateBatteryLevel(window, battery_level, current_power):
    window['BATTERY_LEVEL'].update(f'Battery Level: {battery_level}%')
    window['CURRENT_POWER'].update(f'Current Power: {current_power} volts')
    window['PROGRESS_BAR'].update(battery_level)

# function to create and manage the GUI
def GUI():
    # defining GUI layout, creating buttons with text of a certain size, font, offset and color
    # also includes images using the ImageDirectory variable
    layout = [
            [sg.Button(image_filename=ImageDirectory + '\\PC-SW\\images\\ChinaWall.png', size=(12, 2), pad=(10, 50), button_text='Follow Wall', font='Impact', button_color=('white', 'black')),
            sg.Button(image_filename=ImageDirectory + '\\PC-SW\\images\\CenaSumo.png', size=(12, 2), pad=(10, 50), button_text='Push Object', font='Impact', button_color=('white', 'black')),
            sg.Button(image_filename=ImageDirectory + '\\PC-SW\\images\\ZhongXina.png', size=(12, 2), pad=(10, 50), button_text='Controller', font='Impact', key='control', button_color=('white', 'black'))],

            [sg.Button(image_filename=ImageDirectory + '\\PC-SW\\images\\CenaForward.png', size=(12, 2), pad=(10, 10), button_text='Frem', font='Impact', key='forward', button_color=('white', 'black'))],

            [sg.Button(image_filename=ImageDirectory + '\\PC-SW\\images\\CenaLeft.png', size=(12, 2), pad=(10, 10), button_text='Venstre', font='Impact', key='left', button_color=('white', 'black')),
            sg.Button(image_filename=ImageDirectory + '\\PC-SW\\images\\CenaStop.png', size=(12, 2), pad=(10, 10), button_text='Stop', font='Impact', button_color=('white', 'black')),
            sg.Button(image_filename=ImageDirectory + '\\PC-SW\\images\\CenaRight.png', size=(12, 2), pad=(10, 10), button_text='Højre', font='Impact', key='right', button_color=('white', 'black'))],

            [sg.Button(image_filename=ImageDirectory + '\\PC-SW\\images\\CenaBack.png', size=(12, 2), pad=(10, 10), button_text='Tilbage', font='Impact', key='back', button_color=('white', 'black'))],

            [sg.Button(image_filename=ImageDirectory + '\\PC-SW\\images\\CenaSalute.png', size=(12, 2), pad=(10, 40), button_text='Quit', font='Impact', button_color=('white', 'black')),
            sg.Button(image_filename=ImageDirectory + '\\PC-SW\\images\\BinChillin.png', size=(12, 2), pad=(10, 40), button_text='Update Battery', font='Impact', button_color=('white', 'black'))],

            [sg.Text('Battery Level: ', key='BATTERY_LEVEL')],
            [sg.Text('Current Power: ', key='CURRENT_POWER')],
            [sg.ProgressBar(100, orientation='h', size=(20, 20), key='PROGRESS_BAR')]
            ]

    # centering the GUI elements
    centering = [[sg.VPush()],
                 [sg.Push(), sg.Column(layout, element_justification='c'), sg.Push()],
                 [sg.VPush()]]

    # Creating GUI window
    window = sg.Window('Window Title', centering, size=(1200, 850), finalize=True)

    # retrieving button elements from window
    left = window['left']
    right = window['right']
    forward = window['forward']
    back = window['back']
    control = window['control']

    # Binding button press and release events for directional control
    left.bind('<ButtonPress>', "Go", propagate=True)
    left.bind('<ButtonRelease>', "Stop", propagate=False)

    right.bind('<ButtonPress>', "Go", propagate=True)
    right.bind('<ButtonRelease>', "Stop", propagate=False)
    
    forward.bind('<ButtonPress>', "Go", propagate=True)
    forward.bind('<ButtonRelease>', "Stop", propagate=False)

    back.bind('<ButtonPress>', "Go", propagate=True)
    back.bind('<ButtonRelease>', "Stop", propagate=False)

    control.bind('<ButtonPress>', "On", propagate=True)
    control.bind('<ButtonRelease>', "Off", propagate=False)

    # Main loop for GUI event handling
    while True:
        event, values = window.read()
        # if the X in GUI is pressed then the program will break and shut down
        if event == sg.WIN_CLOSED or event == 'Quit':
            break
        else:
            # handing button events
            if event in commands:
                print(commands[event])   # Printing the corresponding command
                Remote.UDPSend(commands[event])   # sending command via UDP
                if event == 'controlOn':
                    controller()                        # activating controller
                elif event == 'Update Battery':
                    try: 
                        print("recieve")
                        currentPower = float(Remote.UDPRecieve())+0.3  # recieving current power information
                        print("convert")
                        batteryLevel = round((currentPower-6.4)/2*100, 2)   # calculating battery power
                        print("update")
                        UpdateBatteryLevel(window, batteryLevel, round(currentPower,2))      # updating GUI with battery info
                    except: pass
    
    window.close()

GUI()                                                                                                                                                                                                                          

