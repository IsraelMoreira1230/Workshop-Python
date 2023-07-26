class Usuario:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco

    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Data de Nascimento: {self.data_nascimento}, Endereço: {self.endereco}"


class Conta:
    numero_conta = 1

    def __init__(self, usuario):
        self.agencia = "1"
        self.numero = Conta.numero_conta
        self.usuario = usuario
        self.saldo = 0
        self.extrato = []
        Conta.numero_conta += 1

    def __str__(self):
        return f"Agência: {self.agencia}, Número: {self.numero}, Usuário: {self.usuario.nome}, Saldo: R${self.saldo}"

    def sacar(self, *, saldo, valor, limite, limite_saques, numero_saques):
        if valor > 0 and valor <= saldo + limite and numero_saques < limite_saques:
            saldo -= valor
            numero_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Valor inválido para saque ou limite de saques atingido!")
        return saldo

    def depositar(self, saldo, valor):
        if valor > 0:
            saldo += valor
            print("Depósito realizado com sucesso!")
            self.extrato.append(f"Depósito: +R${valor}")
        else:
            print("Valor inválido para depósito!")
        return saldo

    def extrato(self, saldo, *, extrato):
        print(f"Saldo atual: R${saldo}")
        if extrato:
            print("Extrato:")
            for item in extrato:
                print(item)


def cadastrar_usuario():
    nome = input("Nome: ")
    cpf = input("CPF: ")
    data_nascimento = input("Data de Nascimento: ")
    endereco = input("Endereço: ")
    return Usuario(nome, cpf, data_nascimento, endereco)


def cadastrar_conta_corrente(usuarios):
    print("Usuários cadastrados:")
    for indice, usuario in enumerate(usuarios):
        print(f"Índice: {indice}, {str(usuario)}")

    indice_usuario = int(
        input("Digite o índice do usuário para vincular à conta corrente: "))
    usuario = usuarios[indice_usuario]
    conta = Conta(usuario)
    print("Conta corrente criada com sucesso!")
    return conta


def listar_contas(contas):
    for conta in contas:
        print(str(conta))

# Programa principal


usuarios = []
contas = []

while True:
    print("\n1 - Cadastrar usuário")
    print("2 - Cadastrar conta corrente")
    print("3 - Sacar")
    print("4 - Depositar")
    print("5 - Extrato")
    print("6 - Listar contas")
    print("0 - Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        usuario = cadastrar_usuario()
        if any(u.cpf == usuario.cpf for u in usuarios):
            print("Já existe um usuário cadastrado com esse CPF!")
        else:
            usuarios.append(usuario)
            print("Usuário cadastrado com sucesso!")

    elif opcao == "2":
        if usuarios:
            conta_corrente = cadastrar_conta_corrente(usuarios)
            contas.append(conta_corrente)
        else:
            print("Não existem usuários cadastrados!")

    elif opcao == "3":
        numero_conta = int(input("Digite o número da conta corrente: "))
        for conta in contas:
            if conta.numero == numero_conta:
                valor = float(input("Digite o valor do saque: "))
                conta.saldo = conta.sacar(
                    saldo=conta.saldo, valor=valor, limite=1000, limite_saques=5, numero_saques=0)
                break
        else:
            print("Conta corrente não encontrada!")

    elif opcao == "4":
        numero_conta = int(input("Digite o número da conta corrente: "))
        for conta in contas:
            if conta.numero == numero_conta:
                valor = float(input("Digite o valor do depósito: "))
                conta.saldo = conta.depositar(saldo=conta.saldo, valor=valor)
                break
        else:
            print("Conta corrente não encontrada!")

    elif opcao == "5":
        numero_conta = int(input("Digite o número da conta corrente: "))
        for conta in contas:
            if conta.numero == numero_conta:
                conta.extrato(saldo=conta.saldo, extrato=conta.extrato)
                break
        else:
            print("Conta corrente não encontrada!")

    elif opcao == "6":
        listar_contas(contas)

    elif opcao == "0":
        break

    else:
        print("Opção inválida!")
