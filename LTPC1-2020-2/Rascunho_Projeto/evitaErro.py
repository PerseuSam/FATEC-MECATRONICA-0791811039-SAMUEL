verificaNumero = True
while verificaNumero:
  valor = input("Gerar QR Code de qual valor? ")
  if valor.isdigit():
    valor = int(valor)
    verificaNumero = False
  else:
    print("Algo errado")
    print("Tente novamente")
