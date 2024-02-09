import Hardware.motorstyrring as motor
# import UserInterface.konsol as kons
# from UserInterface.kommandoer import followWall, SUMO, reset, ManualOverride
# from Hardware import ReadSensor as SA
import socket
import Connection.UDP as UDP

functions_dict = {
    "forward": motor.fremad,
    "stop": motor.stop,
    "backward": motor.tilbage,
}

motor.init()

while True:
    UDP.UDPConnect()
    HOST = '0.0.0.0'
    PORT = 5001
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((HOST, PORT))
    print(f"Listening for UDP messages on {HOST}:{PORT}")

    # Main loop
    while True:
        # Receiving and processing UDP messages
        data, addr = sock.recvfrom(1024)
        received_msg = data.decode('utf-8')  # Decode the received bytes to string
        global recieved_msg
        
        if received_msg in functions_dict:
            functions_dict[received_msg]()  # Call the function
        else:
            print("Function not found for input:", received_msg)