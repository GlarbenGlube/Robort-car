from machine import Pin, PWM
from time import sleep

#venstre motor
leftForward = Pin(3, Pin.OUT)
leftBack = Pin(2, Pin.OUT)

#højre motor
rightForward = Pin(4, Pin.OUT)
rightBack = Pin(5, Pin.OUT)

def init():
    led = Pin(25, Pin.OUT)
    led.toggle()
    frequency = 10000
    dutycycle = .7

    leftpwm = PWM(Pin(0))
    leftpwm.freq(frequency)
    leftpwm.duty_u16(int(65536 * dutycycle))

    rightpwm = PWM(Pin(1))
    rightpwm.freq(frequency)
    rightpwm.duty_u16(int(65536 * dutycycle))

def forward():
    leftForward.value(1)
    rightForward.value(1)
    leftBack.value(0)
    rightBack.value(0)

def back():
    leftForward.value(0)
    rightForward.value(0)
    leftBack.value(1)
    rightBack.value(1)

def stop():
    leftForward.value(0)
    rightForward.value(0)
    leftBack.value(0)
    rightBack.value(0)

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
    rightBack.value(0)
    rightForward.value(1)
    leftBack.value(1)
    leftForward.value(0)


def turnleft():
    rightBack.value(1)
    rightForward.value(0)
    leftBack.value(0)
    leftForward.value(1)

