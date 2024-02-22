from machine import Pin
button = Pin(15, Pin.IN, Pin.PULL_DOWN)

def readbutton():
        if button.value() == 1:
            button_state = 1
            print("Button on")
        else:
            button_state = 0
            print("Button off")
        return button_state
