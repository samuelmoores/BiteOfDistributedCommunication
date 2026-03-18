#This is out client script (Updated by Guy)
import socket
import json

UDP_IP = "224.1.1.1" #  "127.0.0.1" before, "224.1.1.1" now
UDP_PORT = 5007 # 5005 before, 5007 now
# MESSAGE = b"Hello, World!"

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)

#sock = socket.socket(socket.AF_INET, # Internet
#                     socket.SOCK_DGRAM) # UDP
#sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #(Internet, UDP)

# Actuall JSON + Bin. Data implementation

# First Sender
json_mesag1 = {"Sensor": "temp", "value": 23.5}
sock.sendto(json.dumps(json_mesag1).encode('utf-8'), (UDP_IP, UDP_PORT))
print(f"Sent JSON: {json_mesag1}")

# Second Sender
json_mesag2 = {"Sensor": "humidity", "value": 45.0}
sock.sendto(json.dumps(json_mesag2).encode('utf-8'), (UDP_IP, UDP_PORT))
print(f"Sent JSON: {json_mesag2}")

# Binary Data
bin_data = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09'
sock.sendto(bin_data, (UDP_IP, UDP_PORT))
print(f"Sent Binary Data: {bin_data}")

print("All messages should be sucessfully sent")
