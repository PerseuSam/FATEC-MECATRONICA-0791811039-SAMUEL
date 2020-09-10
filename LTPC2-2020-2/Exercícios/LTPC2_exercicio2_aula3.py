#Calculo da Velocidade Média

posição_inicial = int(input("Informe a Posição Inicial, em metros(m): "))
posição_final = int(input("Informe a Posição Final, em metros(m): "))
tempo_inicial = int(input("Informe o Tempo Inicial, em segundos(s): "))
tempo_final = int(input("Informe o Tempo Final, em segundos(s): "))

Vm = (posição_final - posição_inicial) / (tempo_final - tempo_inicial)

print("A Velocidade Média é:", Vm,"m/s")
