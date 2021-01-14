import socket
import time
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
while 1:
    sock.sendto(b'HELLO Champ', ("192.168.1.13", 8888))
    print("sent")
    time.sleep(120)

