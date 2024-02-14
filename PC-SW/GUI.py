import PySimpleGUI as sg
import Remote
from Controller import readController as controller

sg.theme('DarkGrey15')

currentPower = 0
batteryLevel = currentPower/100*8.4

commands = {"Follow Wall":"wallfollow","Push Object": "boxpush", 
            "controlOn": "controller", "controlOff": "manual",
            "forwardGo": "forward", "forwardStop": "stop",
            "leftGo": "left", "leftStop": "stop",
            "Stop": "stop",
            "rightGo": "right", "rightStop": "stop",
            "backGo": "backward", "backStop": "stop",
            "Update Battery": "getbattery"
            }

def UpdateBatteryLevel(window, battery_level, current_power):
    window['BATTERY_LEVEL'].update(f'Battery Level: {battery_level}%')
    window['CURRENT_POWER'].update(f'Current Power: {current_power} volts')
    window['PROGRESS_BAR'].update(battery_level)

def GUI():
    layout = [[sg.Button('Follow Wall', size=(12, 2), pad=(10, 50), font='Impact'),
               sg.Button('Push Object', size=(12, 2), pad=(10, 50), font='Impact'),
               sg.Button('Controller', size=(12, 2), pad=(10, 50), font='Impact', key= 'control')],

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

    centering = [[sg.VPush()],
                 [sg.Push(), sg.Column(layout, element_justification='c'), sg.Push()],
                 [sg.VPush()]]

    window = sg.Window('Window Title', centering, size=(1100, 700), finalize=True)

    left = window['left']
    right = window['right']
    forward = window['forward']
    back = window['back']
    control = window['control']

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

    #main lööp
    while True:
        UpdateBatteryLevel(window, batteryLevel, currentPower)
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Quit':
            break
        else:
            if event in commands:
                print(commands[event]) 
                Remote.UDPSend(commands[event])
                if event == 'controlOn':
                    controller()
                elif event == 'Update Battery':
                    print(1)
                    sg.batteryLevel = Remote.UDPRecieve()

    window.close()



GUI()
