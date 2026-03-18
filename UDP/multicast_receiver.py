#This is our server script
import socket
import argparse
import os
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
duration = 5

#Read argument
parser = argparse.ArgumentParser()
parser.add_argument("-duration", help="Maximum length between receives before" )
args = parser.parse_args() #args will contain our args

#Check if "duration" was given a value
duration = 10 #Default value
if args.duration != None:
    duration = int(args.duration)

#Create Socket
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Allow reuse of socket
sock.bind((UDP_IP, UDP_PORT)) #Connect to socket we just created

#Set timer
end_time = time.time() + duration
sock.settimeout(duration) #Set timeout length to be duration

# I stole this from Sam, I figure we'll need it later | Set SERVER_NAME in docker-compose or default to hostname
name = os.environ.get('SERVER_NAME', socket.gethostname())


def listen():
    print(f"Server {name} listening on port {UDP_PORT}")
    try:
        while time.time() < end_time:
            data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes. We yield here
            print("received message: %s" % data) #CHANGE WHEN IMPLEMENTING RECEIVES

    #We reach a timeout, exit
    except socket.timeout:
        print(f"{name} timed out")
    except Exception:
        print(f"Error: {Exception}")

    #While loop complete or error occured
    print(f"Closing socket: {name}")
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()
    print(f"{name} closed")

listen()
