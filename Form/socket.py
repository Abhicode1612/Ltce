#Server Code

#import socket
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# host = socket.gethostname()
# port = 8000
# s.bind ((host, port))
# s.listen(1)
# con, address= s.accept()
# print ("Connected:",address)
# while True:
#     msg = input ("sends message to client:")
#     con.send (msg .encode ())
#     print ("Waiting for response")
#     rev_msg = con.recv(1024)
#     print("Client:",rev_msg.decode())



#Client Code
import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8000
s.connect((host, port))
while True:
    print("waiting for response")
    rev_msg = s.recv(1024)
    print("Server:", rev_msg.decode())
    msg=input("send message to server:")
    s.send(msg.encode())