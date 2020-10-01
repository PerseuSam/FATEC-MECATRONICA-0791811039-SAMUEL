valores = []

quantidade = int(input("Quantidade de valores: "))

while len(valores)<quantidade:
  valor = int(input("Valor: "))
  valores.append(valor)
  
valor_medio = sum(valores)/len(valores)

acima_da_media = []

for valor in valores:
  if valor > valor_medio:
    acima_da_media.append(valor)
    
print("Média: ", valor_medio)
print("Valores informados: ", sorted(valores))
print("Valores acima da média: ", sorted(acima_da_media))
