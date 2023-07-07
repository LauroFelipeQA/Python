
saldo = 0.0
extrato = ""
quantidadeSaque = 0

menu = """ 

    Olá usuário, bem vindo! Digite:

    1 - Para depositar
    2 - Para sacar  
    3 - Extrato
    4 - Para sair

Escolha: """

def depositar():
    valorDeposito = float(input("Qual o valor deseja depositar?\n"))
    if valorDeposito> 0:
        global saldo = valorDeposito
        extrato += f"Deposito realizado no valor de R$ {valorDeposito:.2f}.\n"
    else:
        print("Valor negativo, escolha novamente a aperação \n")

def sacar():
    valorSaque = float(input("Qual o valor deseja sacar?\n"))
    if(saldo>= valorSaque):
        if quantidadeSaque < 3:
                
            quantidadeSaque += 1
            print(f"Já realizou {quantidadeSaque} saques de 3 diarios.\n")
            saldo -= valorSaque
            extrato += f"Saque no valor R${valorSaque:.2f} realizado.\n"

        else:
            print("Já realizou a quantidade máxima de saques diarios.\n")

    else:
        print("Saldo insuficiente\n")

def extrato():
    cabecalho = " EXTRATO "
    print(f"""
    {cabecalho.center(20,"#")}

    {extrato}
    SALDO: R$ {saldo}.\n
    """)

while True:
    #ESCOLHER OPÇÂO DO MENU
    opcao = int(input(menu))
    
    #DEPOSITAR
    if(opcao == 1):
        depositar()

    #SACAR
    elif(opcao == 2):
        sacar()
        
    #EXTRATO
    elif opcao == 3:   
        extrato()

    #SAIR
    elif opcao == 4:
        break
    else:
        print("Tente novamente!")