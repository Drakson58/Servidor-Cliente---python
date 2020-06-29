class ValidaMensagem:

    
    def __init__(self, mensagem):
        self.__mensagem = mensagem
    

    def getMensagem(self):
        return self.__mensagem
    def setMensagem(self, mensagem):
        self.__mensagem = mensagem

    
    def contaPontos(self):
        if(self.__mensagem.count('.') == 3):
            return True
    

    def separaOctetos(self):
        return self.__mensagem.split('.')


    def verificaCampos(self, octetos):
        for cont in range(0, 4):
            if(octetos[cont].isdigit()):
                continue
            else:
                return False
        return True   
            

    def contaCampos(self, octetos):
        for cont in range(0, 4):
            if(len(octetos[cont]) < 4):
                continue
            else:
                return False
        return True