from machine import Pin, PWM, idle
from time import sleep
import time
import network
import socket

# Initialize network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('ITEK 2nd', '2nd_Semester_F24v')
wlandelay = time.ticks_ms() + 10000

pwm = PWM(Pin(16))
pwm.freq(20)
IN1 = Pin(17, Pin.OUT)
IN2 = Pin(18, Pin.OUT)

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

HOST = '0.0.0.0'
PORT = 5001
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))
print(f"Listening for UDP messages on {HOST}:{PORT}")


# Function to simulate elevator movement


# Main loop
while True:
    # Receiving and processing UDP messages
    data, addr = sock.recvfrom(1024)
    received_msg = data.decode('utf-8')  # Decode the received bytes to string
    print(f"Received message from {addr}: {received_msg}")

    # Assuming the received message is the target floor number (1, 2, or 3)
    

    # Rest of your code can remain empty as the elevator control is now solely based on UDP messages