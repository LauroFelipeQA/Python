#Compressão de listas, usar para filtros ou gerar um nova lista a partir de uma existente
numeros = [1,2,3,4,5,6,8,10,11,12,13,14,15,16,17,18,19,20]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero) #append adiciona o valor da iteração na outra lista

print(pares)

# AGORA COM COMPRESSAO

parescompressao = [numerocompressao for numerocompressao in numeros if numerocompressao % 2 == 0]
print(parescompressao)

#outro exemplos

lista_antes = [1, 30, 21, 2 , 9, 65, 34] # agora quero elevar ao quadrado in line
lista_pos = [valor ** 2 for valor in lista_antes]
print (lista_pos)

