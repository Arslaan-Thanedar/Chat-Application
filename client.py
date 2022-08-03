import socket

PORT = 5050
HEADER = 64
FORMAT = "utf-8"
DISS_CONN = ["DISSCONECT","logout","exit"]
SERVER = "YOUR HOST MACHINE IP ADDRESS"
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


while 1:

    x = input(str("Type a message : "))

    if "logout" in x or "Disconnect" in x or "exit" in x :
        print("Logged Out...")
        break
    send(x)    




