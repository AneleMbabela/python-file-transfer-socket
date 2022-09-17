import os
import socket
import time

host = input("Enter Host Name: ")
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# trying to connect to the socket.
try:
    sock.connect((host,22222))
    print("Connected Successfully")
except:
    print("Unable to connect")
    exit(0)

# recieve file details.
file_name = sock.recv(100).decode()
file_size = sock.recv(100).decode()

# open and write the file.
with open("./rec/" + file_name,"wb") as file:
    c = 0

    # starting the time capture.
    start_time = time.time()

    # will run the loop till all of the file is recieved.
    while c <= int(file_size):
        data = sock.recv(1024)
        if not (data):
            break
        file.write(data)
        c += len(data)

    # ending the time capture.
    end_time = time.time()

print("File transfer complete. Total time: ",end_time - start_time)

# Close the socket.
sock.close()
