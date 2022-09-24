class Cliente:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

    def getNome(self):
        return self.nome

    def getCPF(self):
        return self.cpf

    def getIdade(self):
        return self.idade

    def setNome(self, nome):
        self.nome = nome

    def setCPF(self, cpf):
        self.cpf = cpf

    def setIdade(self, idade):
        self.idade = idade

    def __str__(self):
        return "Nome: " + self.nome + " CPF: " + self.cpf + " Idade: " + str(self.idade)