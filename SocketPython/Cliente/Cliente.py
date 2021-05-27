import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


cliente.connect(('localhost', 6666))


namefile = str(input('Arquivo>'))

cliente.send(namefile.encode())

with open(namefile, 'wb') as file:
    while 1:
        data = cliente.recv(10000000)

        if not data:
            break
        file.write(data)

print(f'{namefile} recebido!\n')       