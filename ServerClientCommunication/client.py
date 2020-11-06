import socket
import sys

def client_socket():

    # host and port 
    _HOST = socket.gethostname()
    _PORT = 5000

    # adjust socket() and others using with statement
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sckt:

        try:
            # connect by connect() and pass parameters to function
            sckt.connect((_HOST,_PORT))
        except:
            print("Connection Error!")
            sys.exit()

        # the first input to send server
        print("to exit the system -> 'press q' ")
        message = input(" => ")

        while message.lower().strip() != "q": # if data is 'q' then exit the system

            sckt.send(message.encode())
            data = sckt.recv(1024).decode()
            print("to exit the system -> 'press q' ")
            print("Received from server : " + data)
            message = input(" => ")
        
        # close the socket
        sckt.close()

if __name__ == "__main__":

    client_socket()