def caixa_eletronico():
    saldo = 5000
    opcao = -1

    while opcao !=0:
            
        opcao = int(input("Como posso ajudar? Tecle: 1 - Sacar, 2 - Depositar, 3 - Verificar saldo: , 0 - Sair"))

        if opcao == 1:
            valor_saque = float(input("Qual valor deseja sacar? "))
            if valor_saque <= saldo:
                saldo -= valor_saque
                print("Valor sacado:", valor_saque, "Novo saldo:", saldo)
            else:
                print("Saldo insuficiente")
        
        elif opcao == 2:
            valor_deposito = float(input("Qual valor deseja depositar? "))
            saldo += valor_deposito
            print("Valor depositado, seu novo saldo é:", saldo)
        
        elif opcao == 3:
            print("Seu saldo é", saldo)
        else:
            print("Opção inválida. Tente novamente.")

    else:
        print("Obrigado!")

caixa_eletronico()
