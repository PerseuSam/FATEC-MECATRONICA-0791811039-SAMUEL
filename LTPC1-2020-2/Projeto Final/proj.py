print("Olá")
print("O que deseja hoje?")
print("Para adicionar usuário - Digite 1 ")
print("Para realizar transação - Digite 2")

continuar = True
opcao = 0

while continuar:
  opcao = input("Opção: ")
  if opcao == "1":
    print("adicionando")
    continuar = False
  elif opcao == "2":
    print("entrando")
    continuar = False
  else:
    print("Opção inválida, tente novamente")
