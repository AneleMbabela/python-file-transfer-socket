import os
import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(),22222))
sock.listen(5)
print("HOST: ", sock.getsockname())

# accepting the connection from the client.
client, addr = sock.accept()

# getting the file details to be sent
file_name = input("File Name:")
file_size = os.path.getsize(file_name)

# send the file details to the client.
client.send(file_name.encode())
client.send(str(file_size).encode())

# Open and read the file.
with open(file_name, "rb") as file:
    c = 0

    # start the time capture.
    start_time = time.time()

    # running the loop while the file is sent
    while c <= file_size:
        data = file.read(1024)
        if not (data):
            break
        client.sendall(data)
        c += len(data)

    # end time capture
    end_time = time.time()

print("File transfer complete. Total time: ",end_time - start_time)

# closing the socket.
sock.close()