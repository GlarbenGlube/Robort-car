import socket
ip = '10.120.0.8'
port = 5001

def UDPSend(cmd:str):
    # Open UDP socket
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # Convert to utf-8 formatted bytestring
    sock.sendto(bytes(cmd, "utf-8"), (ip , port))

def send_coordinates(x, y):
    # Convert to byte string
    message = f"{x},{y}".encode()

    # Open UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Send the message
    sock.sendto(message, (ip , port))