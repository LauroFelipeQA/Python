#Tuplas é imutável, usamos parenteses para declarar que é tupla

lauro = ["Lauro", "Felipe"]
laurotupla = ("Lauro", "Felipe",)
print(laurotupla)

matrizTupla = (
    (1,2,3),
    (4,5,6),
    (7,8,9)
)

print(matrizTupla[::])

carros = ("gol")
print(isinstance(carros, tuple))