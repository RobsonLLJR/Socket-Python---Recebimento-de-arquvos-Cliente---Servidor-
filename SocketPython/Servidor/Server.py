import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 6666

server.bind((host, port))

print('Servidor', 6666)
print('ESPERANDO CONEXÃO!\n')

server.listen(1)

connection, address = server.accept()
print('Cliente!: ', address, 'porta: ', port)



nameFile = connection.recv(4096).decode

with open(nameFile, 'rb') as file:
    for data in file.readlines():
        connection.send(data)

    print('Arquivo enviado!')    

