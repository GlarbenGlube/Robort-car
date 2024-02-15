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

def UDPRecieve():
    HOST = '0.0.0.0'
    PORT = 5001
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(2)
    sock.bind((HOST, PORT))
    print(f"Listening for UDP messages on {HOST}:{PORT}")
    try: data, addr = sock.recvfrom(1024)
    except: 
        print("no data recieved")
        return
    return data.decode('utf-8')
