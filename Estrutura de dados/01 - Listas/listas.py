# pode ser declarado direto com colchetes = [] ou = list()

carros = ["Ferrari", "Palio", 5, 1.9, True]

# percorrer a lista

for carro in carros:
    print(carro)
separador = "*"
print(separador.center(20,"*"))

print(carros[0])
print(carros[3]+carros[2])

# o metodo list espera receber um iteravel, e uma string é iteravel, então é quebrado cada letra para uma posição
letras = list("Lauro")
print(letras)

# argumento negativo

print(letras[-1])
print(letras[-3])

# fatiamento
print(letras[2:])
print(letras[2:-1])
print(letras[:-1])
print(letras[0:5:2])
print(letras[::-1])

# metodos da classe list
numeros = [1,2,2,2,5,6,8,10,11,12,13,14,15,16,17,18,19,20, "Casa", True]

# copiar a lista
print("copiando a lista numeros apra a lista listanova:")
listanova = numeros.copy()
print(id(listanova), id(numeros))

# contar quantas vezes algo aparece na lista
print("contando quantas vezes um elemento aparece na lista:")
print(numeros.count(2))

# adicionar mais de um item na lista
print("adicionando elementos com extend:")
numeros.extend(["Lauro", "Mateus"])
print(numeros)

# identificar o index de um objeto
print("Identificando onde ocorre a primeira ocorrencia do objeto Lauro")
print(numeros.index("Lauro"))

# usando o pop para remover um objeto pelo index
print("usando o pop para remover o lauro que é o indice 20:")
print(numeros.pop(20))
print(numeros)

# usando o remove para remover um objeto pelo argumento
print("usando o remove para remover o Mateus:")
print(numeros.remove("Mateus"))
print(numeros)

# Colocar a lista ao contrario
print("Colocando a lista ao contrario")
numeros.reverse()
print(numeros)

# limpar a lista
numeros.clear()
print("lista limpa usando o clear:")
print(numeros)

# Ordenar uma lista

linguagens = ["Java", "Python", "JS", "C#"]
linguagens.sort()
print(linguagens)
print("Por tamanho das palavras:")
linguagens.sort(key=lambda x: len(x))
print(linguagens)