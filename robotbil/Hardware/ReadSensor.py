import time 
from machine import ADC, Pin, time_pulse_us

gy = Pin(0, Pin.IN,)
QA = ADC(Pin(26))
bat = ADC(Pin(27))

def measureDistance():
    while gy.value == True: pass
    pulsetime = time_pulse_us(gy, 1)
    print(pulsetime/100)
    return pulsetime/100

def measureReflection():
    return(QA.read_u16())

def measureBattery():
    battery = bat.read_u16()
    battery_voltage = battery/(8.4*(1/3))*3.3/65535*8.4
    print(battery_voltage)
    return battery_voltage

# testing the distance measuring function 
# while True:
#     print(measureDistance())
