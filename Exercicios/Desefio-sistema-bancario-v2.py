def menu():
    print("""
    ------------ MENU -------------
    1 - depositar #TESTOK
    2 - sacar     #TESTOK  
    3 - extrato   #TESTOK
    4 - novo usuario 
    5 - nova conta
    6 - listar contas
    7 - sair
    """)
    opcao = int(input("Digito o número da sua opção: "))

    return opcao

def depositar(saldo, valor, extrato, /):
     
    if valor > 0:
        saldo += valor
        extrato += f"Deposito realizado no valor de R$ {valor:.2f}.\n"
        print("Depósito realizado com sucesso")
    else:
        print("Valor negativo, escolha novamente a aperação \n")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, numero_saques, limite_saques):
    
    if(saldo >= valor):
        if numero_saques < limite_saques:
                
            numero_saques += 1
            print(f"Já realizou {numero_saques} saques de 3 diarios.\n")
            saldo -= valor
            extrato += f"Saque no valor R${valor:.2f} realizado.\n"

        else:
            print("Já realizou a quantidade máxima de saques diarios.\n")

    else:
        print("Saldo insuficiente\n")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /,*,extrato):
    print(extrato)
    print(f"Seu saldo é: R$ {saldo}.")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF para cadastro: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("CPF existente no banco de dados")
        return
    
    nome = input("Qual o nome do usuário?")
    data_nascimento = input("informe a data de nascimento DD-MM-AAAA: ")
    endereco = input("Informe o endereço (Lagradouro, numero, bairro, cidade, estado)")

    usuarios.append({"nome": nome, "data_nacimento": data_nascimento,"endereco":endereco, "cpf": cpf})

def filtrar_usuario(cpf, usuarios):

    usuarios_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrado[0] if usuarios_filtrado else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF para cadastro: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Conta criada")
        return {"agencia": agencia, "numero_conta":numero_conta, "usuario": usuario}
    else: 
        print("O Usuario não foi encontrado, crie o usuário para criar a conta")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agencia: {conta['agencia']}
            Conta: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
        """
        print(linha)


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 1:
            valor = float(input("Qual valor deseja depositar? "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 2:
            valor = float(input("Qual o valor deseja sacar?\n"))
            saldo, extrato, numero_saques = sacar(saldo = float(saldo), valor = float(valor), extrato = extrato, numero_saques= numero_saques, limite_saques= LIMITE_SAQUES)

        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 4:
            criar_usuario(usuarios)

        elif opcao == 5:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            contas.append(conta)

        elif opcao == 6:
            listar_contas(contas)

        elif opcao == 7:
            break

        else:
            print("numero invalido, tente novamente: ")
main()