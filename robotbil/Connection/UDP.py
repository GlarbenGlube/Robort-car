from machine import Pin, PWM, idle
from time import sleep
import time
import network
import socket

def UDPConnect():
# Initialize network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect('ITEK 2nd', '2nd_Semester_F24v')
    wlandelay = time.ticks_ms() + 10000

    # Check Wi-Fi connection
    while time.ticks_ms() < wlandelay:
        if wlan.isconnected():
            if wlan.status() < 0 or wlan.status() >= 3:
                break
        idle()

    if wlan.status() != 3:
        raise RuntimeError('Wi-Fi connection failed')
        machine.reset()
    else:
        print('Connected')
        status = wlan.ifconfig()
        print('ip = ' + status[0])
        wlan_mac = wlan.config('mac')
        print("MAC Address:", wlan_mac)  # Show MAC for peering