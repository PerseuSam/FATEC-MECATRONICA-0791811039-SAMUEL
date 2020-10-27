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
nome_completo = input("Vamos começar pelo seu nome, qual seu nome completo? ").split()
print("Olá", nome_completo[0],)

mail = input("Agora digite seu e-mail: ")

print("Estamos quase lá")

senha_0 = input("Digite uma senha: ")

