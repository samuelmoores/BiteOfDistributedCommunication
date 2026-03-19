Req: Open 3 terminals in your command prompt in the same file directory
Note: Can duplicate command prompt by right clicking

Step 1:
    Start the receivers first (first terminal):
    docker-compose up --build receiver1 receiver2 receiver3
Step 2: 
    Run the tcpdump inside one receiver (second terminal) (within 5 seconds of running step 1):
    docker exec -it udpproject-receiver1-1 tcpdump -i eth0 udp port 5007 -nn
Step 3:
    In third terminal start the senders (third terminal) (within 10-15 sec of running step 2):
    docker-compose up sender1 sender2
