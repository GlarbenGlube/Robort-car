from machine import Pin, PWM
import time

def drejhøjre():
    venstreFrem.value(0)
    højreFrem.value(0)
    venstreTilbage.value(1)
    højreTilbage.value(1)

def drejvenstre():
    venstreFrem.value(0)
    højreFrem.value(0)
    venstreTilbage.value(1)
    højreTilbage.value(1)