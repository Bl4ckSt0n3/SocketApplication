import socket
import time
import sys


def server_socket():

    # get hostname and adjust port number
    _PORT = 5000
    _HOST = socket.gethostname()

    print("Server is loading...")
    time.sleep(1)
    print("Complated !")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sckt:

        # adjust these steps bind() -> listen() -> accept()
        try:
            sckt.bind((_HOST, _PORT))
        except:
            print("Bind failed ! Error "+str(sys.exc_info()))
            sys.exit()

        sckt.listen(2)
        conn, addr = sckt.accept()
        print("Connected with " + str(addr[0]) +" : "+ str(addr[1]))
        print("connection:: "+str(conn))

        while True:

            # receive data stream. it won't be able to accept data packet greater than 1024 bytes   
            data = conn.recv(1024).decode()   # decode recieved data of connection because the data comes in bytes

            if not data: 
                break

            print("from connected client {}".format(_HOST) + ": " + str(data))
            data = input(" => ")
            conn.send(data.encode()) # data is encoded before sending because the data comes in byte level

        conn.close()

if __name__ == "__main__":

    server_socket()