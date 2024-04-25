import textwrap

def menu():
    menu = '''\n
    ==============Menu===============
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [lc] Listar Contas
    [nu] Novo Usuario
    [q] Sair
    => '''
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques, /):
    excedeu_saldo = valor > saldo
    LIMITE_SAQUES = 3

    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def extrato(extrato, /):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)

def nova_conta(contas, /):
    numero_conta = len(contas) + 1
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    contas[numero_conta] = (saldo, limite, extrato, numero_saques)
    print(f"Conta {numero_conta} criada com sucesso.")
    return contas

def listar_contas(contas, /):
    print("\n================ CONTAS ================")
    for numero_conta, (saldo, limite, extrato, numero_saques) in contas.items():
        print(f"Conta: {numero_conta}")
        print(f"Saldo: R$ {saldo:.2f}")
        print(f"Limite: R$ {limite:.2f}")
        print(f"Saques: {numero_saques}")
        print()

def novo_usuario(usuarios, /):
    nome = input("Informe o nome do usuário: ")
    cpf = input("Informe o CPF do usuário: ")
    usuarios[cpf] = nome
    print(f"Usuário {nome} cadastrado com sucesso.")
    return usuarios

def main():
    contas = {}
    usuarios = {}

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            conta = int(input("Informe o número da conta: "))
            saldo, limite, extrato, numero_saques = contas[conta]
            saldo, extrato = depositar(saldo, valor, extrato)
            contas[conta] = (saldo, limite, extrato, numero_saques)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            conta = int(input("Informe o número da conta: "))
            saldo, limite, extrato, numero_saques = contas[conta]
            saldo, extrato, numero_saques = sacar(saldo, valor, extrato, limite, numero_saques)
            contas[conta] = (saldo, limite, extrato, numero_saques)

        elif opcao == "e":
            conta = int(input("Informe o número da conta: "))
            saldo, limite, extrato, numero_saques = contas[conta]
            extrato(extrato)

        elif opcao == "nc":
            contas = nova_conta(contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "nu":
            usuarios = novo_usuario(usuarios)

        elif opcao == "q":
            break

        else:
            print("Opção inválida! Tente novamente.")

# Call the menu function at the beginning of main
menu()
main()
