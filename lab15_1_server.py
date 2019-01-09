#! /usr/bin/python3

import socket
import time
import datetime

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9999
server_socket.bind((host, port))
server_socket.listen(5)
print('the server is waiting for connection')
while True:
    client_socket, addr = server_socket.accept()
    print('Got a connection from {}'.format(addr))

    client_socket.send('What is your name?'.encode('utf-8'))
    client_answer = client_socket.recv(1024)
    print(client_answer.decode('utf-8'))
    client_socket.send((('Hello, ' + client_answer.decode('utf-8')) + '\n').encode('utf-8'))
    while True:
        client_socket.send("What do you want?".encode('utf-8'))
        client_answer = client_socket.recv(1024)
        response = client_answer.decode('utf-8')

        if response == 'Exit.':
            client_socket.close()
            break

        if response == 'What time is it?':
            client_socket.send(datetime.datetime.fromtimestamp(time.time()).strftime('Current server time: %Y-%m-%d '
                                                                                     '%H:%M:%S\n').encode('utf-8'))
        if response == 'How far is the Sun from the Earth?':
            client_socket.send('The distance from Earth to the Sun is 149600000 km.'.encode('utf-8'))

        if response == 'How far is the Moon from the Earth?':
            client_socket.send('The Moon orbits the Earth at a distance of, on average, 384,000 km.'.encode('utf-8'))
    print('Client disconected')