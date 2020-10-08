 def funcao(lista):
  resposta = []
  media = sum(lista) / len(lista)
  for valor in lista:
    if valor > media:
     resposta.append(valor)
  return resposta

valores = []
quantidade = int(input("Quantidade de valores: "))
while len(valores) < quantidade:
  valor = int(input("Informe um valor:"))
  valores.append(valor)

print(funcao(valores))
