from Classes.ValidaMensagem import ValidaMensagem

import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
porta = 9980
servidor.bind((host, porta))
servidor.listen(5)


while True:

    
    conexaoCliente, ipCliente = servidor.accept()

    while True:

        # Recebendo msg do cliente
        string = conexaoCliente.recv(1024)
        mensagemDoCliente = string.decode('ascii')
        
        if(mensagemDoCliente == 'fechar'):

            print('Conexão fechada.')
            conexaoCliente.close()
            break
        else:    

            # Manipulção
            # print(type(mensagemDoCliente))
            ip = ValidaMensagem(mensagemDoCliente)
            
            if(ip.contaPontos()):
                octetos = ip.separaOctetos()
                if(ip.verificaCampos(octetos)):
                    if(ip.contaCampos(octetos)):
                        print('Campos valido')
                    
                
            # Enviando msg pro cliente
            dado = input('Digite Uma msg para o clinte')
            msg = dado.encode('ascii')
            conexaoCliente.send(msg)
    
    
        



