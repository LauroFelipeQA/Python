valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())


totalHambugueres = valorHamburguer * quantidadeHamburguer
totalBebidas = valorBebida * quantidadeBebida
total = totalBebidas + totalHambugueres

troco = 0
if valorPago > total:
  troco = valorPago - total

print(f"O preço final do pedido é R${total: .2f}. Seu troco é R${troco: .2f}.")