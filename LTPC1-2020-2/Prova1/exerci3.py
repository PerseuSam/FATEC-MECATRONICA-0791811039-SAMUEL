numeros = []

continuar = True

while continuar == True:
  numero = int(input("Informe um número: "))
  numeros.append(numero)
  if input("Deseja continuar (s/n)? ") == 's':
    continuar = True
  else:
    continuar = False

valor_medio = sum(numeros)/len(numeros)
print("Valor médio: ",valor_medio)
