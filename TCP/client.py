import socket
import time

def connect():
    # create TCP socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to one of three replica servers defined in compose file
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

        # wait for other replicas to print
        time.sleep(2)
