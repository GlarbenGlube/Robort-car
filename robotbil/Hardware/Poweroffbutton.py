button = Pin(18, Pin.IN, Pin.PULL_DOWN)

def readbutton():
        if button.value() == 1:
            button_state = "ON"
        else:
            button_state = "OFF"
        return button_state
