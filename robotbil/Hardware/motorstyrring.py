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

# variables to control the speed of the motors
frequency = 5000
dutycycleR = .7
dutycycleL = .706

# Update the PWM frequency and dutycycles for each motor. 
def UpdatePWM(freq=int, dutyL=float(), dutyR=float()):
    if dutyR != None:
        rightpwm.duty_u16(int(65536 * dutyR))
    if dutyL != None:
        leftpwm.duty_u16(int(65536 * dutyL))
    if freq != None and freq != 0:
        leftpwm.freq(freq)
        rightpwm.freq(freq)

#car go foward
def forward():
    rightForward.value(1)
    leftForward.value(1)
    rightBack.value(0)
    leftBack.value(0)

# adjustable motor speed (left)
def VariableLeft(speed):
    if speed <0:
        dutycycleL = (speed*-1)/100
        leftForward.value(0)
        leftBack.value(1)
    else:
        dutycycleL = speed/100
        leftBack.value(0)
        leftForward.value(1)
    UpdatePWM(1200,dutyL=dutycycleL)


# adjustable motor speed (right)
def VariableRight(speed):
    if speed <0:
        dutycycleR = (speed*-1)/100
        rightForward.value(0)
        rightBack.value(1)
    else:
        dutycycleR = speed/100
        rightBack.value(0)
        rightForward.value(1)
    UpdatePWM(1200,dutyR=dutycycleR)


# car go backwards
def back():
    rightForward.value(0)
    leftForward.value(0)
    rightBack.value(1)
    leftBack.value(1)


# car stops
def stop():
    rightForward.value(0)
    leftForward.value(0)
    rightBack.value(0)
    leftBack.value(0)


# car turns right on the spot
def turnright():
    leftForward.value(1)
    leftBack.value(0)
    rightBack.value(1)
    rightForward.value(0)



# car turns left on the spot
def turnleft():
    leftBack.value(1)
    leftForward.value(0)
    rightBack.value(0)
    rightForward.value(1)