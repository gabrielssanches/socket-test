# echo-client.py

import socket
import time

#HOST = "127.0.0.1"  # The server's hostname or IP address
HOST = "104.237.132.236"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        s.sendall(b"Hello, world")
        time.sleep(0.1);
        recv_data = s.recv(1024)
        if recv_data:
            print(f"Received {recv_data!r}")
        time.sleep(0.9);


