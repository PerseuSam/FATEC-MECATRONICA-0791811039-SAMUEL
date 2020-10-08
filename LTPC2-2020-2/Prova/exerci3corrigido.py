temperaturas = []
continuar = True
while continuar == True:
  temperatura = int(input("Temperatura que deseja informar: "))
  temperaturas.append(temperatura)
  continuar = input("Deseja continuar (s/n)? ") == "s"

valor_limiar = int(input("Digite um valor limiar(média): "))
acima_da_media = []

for temperatura in temperaturas:
  if temperatura > valor_limiar:
    acima_da_media.append(temperatura)

percentual = (len(acima_da_media)*100)/len(temperaturas)
print("Percentual acima: ", percentual)

if percentual >= 20 and percentual <45:
  print("Dentro do esperado")
elif percentual >=45 and percentual <70:
  print("Acima do esperado")
elif percentual >=70 and percentual <100:
  print("Muitos valores acima do limiar")
else:
  print("Sem problemas aqui")

  
list.sort(temperaturas) 
print("Temperaturas: ", temperaturas)
print("Valor Limiar: ", valor_limiar)
print("Acima da média: ", sorted(acima_da_media))
