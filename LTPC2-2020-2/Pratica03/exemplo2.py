#Quando utilizado =, é uma atribuição
numero_secreto = 32

palpite = int(input("Informe um palpite: "))

#Quando utilizamos ==, estamos fazendo uma pergunta
if palpite == numero_secreto:
  print("Acertou!")
elif palpite > numero_secreto:
      print("Chute um número menor!")
elif palpite < numero_secreto:
      print("Chute um número maior!")
