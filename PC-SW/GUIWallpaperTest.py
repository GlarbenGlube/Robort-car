# import PySimpleGUI as sg

# layout = [[sg.Image(filename='C:\\Users\\Rasmus\\Pictures\\Bin-Chillin.png', key='-IMAGE-')],
#           [sg.Button('Click Me')]]

# window = sg.Window('Window Title', layout, margins=(0, 0)).Finalize()
# window['-IMAGE-'].update(filename='C:\\Users\\Rasmus\\Pictures\\Bin-Chillin.png')  # To update the background if needed

# while True:
#     event, values = window.read()
#     if event == sg.WIN_CLOSED:
#         break

# window.close()

import PySimpleGUI as sg

# Layout for buttons that will float over the image
buttons_layout = [
    [sg.Button('Button 1')],
    [sg.Button('Button 2')]
]

# Main layout of the window, with an image in the background and buttons on top
layout = [
    [sg.Column([[sg.Image('C:\\Users\\Rasmus\\Pictures\\Bin-Chillin.png')]], key='-IMAGE-COL-', pad=(0, 0))],
    [sg.Column(buttons_layout, pad=(0, 0), key='-BUTTONS-COL-')]
]

# Create the window
window = sg.Window('Window with Background Image', layout, finalize=True)

# Position the buttons column over the image column
window['-BUTTONS-COL-'].Widget.place(relx=0.5, rely=0.5, anchor='center')

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

window.close()