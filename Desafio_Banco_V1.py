menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[s] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == "2":
        valor = float(input("Informe o valor que você gostaria de sacar: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não possui saldo suficiente para realizar essa operação.")
        
        elif excedeu_limite:
            print("Você não tem limite saldo suficiente para realizar essa operação.")
        
        elif excedeu_saques:
            print("O número máximo de saques foi atinguido. Não é possível realizar essa operação.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor: .2f}\n"
            numero_saques += 1

        else:
            print("Falha na operação. Ovalor informado é inválido.")
    
    elif opcao == "3":
        print("\n====================== EXTRATO ======================")
        print("Não foram realizadas movimentações na conta bancária." if not extrato else extrato)
        print(f"Saldo: R$:{saldo: .2f}")
        print("=======================================================")

    elif opcao == "s":
        break

    else:
        print("Opção inválida, por favor, selecione novamene a operação desejada.")
        