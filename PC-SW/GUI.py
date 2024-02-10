import PySimpleGUI as sg
import Remote
from Controller import readController as controller

commands = {"Follow Wall":"wallfollow","Push Object": "boxpush", 
            "controlOn": "controller", "controlOff": "manual",
            "forwardGo": "forward", "forwardStop": "stop",
            "leftGo": "left", "leftStop": "stop",
            "Stop": "stop",
            "rightGo": "right", "rightStop": "stop",
            "backGo": "backward", "backStop": "stop",
            }
sg.theme('DarkGrey15')

def GUI():
    layout = [[sg.Button('Follow Wall', size=(12, 2), pad=(10, 50), font='Impact'),
               sg.Button('Push Object', size=(12, 2), pad=(10, 50), font='Impact'),
               sg.Button('Controller', size=(12, 2), pad=(10, 50), font='Impact', key= 'control')],

              [sg.Button('Frem', size=(12, 2), pad=(10, 10), font='Impact', key='forward')],

              [sg.Button('Venstre', size=(12, 2), pad=(10, 10), font='Impact', key='left'),
               sg.Button('Stop', size=(12, 2), pad=(10, 10), font='Impact'),
               sg.Button('Højre', size=(12, 2), pad=(10, 10), font='Impact', key='right')],

              [sg.Button('Tilbage', size=(12, 2), pad=(10, 10), font='Impact', key='back')],

              [sg.Button('Quit', size=(12, 2), pad=(10, 50), font='Impact')]]

    centering = [[sg.VPush()],
                 [sg.Push(), sg.Column(layout, element_justification='c'), sg.Push()],
                 [sg.VPush()]]

    window = sg.Window('Window Title', centering, size=(900, 600), finalize=True)
    
    left = window['left']
    right = window['right']
    forward = window['forward']
    back = window['back']
    control = window['control']

    left.bind('<ButtonPress>', "Go", propagate=False)
    left.bind('<ButtonRelease>', "Stop", propagate=False)

    right.bind('<ButtonPress>', "Go", propagate=False)
    right.bind('<ButtonRelease>', "Stop", propagate=False)
    
    forward.bind('<ButtonPress>', "Go", propagate=False)
    forward.bind('<ButtonRelease>', "Stop", propagate=False)

    back.bind('<ButtonPress>', "Go", propagate=False)
    back.bind('<ButtonRelease>', "Stop", propagate=False)

    control.bind('<ButtonPress>', "On", propagate=False)
    control.bind('<ButtonRelease>', "Off", propagate=False)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Quit':
            break
        else:
            if event in commands:
                print(commands[event])
                Remote.UDPSend(commands[event])
                if event == 'controlOn':
                    controller()
    window.close()

GUI()
