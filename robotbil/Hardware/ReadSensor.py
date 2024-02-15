import time
from machine import ADC, Pin, time_pulse_us

gy = Pin(17, Pin.IN,)
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

def altMeasureDistance():
    while gy.value == True:
        pass
    pulsetime = time_pulse_us(17, 1)
    return pulsetime/100
def measureReflection():
    return(QA.read_u16())

def measureBattery():
    battery = bat.read_u16()
    battery_voltage = battery * (3.3/65535)*3
    return battery_voltage

print(altMeasureDistance())