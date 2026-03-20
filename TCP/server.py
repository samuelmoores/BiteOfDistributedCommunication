import socket
import os

# Set SERVER_NAME in docker-compose or default to hostname
name = os.environ.get('SERVER_NAME', socket.gethostname())

# create TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 5000 defined in dockerfile
server.bind(('0.0.0.0', 5000))
server.listen(5)
print(f"Server {name} listening on port 5000...", flush=True)

while True:
    # connect to the client from one of the replica servers
    conn, addr = server.accept()
    print(f"Connection from {addr}", flush=True)
    conn.send(f"Hello from {name}!\n".encode())
    conn.close()
