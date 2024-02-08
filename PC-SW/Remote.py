import socket

def remote(command: str):
    com = { "forward":1  ,}
    if command in com:
        UDPSend(com[command])
def UDPSend(cmd):
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    sock.sendto(bytes(cmd, "utf-8"), ('10.120.0.8' , 5001))

while True:
    UDPSend(input())