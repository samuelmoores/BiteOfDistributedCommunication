#This is out client script
import socket
import json
import os

UDP_IP = "224.1.1.1" #  "127.0.0.1" before, "224.1.1.1" now
UDP_PORT = 5007 # 5005 before, 5007 now

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #(Internet, UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)

# Improved for readability of the running ile
sender_name = os.environ.get('SERVER_NAME', socket.gethostname())

print(f"{sender_name} target IP: {UDP_IP}")
print(f"{sender_name} target port: {UDP_PORT}")

# Actuall JSON + Bin. Data implementation

# First Sender
json_mesag1 = {"Sensor": "temp", "value": 23.5}
sock.sendto(json.dumps(json_mesag1).encode('utf-8'), (UDP_IP, UDP_PORT))
print(f"{sender_name} sent JSON: {json_mesag1}")

# Second Sender
json_mesag2 = {"Sensor": "humidity", "value": 45.0}
sock.sendto(json.dumps(json_mesag2).encode('utf-8'), (UDP_IP, UDP_PORT))
print(f"{sender_name} sent JSON: {json_mesag2}")

# Binary Data
bin_data = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09'
sock.sendto(bin_data, (UDP_IP, UDP_PORT))
print(f"{sender_name} sent binary data: {bin_data}")

print(f"{sender_name} finished sending")
sock.close()
