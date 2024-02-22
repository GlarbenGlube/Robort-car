import Hardware.motorstyrring as motor
from kommandoer import followWall, SUMO
from Hardware import ReadSensor as SA
# from edging import cbt
import socket
import Connection.UDP as UDP
from time import sleep
import gc

# ip = '192.168.137.1'
ip = '10.120.0.86'
port = 5001

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
    "wallfollow": followWall,
    "getbattery": UDPBattery,
    # "edging": cbt,
    "boxpush": SUMO
}

while True:
    UDP.UDPConnect()
    HOST = '0.0.0.0'
    PORT = 5001
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((HOST, PORT))
    print(f"Listening for UDP messages on {HOST}:{PORT}")

    motor.UpdateFreq(1200,1200)
    motor.UpdatePWM(0.7,0.7)

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
                if x == 5:
                    print("state1 - forward / backward")
                    if y <= 20:
                        motor.stop()
                        print("stop")
                    else:
                        print(y)
                        motor.VariableLeft(y)
                        motor.VariableRight(y)
                elif x == 4:
                    print("state1 - forward / backward")
                    if y <= 5:
                        motor.stop()
                        print("stop")
                    else:
                        print(y)
                        motor.VariableLeft(-1*y)
                        motor.VariableRight(-1*y)
                elif x == 0:
                    print("state2 - left/right")
                    if y < 0:
                        print("left: ",y)
                        motor.VariableRight(100 - (y*-1))
                    elif y > 0:
                        print("Right: ",y)
                        motor.VariableLeft(100-y)
                    else: 
                        motor.stop() 
                        print("state3 - stop")

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