class ClasseIP:


    def __init__(self, octetos):
        self._ipPartido = octetos


    def tipoClasse(self):
        if int(self._ipPartido[0]) > 1 and int(self._ipPartido[0]) < 127:
            return 'A'
        elif int(self._ipPartido[0]) > 127 and int(self._ipPartido[0]) < 192:
            return 'B'
        elif int(self._ipPartido[0]) < 128 and int(self._ipPartido[0]) > 126:
            return 'loopback'
        elif int(self._ipPartido[0]) > 191 and int(self._ipPartido[0]) < 224:
            return 'C'
        elif int(self._ipPartido[0]) > 223 and int(self._ipPartido[0]) < 240:
            return 'D'