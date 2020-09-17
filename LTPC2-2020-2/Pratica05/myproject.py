#Criar um log de temperaturas
#Ler N temperaturas
#Calcular a temperatura media
#Encontrar todas as temperaturas acima da media
#Encontrar a maior temperatura
#Encontrar a menor temperatura
#################################################################################

#Cria uma lista de temperaturas
temperaturas = []

#Permite adicionar uma quantidade temperaturas
quantidade = int(input("Quantidade de temperaturas que deseja informar: "))

#Adiciona as temperaturas
while len(temperaturas) < quantidade:
  temperatura = float(input("Temperatura: "))
  temperaturas.append(temperatura)

#Encontra a temperatura média
temperatura_media = sum(temperaturas)/len(temperaturas)

#Encontra temperaturas acima da média
temperaturas_acima_da_media = []
for temperatura in temperaturas:
  if temperatura > temperatura_media:
    temperaturas_acima_da_media.append(temperatura)

#Encontrar a maior temperatura
maior = max(temperaturas)

#Encontra a menor temperatura
menor = min(temperaturas)

#Mostra os resultados
print("Temperaturas informadas: ", temperaturas)
print("Temperatura Média: ", temperatura_media)
print("Temperaturas acima da média: ", temperaturas_acima_da_media)
print("Maior temperatura:", maior)
print("Menor temperatura:", menor)
