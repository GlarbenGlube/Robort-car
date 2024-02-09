import PySimpleGUI as sg
import Remote
commands = {"Follow Wall":"wallfollow","Push Object": "boxpush", "Manual": "manual", "Frem": "forwards", "Venstre": "venstre", "Stop": "stop", "Højre": "right", "Tilbage": "backwards"}
sg.theme('DarkGrey15')

def GUI():
    layout = [[sg.Button('Follow Wall', size=(12, 2), pad=(10, 50), font='Impact'),
               sg.Button('Push Object', size=(12, 2), pad=(10, 50), font='Impact'),
               sg.Button('Manual', size=(12, 2), pad=(10, 50), font='Impact')],

              [sg.Button('Frem', size=(12, 2), pad=(10, 10), font='Impact')],

              [sg.Button('Venstre', size=(12, 2), pad=(10, 10), font='Impact'),
               sg.Button('Stop', size=(12, 2), pad=(10, 10), font='Impact'),
               sg.Button('Højre', size=(12, 2), pad=(10, 10), font='Impact')],

              [sg.Button('Tilbage', size=(12, 2), pad=(10, 10), font='Impact')],

              [sg.Button('Quit', size=(12, 2), pad=(10, 50), font='Impact')]]

    centering = [[sg.VPush()],
                 [sg.Push(), sg.Column(layout, element_justification='c'), sg.Push()],
                 [sg.VPush()]]

    window = sg.Window('Window Title', centering, size=(900, 600))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or 'quit':
            break
        else:
            if event in commands:
                Remote.UDPSend(commands[event])
            

    window.close()

GUI()
