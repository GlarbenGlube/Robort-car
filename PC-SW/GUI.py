import PySimpleGUI as sg
import Remote
from Controller import readController as controller
from time import sleep

sg.theme('DarkGrey15')  # setting the theme for GUI

# Dictionary mapping GUI button texts to corresponding commands
# in other words, it translates the button text into a command the program can execute
commands = {"Follow Wall":"wallfollow","Push Object": "boxpush", 
            "controlOn": "controller", "controlOff": "manual",
            "forwardGo": "forward", "forwardStop": "stop",
            "leftGo": "left", "leftStop": "stop",
            "Stop": "stop",
            "rightGo": "right", "rightStop": "stop",
            "backGo": "backward", "backStop": "stop",
            "Update Battery": "getbattery",
            "Edging": "edging",
            }

# updates the battery level and current voltage
def UpdateBatteryLevel(window, battery_level, current_power):
    window['BATTERY_LEVEL'].update(f'Battery Level: {battery_level}%')
    window['CURRENT_POWER'].update(f'Current Power: {current_power} volts')
    window['PROGRESS_BAR'].update(battery_level)

# function to create and manage the GUI
def GUI():
    # defining GUI layout, creating buttons with text of a certain size, font and offset
    layout = [[sg.Button('Follow Wall', size=(12, 2), pad=(10, 50), font='Impact'),
               sg.Button('Push Object', size=(12, 2), pad=(10, 50), font='Impact'),
               sg.Button('Controller', size=(12, 2), pad=(10, 50), font='Impact', key= 'control'),
               sg.Button('Edging', size=(12, 2), pad=(10, 50), font='Impact')],

              [sg.Button('Frem', size=(12, 2), pad=(10, 10), font='Impact', key='forward')],

              [sg.Button('Venstre', size=(12, 2), pad=(10, 10), font='Impact', key='left'),
               sg.Button('Stop', size=(12, 2), pad=(10, 10), font='Impact'),
               sg.Button('Højre', size=(12, 2), pad=(10, 10), font='Impact', key='right')],

              [sg.Button('Tilbage', size=(12, 2), pad=(10, 10), font='Impact', key='back')],

              [sg.Button('Quit', size=(12, 2), pad=(10, 10), font='Impact'),
               sg.Button('Update Battery', size=(12, 2), pad=(10, 50), font='Impact')],

              [sg.Text('Battery Level: ', key='BATTERY_LEVEL')],
              [sg.Text('Current Power: ', key='CURRENT_POWER')],
              [sg.ProgressBar(100, orientation='h', size=(20, 20), key='PROGRESS_BAR')]
              ]

    # centering the GUI elements
    centering = [[sg.VPush()],
                 [sg.Push(), sg.Column(layout, element_justification='c'), sg.Push()],
                 [sg.VPush()]]

    # Creating GUI window
    window = sg.Window('Window Title', centering, size=(1100, 700), finalize=True)

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
                        currentPower = Remote.UDPRecieve()  # recieving current power information
                        batteryLevel = round((float(currentPower)-6.4)/2*100, 2)   # calculating battery power
                        UpdateBatteryLevel(window, batteryLevel, currentPower)      # updating GUI with battery info
                    except: pass
    
    window.close()

GUI()                                                                                                                                                                                                                          
