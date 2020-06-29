import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
porta = 9980
cliente.connect((host, porta)) # Se conecantando ao servidor.

while True:

    print('*** BUSCA INFORMAÇÕES SOBRE UM IP ***')
    print('Digite o IP ou 0 para fechar a conexão.')
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
