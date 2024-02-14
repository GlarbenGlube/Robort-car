import Hardware.motorstyrring as motor
from kommandoer import followWall, SUMO
from Hardware import ReadSensor as SA
import socket
import Connection.UDP as UDP

ip = 0
port = 5001

functions_dict = {
    "forward": motor.forward,
    "stop": motor.stop,
    "backward": motor.back,
    "right": motor.turnright,
    "left": motor.turnleft,
    "wallfollow": followWall,
    "getbattery": UDPBattery,
}

def UDPBattery():
    # Open UDP socket
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # Convert to utf-8 formatted bytestring
    sock.sendto(bytes((SA.measureBattery(), "utf-8"), (ip , port)))

receivermode = 0

while True:
    UDP.UDPConnect()
    HOST = '0.0.0.0'
    PORT = 5001
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((HOST, PORT))
    print(f"Listening for UDP messages on {HOST}:{PORT}")
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
            
            if received_msg in functions_dict:
                functions_dict[received_msg]()  # Call the function
            else:
                if received_msg == 'controller':
                    receivermode = 1
                else:    
                    print("Function not found for input: ", received_msg)