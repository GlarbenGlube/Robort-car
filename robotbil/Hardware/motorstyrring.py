from machine import Pin, PWM
from time import sleep

#venstre motor
rightForward = Pin(3, Pin.OUT)
rightBack = Pin(2, Pin.OUT)

#højre motor
leftForward = Pin(4, Pin.OUT)
leftBack = Pin(5, Pin.OUT)

def init():
    led = Pin(25, Pin.OUT)
    led.toggle()
    frequency = 10000
    dutycycleR = .7
    dutycycleL = .71

    leftpwm = PWM(Pin(0))
    leftpwm.freq(frequency)
    leftpwm.duty_u16(int(65536 * dutycycleL))

    rightpwm = PWM(Pin(1))
    rightpwm.freq(frequency)
    rightpwm.duty_u16(int(65536 * dutycycleR))

def forward():
    rightForward.value(1)
    leftForward.value(1)
    rightBack.value(0)
    leftBack.value(0)

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

# def onspotturnright(grader):
#     rightForward.value(0)
#     leftBack.value(0)
#     leftForward.value(1)
#     rightBack.value(1)
#     sleep(grader)
#     leftForward.value(0)
#     rightBack.value(0)

# def onspotturnleft(grader):
#     leftForward.value(0)
#     rightBack.value(0)
#     rightForward.value(1)
#     leftBack.value(1)
#     sleep(grader)
#     rightForward.value(0)
#     leftBack.value(0)

def turnright():
    leftBack.value(0)
    leftForward.value(1)
    rightBack.value(1)
    rightForward.value(0)


def turnleft():
    leftBack.value(1)
    leftForward.value(0)
    rightBack.value(0)
    rightForward.value(1)

