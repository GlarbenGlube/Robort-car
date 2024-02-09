from machine import Pin, PWM
from time import sleep

#højre motor
rightForward = Pin(5, Pin.OUT)
rightBack = Pin(4, Pin.OUT)

#venstre motor
leftForward = Pin(2, Pin.OUT)
leftBack = Pin(3, Pin.OUT)

def init():
    frequency = 6000
    dutycycle = 50

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

def onspotturnright(grader):
    rightForward.value(0)
    leftBack.value(0)
    leftForward.value(1)
    rightBack.value(1)
    sleep(grader)
    leftForward.value(0)
    rightBack.value(0)

def onspotturnleft(grader):
    leftForward.value(0)
    rightBack.value(0)
    rightForward.value(1)
    leftBack.value(1)
    sleep(grader)
    rightForward.value(0)
    leftBack.value(0)

def turnright(grader):
    leftBack.value(0)
    leftForward.value(1)
    sleep(grader)
    leftForward.value(0)

def turnleft(grader):
    rightBack.value(0)
    rightForward.value(1)
    sleep(grader)
    rightForward.value(0)


