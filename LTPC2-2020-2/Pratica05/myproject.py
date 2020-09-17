temperaturas = []

quantidade = int(input("Quantidade de temperaturas que deseja informar: "))

while len(temperaturas) < quantidade:
  temperatura = int(input('Temperatura:'))
  temperaturas.append(temperatura)

print('Temperaturas informadas: ', temperaturas)

temperatura_media = sum(temperaturas)/len(temperaturas)
print("Temperatura Média: ", temperatura_media)

for temperatura in temperaturas:
  if temperatura > temperatura_media:
    print("Temperaturas acima da média: ", temperatura)

#Encontrar o maior Valor
maior = max(temperaturas)
print('Maior temperatura:', maior)

#Encontra o menor valor
menor = min(temperaturas)
print('Menor temperatura:', menor)
