import Hardware.motorstyrring as motor
import UserInterface.konsol as kons
from UserInterface.kommandoer import followWall, SUMO, reset, ManualOverride
from robotbil.Hardware import ReadSensor as SA
import socket
import Connection.UDP as UDP

while True:
    UDP.UDPConnect()
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
        print(received_msg)
