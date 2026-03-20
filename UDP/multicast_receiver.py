#This is our server script
import socket
import argparse
import os
import time
import struct

UDP_IP = "224.1.1.1" # Changed IP port from "127.0.0.1" to "224.1.1.1" to accept IP given as an example in the instructions
UDP_PORT = 5007 # Changed UDP Port from 5005 to 5007 port so that sender and reciever don't conflict 
duration = 5

#Read argument
parser = argparse.ArgumentParser()
parser.add_argument("--duration", help="Maximum time to listen (seconds)")
args = parser.parse_args() #args will contain our args

#Check if "duration" was given a value
duration = int(args.duration) if args.duration else 10

#Create Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # (Internet, UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Allow reuse of socket

# Note: Binding needs to be to all interfaces and not just the group IP 
sock.bind(('', UDP_PORT)) #Connect to socket we just created


# Multicast Group (joining part)
brig_IP = "172.20.0.1" # for docker bridge getway
mreq = struct.pack("4sL", socket.inet_aton(UDP_IP), socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
print("Joined multicast group")

#Set timer
end_time = time.time() + duration
sock.settimeout(max(duration/10, 1)) #Set timeout length to be duration to be short as we will loop

# I stole this from Sam, I figure we'll need it later | Set SERVER_NAME in docker-compose or default to hostname  
# This was neeeded to run it properly (Guy)
name = os.environ.get('SERVER_NAME', socket.gethostname())


def listen():
    print(f"Server {name} listening on port {UDP_PORT}")
    while time.time() < end_time:
        try:
            data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes. We yield here
            #print("received message: %s" % data) #CHANGE WHEN IMPLEMENTING RECEIVES
            try:
                decoded = data.decode('utf-8') # if decoded txt contains npc, treat as bin
                print(f"Recieved: {decoded} from {addr}")
            except UnicodeDecodeError:
                print(f"Received binary from {addr}: {data}")
        except socket.timeout:
            pass # keep going

    # While loop complete or error occured
    print("Leaving multicast group")
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_DROP_MEMBERSHIP, mreq)
    print(f"Closing socket: {name}")
    sock.close()
    print(f"{name} closed")

listen()
