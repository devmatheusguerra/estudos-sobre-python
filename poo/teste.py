from Conta import Conta
from Cliente import Cliente

cliente1 = Cliente("Joao", "123.456.789-10", 25)
cliente2 = Cliente("Maria", "987.654.321-10", 30)

conta1 = Conta(1, cliente1, 1000, 1000)
conta2 = Conta(2, cliente2, 100, 1000)

conta1.deposita(100)
conta1.saque(50)
conta1.transferir(100, conta2)

conta1.extrato()

print("\n\n\n")
conta2.extrato()


