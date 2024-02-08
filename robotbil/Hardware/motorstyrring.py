from machine import Pin, PWM
import time

frequency = "placeholder"
dutyCycle = "placeholder2"

pwm = PWM(Pin("placeholder3"))
pwm.freq(frequency)

#højre motor
højreFrem = Pin("placeholder4", Pin.OUT)
højreTilbage = Pin("placeholder5", Pin.OUT)

#venstre motor
venstreFrem = Pin("placeholder6", Pin.OUT)
venstreTilbage = Pin("placeholder7", Pin.OUT)



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
    time.sleep(grader)
    venstreFrem.value(0)
    højreTilbage.value(0)

def drejvenstre(grader):
    venstreFrem.value(0)
    højreFrem.value(1)
    venstreTilbage.value(1)
    højreTilbage.value(0)
    time.sleep(grader)
    højreFrem.value(0)
    venstreTilbage.value(0)