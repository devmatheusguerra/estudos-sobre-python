class Extrato:
    def __init__(self):
        self.__historico = []

    def adiciona(self, transacao):
        self.__historico.append(transacao)

        
    def getHistorico(self):
        return self.__historico

