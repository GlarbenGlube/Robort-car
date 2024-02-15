import Hardware.motorstyrring as motor
from kommandoer import followWall, SUMO
from Hardware import ReadSensor as SA
import socket
import Connection.UDP as UDP
from time import sleep
import gc

ip = '10.120.0.86'
port = 5001

def UDPBattery():
    battery = str(SA.measureBattery())
    # Open UDP socket
    sleep(1)
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
    "wallfollow": followWall,
    "getbattery": UDPBattery,
}

while True:
    UDP.UDPConnect()
    HOST = '0.0.0.0'
    PORT = 5001
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((HOST, PORT))
    print(f"Listening for UDP messages on {HOST}:{PORT}")
    motor.UpdatePWM()
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
            else:
                x, y = map(int, message.split(','))
                print(f"Received coordinates: X={x}, Y={y}")


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