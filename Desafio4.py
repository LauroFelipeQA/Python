def main():
  n = int(input())
 
  total = 0
 
  for i in range(1, n + 1):
    pedido = input().split(" ")
    nome = pedido[0]
    valor = float(pedido[1])
    total += valor
  
  desconto = input()
  
  if desconto == "20%":
    totalAjustado = total * 0.8
  elif desconto == "10%":
    totalAjustado = total * 0.9
  print(f"Valor total: {totalAjustado: .2f}")
if __name__ == "__main__":
    main()