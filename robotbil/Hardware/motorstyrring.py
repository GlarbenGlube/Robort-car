from machine import Pin, PWM
from time import sleep

#højre motor
højreFrem = Pin(5, Pin.OUT)
højreTilbage = Pin(4, Pin.OUT)

#venstre motor
venstreFrem = Pin(2, Pin.OUT)
venstreTilbage = Pin(3, Pin.OUT)

def init():
    frequency = 6000
    dutycycle = 50

    leftpwm = PWM(Pin(0))
    leftpwm.freq(frequency)
    leftpwm.duty_u16(int(65536 * dutycycle))

    rightpwm = PWM(Pin(1))
    rightpwm.freq(frequency)
    rightpwm.duty_u16(int(65536 * dutycycle))

def stop():
    venstreFrem.value(0)
    højreFrem.value(0)
    venstreTilbage.value(0)
    højreTilbage.value(0)

def fremad():
    venstreFrem.value(1)
    højreFrem.value(1)
    venstreTilbage.value(0)
    højreTilbage.value(0)


def tilbage():
    venstreFrem.value(0)
    højreFrem.value(0)
    venstreTilbage.value(1)
    højreTilbage.value(1)


def drejhøjre(grader):
    venstreFrem.value(1)
    højreFrem.value(0)
    venstreTilbage.value(0)
    højreTilbage.value(1)
    sleep(grader)
    venstreFrem.value(0)
    højreTilbage.value(0)

def drejvenstre(grader):
    venstreFrem.value(0)
    højreFrem.value(1)
    venstreTilbage.value(1)
    højreTilbage.value(0)
    sleep(grader)
    højreFrem.value(0)
    venstreTilbage.value(0)