#Inicializção

print("Olá")
print("O que deseja hoje?")
print("Para adicionar usuário - Digite 1 ")
print("Para realizar transação - Digite 2")

continuar = True
opcao = 0

while continuar:
  opcao = input("Opção: ")
  if opcao == "1":
    print("Vamos lá")
    continuar = False
  elif opcao == "2":
    print("entrando")
    continuar = False
  else:
    print("Opção inválida, tente novamente")

#Opção 1

cliente = []

nome_completo = (input("Vamos começar pelo seu nome, qual seu nome completo? ").title()).split()
print("Olá", nome_completo[0].title())

e_mail = input("Agora digite seu e-mail: ")

print("Estamos quase lá")

senha = input("Digite uma senha: ")

cliente.append(nome_completo)
cliente.append(e_mail)
cliente.append(senha)

print(cliente) #print(" ".join(nome_completo)) #QAUNDO PRECISAR MOSTAR O NOME INTEIRO SEM SEPARAÇÃO

