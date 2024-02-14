from machine import Pin, idle, reset
import time
import network

def UDPConnect():
# Initialize network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect('ITEK 2nd', '2nd_Semester_F24v')
    wlandelay = time.ticks_ms() + 10000
    led = Pin("LED", Pin.OUT)

    # Check Wi-Fi connection
    while time.ticks_ms() < wlandelay:
        if wlan.isconnected():
            if wlan.status() < 0 or wlan.status() >= 3:
                break
        idle()

    if wlan.status() != 3:
        led.toggle()
        print('Wi-Fi connection failed')
        reset()
    else:
        led.toggle()
        print('Connected')
        status = wlan.ifconfig()
        print('ip = ' + status[0])
        wlan_mac = wlan.config('mac')
        print("MAC Address:", wlan_mac)  # Show MAC for peering
