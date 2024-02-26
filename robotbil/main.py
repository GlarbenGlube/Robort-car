import Hardware.motorstyrring as motor
from kommandoer import SUMO, followWall
from Hardware import ReadSensor as SA
# from edging import cbt
import socket
import Connection.UDP as UDP
from time import sleep
import gc

# ip = '192.168.137.1'
ip = '10.120.0.86'
port = 5001

def controller(x,y):
    speed = 60
    if x != 1: 
        y = int(y)
        if x == 5:
            print("state1 - forward / backward")
            if y <= 10:
                motor.stop()
                print("stop")
            else:
                print(y)
                motor.VariableSpeed(y,y)

        elif x == 4:
            print("state1 - forward / backward")
            if y <= 5:
                speed = 0
                motor.stop()
                print("stop")
            else:
                print(y)
                speed = y
                motor.VariableSpeed(-1*y,-1*y)
    
    elif x == 1:
        x,y = map(int,y.split('_'))
        if x == -1:
            if y == -1 or y == 1:
                motor.VariableSpeed(5, speed*y)
            if y == 0:
                motor.VariableSpeed(speed*-1,speed) 
        elif x == 1:
            if y == -1 or y == 1:
                motor.VariableSpeed(speed*y, 5)
            if y == 0:
                motor.VariableSpeed(speed,-1*speed) 
        elif x == 0:
            if y == -1 or y == 1:
                motor.VariableSpeed(speed*y, speed*y)
            if y == 0:
                motor.stop() 



def UDPBattery():
    battery = str(SA.measureBattery())
    sleep(0.5)
    # Open UDP socket
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    battery.encode('utf-8')
    sock.sendto(battery, (ip , port))
    sock.close()
    gc.collect()

receivermode = 0

functions_dict = {
    "forward": motor.forward,
    "stop": motor.stop,
    "backward": motor.back,
    "right": motor.turnright,
    "left": motor.turnleft,
    "wallfollow": followWall.followwall,
    "getbattery": UDPBattery,
    # "edging": cbt,
    "boxpush": SUMO.Sumo,
}

while True:
    UDP.UDPConnect()
    HOST = '0.0.0.0'
    PORT = 5001
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((HOST, PORT))
    print(f"Listening for UDP messages on {HOST}:{PORT}")

    motor.UpdateFreq(75,75)
    motor.UpdatePWM(0.4,0.4)

    # Main loop
    while True:
        print("Mode: ", receivermode)
        # Receiving and processing UDP messages
        data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
        if receivermode == 1:
            # Deserialize the coordinates
            message = data.decode()
            if message == 'manual':
                receivermode = 0
                motor.UpdatePWM(0.4,0.4)
            else:
                x, y = map(str, message.split(','))
                x = int(x)
                controller(x,y)

        else:
            received_msg = data.decode('utf-8')  # Decode the received bytes to string
            print(received_msg)
            if received_msg in functions_dict:
                functions_dict[received_msg]()  # Call the function
            else:
                if received_msg == 'controller':
                    receivermode = 1
                else:    
                    print("Function not found for input: ", received_msg)

                    