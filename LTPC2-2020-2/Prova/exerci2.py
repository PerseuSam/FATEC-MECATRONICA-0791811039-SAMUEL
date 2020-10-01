def ValoresAcimaDaMedia(lista):
  for valor in valores:
    if valor > valor_medio:
     acima_da_media.append(valor)

valores = []
acima_da_media = []
quantidade = int(input("Quantidade de valores: "))

while len(valores) < quantidade:
  valor = int(input("Informe um valor:"))
  valores.append(valor)

valor_medio = sum(valores) / len(valores)
ValoresAcimaDaMedia(valores)

print("Média: ", valor_medio)
print("Valores informados: ", sorted(valores))
print("Valores acima da média: ", sorted(acima_da_media))
