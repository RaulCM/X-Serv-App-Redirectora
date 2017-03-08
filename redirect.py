#!/usr/bin/python3


import socket
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Let the port be reused if no process is actually using it
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind to the address corresponding to the main name of the host
mySocket.bind(('localhost', 1234))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an almost-infinite loop; the loop can be stopped with Ctrl+C)

try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('HTTP request received:')
        peticion = recvSocket.recv(2048).decode("utf-8", "strict")
        print(peticion)
        randomURL = ("http://localhost:1234/" +
                     str(random.randint(1, 1000000)))
        mensaje = "Seras redirigido a un recurso aleatorio en 3 segundos."
        recvSocket.send(bytes("HTTP/1.1 301 \r\n\r\n" +
                              "<html><body><h1>" + mensaje + "</h1>" +
                              "<meta http-equiv='refresh' content=3;url=" +
                              randomURL + ">" + "</body></html>" +
                              "\r\n", 'utf-8'))
        recvSocket.close()

except KeyboardInterrupt:
    print ("Closing binded socket")
    mySocket.close()
