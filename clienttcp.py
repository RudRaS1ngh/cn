import socket

serverName="127.0.0.1"
serverPort=12530
clientSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

fname=input("Enter file name:")
clientSocket.send(fname.encode())

fcontent=clientSocket.recv(1024).decode()
print("From server:",fcontent)

clientSocket.close()