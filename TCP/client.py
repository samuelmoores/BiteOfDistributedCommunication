import socket
import time

def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('anycast_server', 5000))  # Docker picks which server
    response = client.recv(1024)
    print(f"Response: {response.decode()}", flush=True)
    client.close()

if __name__ == '__main__':
    time.sleep(2)
    round = 1
    while True:
        print(f"--- Round {round} ---", flush=True)
        connect()
        round += 1
        time.sleep(2)
