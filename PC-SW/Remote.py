import socket
def UDPSend(cmd:str):
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    sock.sendto(bytes(cmd, "utf-8"), ('10.120.0.8' , 5001))