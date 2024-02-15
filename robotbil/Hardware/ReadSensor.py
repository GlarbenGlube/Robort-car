import time
from machine import ADC, Pin

gy = Pin(17, Pin.IN, Pin.PULL_DOWN)
QA = ADC(Pin(26))
bat = ADC(Pin(27))

def measureDistance():
    gy = True
    while gy.value() == True:
        pass
    while gy.value() == False:
        pass
    startTime = time.ticks_us()
    while gy.value() == True:
        pass
    endTime = time.ticks_us()
    TotalTime = endTime - startTime
    print(TotalTime/100)
    return TotalTime

def measureReflection():
    return(QA.read_u16())

def measureBattery():
    battery = bat.read_u16()
    battery_voltage = battery * (3.3/65535)*3
    return battery_voltage

print(measureDistance())