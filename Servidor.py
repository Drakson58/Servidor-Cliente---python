import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ''
porta = 9980
servidor.bind((host, porta))
servidor.listen(5)


while True:

    
    conexaoCliente, ipCliente = servidor.accept()

    while True:

        # Recebendo msg do cliente
        string = conexaoCliente.recv(1024)
        mensagem = string.decode('ascii')
        
        if(mensagem == 'fechar'):

            print('Conexão fechada.')
            conexaoCliente.close()
            break
        else:    

            dado = input('Digite Uma msg para o clinte')
            # Enviando msg pro cliente
            msg = dado.encode('ascii')
            conexaoCliente.send(msg)
    
    
        



