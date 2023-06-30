numPedidos = int(input())

for i in range(1, numPedidos + 1):
  prato = input()
  calorias = int(input())
  ehVegano = False
  vegano = input()
  
  if vegano == "s":
    ehVegano = True
  
  while ehVegano:
    print(f"Pedido {i}: {prato} (Vegano) - {calorias} calorias")
    break
  else:
    print(f"Pedido {i}: {prato} (Nao-vegano) - {calorias} calorias")