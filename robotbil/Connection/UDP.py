from machine import Pin, idle, reset
import time
import network

def UDPConnect():
# Initialize network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect('ITEK 2nd', '2nd_Semester_F24v')  
    # wlan.connect('pico test','123454321') 
    wlandelay = time.ticks_ms() + 10000     # Set timeout for connection
    
    led = Pin("LED", Pin.OUT)

    # Wait for Wi-Fi connection, continue when connected
    while time.ticks_ms() < wlandelay:
        if wlan.isconnected():
            if wlan.status() < 0 or wlan.status() >= 3:
                break
        idle()


    if wlan.status() != 3:                  # If wlan doesn't connect
        led.off()                           # Change led state
        print('Wi-Fi connection failed')
        reset()
    else:
        led.on()                            # Indicate connection success
        print('Connected')                  # Indicate connection success
        status = wlan.ifconfig()
        print('ip = ' + status[0])          # Show ip for connecting with GUI
        wlan_mac = wlan.config('mac')       
        print("MAC Address:", wlan_mac)     # Show MAC for peering
