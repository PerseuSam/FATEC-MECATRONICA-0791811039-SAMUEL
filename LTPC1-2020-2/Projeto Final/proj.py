#Inicializção

clientes = [] #Tentar fazer isso com dicionário

print("Olá")
print("O que deseja hoje?")

programa = True
while programa:

  print("Para adicionar usuário - Digite 1")
  print("Para realizar transação - Digite 2")
  print("Para sair - Digite sair")

  continuar_1 = True
  opcao = 0

  while continuar_1:
    opcao = input("Opção: ")
    if opcao == "1":
      continuar_2 = True
      while continuar_2:
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
        clientes.append(cliente)

        continuar_2  = input("Adicionar mais algúem? (s/n)") == "s"

      print(clientes) ##Temporário
      print("tudo certo") ##Temporário
      continuar_1 = False

    elif opcao == "2":
      print("entrando")
      continuar_1 = False

    elif opcao == "sair":
      print("Até breve")
      continuar_1 = False
      programa = False

    else:
      print("Opção inválida, tente novamente")
