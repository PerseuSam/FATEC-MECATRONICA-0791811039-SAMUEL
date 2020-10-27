#Inicializção

Usuarios = {
    "1": ["Carlos Augusto", "augusto.carlos@gmail.com", "2358"],
    "2": ["Ana Carolina", "ana.carlo@gmail.com", "6752"],
    "3": ["Igor Moraes", "imoraes.raes@gmail.com", "1374"]
}

Contas = {
    "1": 1000,
    "2": 250,
    "3": 3000
}  ##Colocar aqui os valores nas contas das pessoas

print("Olá")
print("Em que posso ajudá-lo hoje?")

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

                nome_completo = (input(
                    "\nVamos começar pelo seu nome, qual seu nome completo? ").
                                 title()).split()
                print("Olá", nome_completo[0].title())

                e_mail = input("Agora digite seu e-mail: ")

                print("Estamos quase lá")

                senha = input("Digite uma senha: ")

                cliente = []
                ID = len(Usuarios) + 1
                cliente.append(" ".join(nome_completo))
                cliente.append(e_mail)
                cliente.append(senha)
                valor = input("Insira um valor inicial: ")
                Usuarios[ID] = cliente
                Contas[ID] = valor
                print("\nUsuários")
                print("----------------------------------------------------------------------------")
                print(Usuarios)
                print("\nContas")
                print("----------------------------------------------------------------------------")
                print(Contas)
                #print(" ".join(nome_completo)) #QAUNDO PRECISAR MOSTAR O NOME INTEIRO SEM SEPARAÇÃO

                continuar_2 = input("\nAdicionar mais algúem? (s/n)") == "s"
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

    ##Transações começa aqui

    print(Usuarios)
    senha = input("Digite sua senha: ")
    if senha in Usuarios:
        print("senhas iguais, acesso liberado")

    nome_completo = input("Digite seu nome completo: ").title()


