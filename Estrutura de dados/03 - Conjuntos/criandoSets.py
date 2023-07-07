# Não aceita elementos repetidos, porém ele não garante a ordem, usar o set ou {}... não aceita indexação e fateamento

numero = set([1, 2,3,1,3,4])
palavra = set("abacaxi")
palavra_2 = set("Morango")
lista = set(("Lauro", "Mateus", "Lauro"))

print(numero, palavra, lista)

#conjuntos
linguagens = {"Python", "java", "Python"}
print(linguagens)
#para ter acesso precisa converter o set para uma lista

listaa = list(linguagens)
print(listaa[0])

for ind, lis in enumerate(lista):
    print(f"{ind} : {lis}")

print(numero.union(palavra)) # uniao de conjuntos
print(palavra.intersection(palavra_2)) # intersecçao de conjuntos
print(palavra.difference(palavra_2)) # diferença de conjuntos
print(palavra.symmetric_difference(palavra_2)) #tudo menos o que esta na intersecção
print(palavra.issubset(palavra_2)) # se esta contido em um conjunto, retorno boleano, pensa no conjunto A abaixo do B
print(palavra.issuperset(palavra_2)) # retorno boleano, pensa no conjunto A acima do B
print(palavra.isdisjoint(palavra_2)) # retorno boleano se está fora um do outro
#tem o ADD, CLONE, discard, POP TIRA O VALOR DA FRENTE E NAO O ULTIMO, REMOVE igual ao discard, porém discard não da erro caso nao exista o valor
palavra_2.discard("a")
palavra_2.add("c")
print(palavra_2)