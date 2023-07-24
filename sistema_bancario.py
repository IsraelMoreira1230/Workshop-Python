class ContaBancaria:
    def __init__(self, nome_titular):
        self.nome_titular = nome_titular
        self.saldo = 0
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: +R${valor}")

    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            self.extrato.append(f"Saque: -R${valor}")
        else:
            print("Saldo insuficiente ou valor inválido!")

    def visualizar_extrato(self):
        print(f"Extrato da conta de {self.nome_titular}:")
        for operacao in self.extrato:
            print(operacao)
        print(f"Saldo atual: R${self.saldo}")


conta = ContaBancaria("Fulano")

conta.depositar(1000)
conta.sacar(500)
conta.depositar(200)
conta.sacar(1500)
conta.visualizar_extrato()
