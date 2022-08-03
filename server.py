import socket
import threading

PORT = 5050
HOST_SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (HOST_SERVER,PORT)
HEADER = 64
FORMAT = "utf-8" 



server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def Client_Query(conn,addr) :
    print(f"\n[NEW USER] {addr} Connected!\n")
    
    connected = True
    while connected :
        msg_length  = conn.recv(HEADER).decode(FORMAT)
        if msg_length :
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            DISS_CONN = ["DISSCONECT","logout","exit"]
            if msg == DISS_CONN[0] or msg == DISS_CONN[1] or msg == DISS_CONN[2]:
                conn.send("You Succesfully Logged Out!".encode(FORMAT))
                print("User logged Out!...")
                connected = False
                
            print(f"{addr} : {msg}")
            conn.send("\nRecived!".encode(FORMAT))

    conn.close()




def Server_Activation():
    server.listen(1000)
    print(f"\n[SERVER ACTIVATED] Server Activated On [{HOST_SERVER}] ")
    while True :
        conn, addr = server.accept()
        thread = threading.Thread(target=Client_Query,args=(conn,addr))
        thread.start()
        print(f"\n[USER] {threading.activeCount() -  1}\n")
        

print("\n[STARTING] Server is getting activated...\n")
Server_Activation()


