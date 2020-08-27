#Usuário fala dois números e nós calculamos a média deles
numero1 = int(input("Número 1: "))
numero2 = int(input("Número 2: "))
media = (numero1 + numero2) / 2
#O "\n" faz pular uma linha quando ele está no meio da string
print("O resultado da média é: ", media)

#Exibindo diversas variavéis em uma saída
print (" média de", numero1, "com", numero2, "é igual a: ", media)
print("A média de %f com %i é: %f" %(numero1, numero2, media))
