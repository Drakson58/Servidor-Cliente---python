import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ''
porta = 9980
cliente.connect((host, porta)) # Se conecantando ao servidor.

while True:

    # Enviando msg para servidor
    msg = input('IP:')
    if(msg == '0'):
        
        msg = 'fechar'
        string = msg.encode('ascii')
        cliente.send(string)
        cliente.close()
        print('Conexão fechada')
        break
    else:

        string = msg.encode('ascii')
        cliente.send(string)

    # Recebendo msg do servidor
    tm = cliente.recv(1024)
    tm2 = tm.decode('ascii')
    print(tm2)

print('Bye, bye')
