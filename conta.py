

class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo o objeto ...{}".format(self))
        self.numero = numero
        self.titulo = titular
        self.saldo = saldo
        self.limite = limite

conta = Conta()
print(conta)

conta.saldo