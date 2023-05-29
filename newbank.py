menu = f"""
    Bem vindo(a) ao Banco BeBank! Como podemos te ajudar hoje?

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    =>"""

saldo = 0
Limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:


    opcao = input(menu)

    if opcao == "d":
        valor = float(input("\nInforme o valor desejado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}\n"
            print("\nDepósito realizado com sucesso. Consulte Extrato para saber o saldo atual!")

        else:
            print("\nOperação falhou! O valor informado é inválido. Tente novamente")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > Limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\nOperação falhou! Você não tem limite suficiente.")
        
        elif excedeu_limite:
            print("\nOperação falhou! O valor do saque excede o valor do limite diário para saque")

        elif excedeu_saques:
            print("\nOperação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("\nSaque realizado com sucesso. Consulte Extrato para saber o saldo atual!")

        else:
            print("\nOperação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n ====================Extrato====================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print (f"\nSaldo: R$ {saldo:.2f}")
        print("\n ======================FIM======================")

    elif opcao == "q":
        break

    else:
        print("Opção inválida, por favor selecione novamente a operação desejada:")

