import socket

serverName="127.0.0.1"
serverPort=12530
serverSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((serverName,serverPort))
serverSocket.listen(1)

print("Server up")

while True:
    connectionSocket,addr=serverSocket.accept()
    filename=connectionSocket.recv(1024).decode()
    try:
        with open(filename,"r") as file:
            fcontent=file.read(1024)
        connectionSocket.sendall(fcontent.encode())
        print("File content sent successfully.")
    except FileNotFoundError:
        connectionSocket.sendall("404".encode())
    finally:
        connectionSocket.close()
    break
serverSocket.close()
print("Server down")