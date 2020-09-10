#Determina o valor da Posição Final

posição_inicial = int(input("Informe a Posição Inicial, em metros(m): "))
velocidade = int(input("Informe a Velocidade, em metros por segundo(m/s): "))
tempo = int(input("Informe o Instante de Tempo, em segundos(s): "))

Sf = posição_inicial + (velocidade * tempo)

print("A Posição Final é:", Sf,"m")
