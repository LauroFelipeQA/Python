def soma( a=1 , b=1):
    return(a+b)


def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_sucessor(numero):
    numero_antecessor = numero -1
    numero_sucessor = numero +1
    return numero_antecessor,numero_sucessor

def carros(marca, modelo, ano):
    return(f"a marca: {marca}, o modelo: {modelo}, ano {ano}")

#forma de passar um dicionario pra uma função
print(carros(**{"marca": "Fiat", "modelo": "Palio", "ano": 2008}))

#passar por uma tupla

          
print(soma(3,4))
print(soma())
print(calcular_total([1,45,6,4,3]))
print(retorna_antecessor_sucessor(1))