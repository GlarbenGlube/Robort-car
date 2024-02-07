from machine import Pin, PWM
import time

frequency = x
dutyCycle = x

pwm = PWM(Pin(x))
pwm.freq(frequency)

#højre motor
højreFrem = Pin(x, Pin.OUT)
højreTilbage = Pin(x, Pin.OUT)

#venstre motor
venstreFrem = Pin(x, Pin.OUT)
venstreTilbage = Pin(x, Pin.OUT)



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


