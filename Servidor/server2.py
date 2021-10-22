
import socket

HOST = ''
PORT = 50000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
print('Aguardando conexões')
server.listen(5)

conn, ender = server.accept()

namefile = conn.recv(4896)

with open(namefile, 'rb') as file:
    for data in file.readlines():

        conn.send(data)
    print('Arquivo recebido!')
