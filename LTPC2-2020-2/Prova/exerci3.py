temperaturas = []

continuar = True

while continuar == True:
  temperatura = int(input("Temperatura que deseja informar:"))
  temperaturas.append(temperatura)
  if input('Deseja continuar (s/n)?') == 's':
    continuar = True
  else:
    continuar = False

valor_limiar = int(input("Digite um valor limiar: "))

acima_da_media = []
for temperatura in temperaturas:
  if temperatura > valor_limiar:
    acima_da_media.append(temperatura)

percentual = (len(acima_da_media)*100)/len(temperaturas)

if percentual >= 20 and percentual <45:
  print("Dentro do esperado")
elif percentual >=45 and percentual <70:
  print("Acima do esperado")
elif percentual >=70 and percentual <100:
  print("Muitos valores acima do limiar")
else:
  print("Sem problemas aqui")

print("Temperaturas: ", temperaturas)
print("Valor Limiar: ", valor_limiar)
print("Acima da média: ", acima_da_media)
print("Percentual: ", percentual)
