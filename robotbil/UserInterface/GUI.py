import PySimpleGUI as sg

sg.theme('DarkGrey15')

def GUI():
    layout = [[sg.Button('Follow Wall', size=(12, 2), pad=(10, 50), font='Impact'),
                             sg.Button('Push Object', size=(12, 2), pad=(10, 50), font='Impact'),
                             sg.Button('Manuel', size=(12, 2), pad=(10, 50), font='Impact')],

                             [sg.Button('Frem', size=(12, 2), pad=(10,10), font='Impact')],

                              [sg.Button('Venstre', size=(12, 2), pad=(10,10), font='Impact'),
                               sg.Button('Stop', size=(12, 2), pad=(10,10), font='Impact'),
                               sg.Button('Højre', size=(12, 2), pad=(10,10), font='Impact')],

                              [sg.Button('Tilbage', size=(12, 2), pad=(10,10), font='Impact')]]

    centering = [[sg.VPush()],
              [sg.Push(), sg.Column(layout,element_justification='c'), sg.Push()],
              [sg.VPush()]]

    window = sg.Window('Window Title', centering, size=(700,500))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Frem':
            print("frem")
        elif event == 'Højre':
            print("Højre")
        elif event == 'Stop':
            print("stop")
        elif event == 'Venstre':
            print("venstre")
        elif event == 'Tilbage':
            print("tilbage")
        elif event == 'Push Object':
            print("push")
        elif event == 'Follow Wall':
            print("follow wall")
        elif event == 'Manuel':
            print("manuel")

    window.close()
