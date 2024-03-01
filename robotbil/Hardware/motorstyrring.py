from machine import Pin, PWM

# PWM pins for controlling each motor
rightpwm = PWM(Pin(0))
leftpwm = PWM(Pin(1))

# Left motor pins
rightForward = Pin(3, Pin.OUT)
rightBack = Pin(2, Pin.OUT)

# Right motor pins
leftForward = Pin(4, Pin.OUT)
leftBack = Pin(5, Pin.OUT)

# variables to control the speed of the motors
frequency = 1200
dutycycleR = .72
offsetR = 0.15
dutycycleL = .700
offsetL = 0

def UpdateFreq(freqL,freqR):
    print(f"freq L: {freqL} freq R: {freqR}")
    leftpwm.freq(freqL)
    rightpwm.freq(freqR)

# Update the PWM frequency and dutycycles for each motor. 
def UpdatePWM(dutyL, dutyR):
    print(f"L: {dutyL} R: {dutyR}")
    if dutyR != 0:
        rightpwm.duty_u16(int(65536 * dutyR+offsetR))
    if dutyL != 0:
        leftpwm.duty_u16(int(65536 * dutyL+offsetL))


#car go foward
def forward():
    rightForward.value(1)
    leftForward.value(1)
    rightBack.value(0)
    leftBack.value(0)

# adjustable motor speed (left)
# def VariableLeft(speed):
#     if speed <0:
#         dutycycleL = (speed*-1)/100
#         leftForward.value(0)
#         leftBack.value(1)
#     else:
#         dutycycleL = speed/100
#         leftBack.value(0)
#         leftForward.value(1)
#     UpdatePWM(1200,dutyL=dutycycleL)


# # adjustable motor speed (right)
# def VariableRight(speed):
#     if speed <0:
#         dutycycleR = (speed*-1)/100
#         rightForward.value(0)
#         rightBack.value(1)
#     else:
#         dutycycleR = speed/100
#         rightBack.value(0)
#         rightForward.value(1)
#     UpdatePWM(1200,dutyR=dutycycleR)

def VariableSpeed(left, right):
    if left < 0: # left motor update
        dutycycleL = (left*-1)/100
        leftForward.value(0)
        leftBack.value(1)
    elif left > 0:
        dutycycleL = left/100
        leftBack.value(0)
        leftForward.value(1)
    else:
        dutycycleL = 0
        leftBack.value(0)
        leftForward.value(0)

        
    if right <0: # right motor update
        dutycycleR = (right*-1)/100
        rightForward.value(0)
        rightBack.value(1)
    elif right > 0:
        dutycycleR = right/100
        rightBack.value(0)
        rightForward.value(1)
    else:
        dutycycleR = 0
        rightBack.value(0)
        rightForward.value(0)

    UpdatePWM(dutycycleL, dutycycleR)

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