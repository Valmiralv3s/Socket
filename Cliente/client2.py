import socket

HOST = '127.0.0.1'
PORT = 50000
# TCP funciona melhor em casos que a confiabilidade do transporte de dados é o foco, como quando trabalhamos com comunicação em texto ou com documentos.

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))
print('Conectado! \n')

namefile = str(input('Arquivo>'))
cliente.send(namefile.encode())
with open(namefile, 'wb') as file:
    while 1:
        data = cliente.recv(1000000)
        if not data:
            break
        file.write(data)

print(f'{namefile}Arquivo recebido! \n')
