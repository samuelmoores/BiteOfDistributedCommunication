#This is our server script
import socket
import time
import asyncio

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
duration = 5

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
socket_live = True



async def auto_close(x:int):
    '''Close socket after x seconds'''
    print("closing socket in 5")
    await asyncio.sleep(x)
    socket_live = False
    sock.detach()
    print("Receiver disconnected")

async def listen():
    print("Listening")
    while socket_live:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes. We yield here
        print("received message: %s" % data)

async def main():
    await asyncio.gather(auto_close(duration),listen()) #Runs both simultaneously

asyncio.run(main())