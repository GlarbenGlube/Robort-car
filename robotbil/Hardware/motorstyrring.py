from machine import Pin, PWM

# PWM pins for controlling each motor
leftpwm = PWM(Pin(0))
rightpwm = PWM(Pin(1))

# Left motor pins
rightForward = Pin(3, Pin.OUT)
rightBack = Pin(2, Pin.OUT)

# Right motor pins
leftForward = Pin(4, Pin.OUT)
leftBack = Pin(5, Pin.OUT)

frequency = 5000
dutycycleR = .7
dutycycleL = .706

def UpdatePWM(freq=int(), dutyL=float(), dutyR=float()):
    if dutyR != None:
        rightpwm.duty_u16(int(65536 * dutyR))
    if dutyL != None:
        leftpwm.duty_u16(int(65536 * dutyL))
    if freq != None:
        leftpwm.freq(freq)
        rightpwm.freq(freq)

def forward():
    rightForward.value(1)
    leftForward.value(1)
    rightBack.value(0)
    leftBack.value(0)

def VariableLeft(speed): # has 
    if speed <0:
        dutycycleL = (speed*-1)/100
        rightForward.value(0)
        rightBack.value(1)
    else:
        dutycycleL = speed/100
        rightBack.value(0)
        rightForward.value(1)
    UpdatePWM()

def VariableRight(speed):
    if speed <0:
        dutycycleR = (speed*-1)/100
        rightForward.value(0)
        rightBack.value(1)
    else:
        dutycycleR = speed/100
        rightBack.value(0)
        rightForward.value(1)
    UpdatePWM()
    
def back():
    rightForward.value(0)
    leftForward.value(0)
    rightBack.value(1)
    leftBack.value(1)

def stop():
    rightForward.value(0)
    leftForward.value(0)
    rightBack.value(0)
    leftBack.value(0)

def turnright():
    leftForward.value(1)
    leftBack.value(0)
    rightBack.value(1)
    rightForward.value(0)


def turnleft():
    leftBack.value(1)
    leftForward.value(0)
    rightBack.value(0)
    rightForward.value(1)


