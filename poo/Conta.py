from Extrato import Extrato
from Transacao import Transacao

class Conta:
    def __init__(self, numero, titular, saldo, limite):

        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__memoria = Extrato()

    def getTitular(self):
        return self.__titular

    def saldo(self):
        print(f'O saldo de {self.__titular.getNome()} e de R$ {self.__saldo}')

    def extrato(self):
        for transacao in self.__memoria.getHistorico():
            print(transacao)
        self.saldo()

    def deposita(self, valor):

        self.__saldo += valor
        transacao = Transacao(Transacao.DEPOSITO, valor, self)
        self.__memoria.adiciona(transacao)


    def saque(self, valor):

        if valor > self.__limite:

            print("Saque negado, ultrapassa o limite")

        else:

            self.__saldo -= valor

            transacao = Transacao(Transacao.SAQUE, valor, self)
            self.__memoria.adiciona(transacao)

    def transferir(self, valor, destino):

        if self.__saldo > valor > self.__limite:

            print("Saque negado, ultrapassa o limite")

        else:
            # sacando valor da conta que transferiu

            self.__saldo -= valor

            #dando o valor para outra conta

            destino.__saldo += valor

            transacao = Transacao(Transacao.TRANSFERENCIA_ENVIADA, valor, self, destino)
            self.__memoria.adiciona(transacao)
            transacao = Transacao(Transacao.TRANSFERENCIA_RECEBIDA, valor, self, destino)
            destino.__memoria.adiciona(transacao)
