from Classes.ValidaMensagem import ValidaMensagem
from Classes.VerificaClasse import ClasseIP
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
        
        resposta = 'Ip invalido'
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
                        tipoIP = ClasseIP(octetos)
                        resposta = tipoIP.tipoClasse()
                        if(resposta == ''):
                            resposta = 'Ip invalido'
            # Enviando msg pro cliente
            msg = resposta.encode('ascii')
            conexaoCliente.send(msg)
    
    
        



