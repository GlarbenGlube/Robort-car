"""from machine import Pin, PWM
gy53 = Pin(19, Pin.IN)"""
import time


def measureDistance():
    gy53 = True
    while gy53.value() == True:
        pass
    while gy53.value() == False:
        pass
    startTime = time.ticks_us()
    while gy53.value() == True:
        pass
    endTime = time.ticks_us()
    TotalTime = endTime - startTime
    print(TotalTime/100)
    return TotalTime