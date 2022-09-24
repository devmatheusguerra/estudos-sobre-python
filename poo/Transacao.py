from datetime import datetime

class Transacao:
    TRANSFERENCIA_ENVIADA = 1
    TRANSFERENCIA_RECEBIDA = 2
    DEPOSITO = 3
    SAQUE = 4

    def __init__(self, tipo , valor, de, para = None):
        self.__data = datetime.now()
        self.__tipo = tipo
        self.__valor = valor
        self.__de = de
        if tipo == Transacao.TRANSFERENCIA_ENVIADA or tipo == Transacao.TRANSFERENCIA_RECEBIDA:
            self.__para = para

    def __str__(self) -> str:
        if self.__tipo == Transacao.TRANSFERENCIA_ENVIADA:
            return f"{self.getDataFormatada()} - Transferência de R$ {self.__valor} enviada para {self.__para.getTitular().getNome()}"
        elif self.__tipo == Transacao.TRANSFERENCIA_RECEBIDA:
            return f"{self.getDataFormatada()} - Transferência de R$ {self.__valor} recebida de {self.__de.getTitular().getNome()}"
        elif self.__tipo == Transacao.DEPOSITO:
            return f"{self.getDataFormatada()} - Depósito de {self.__valor}"
        elif self.__tipo == Transacao.SAQUE:
            return f"{self.getDataFormatada()} - Saque de {self.__valor}"

    def getDataFormatada(self):
        return self.__data.strftime("%d/%m/%Y %H:%M:%S")
        
