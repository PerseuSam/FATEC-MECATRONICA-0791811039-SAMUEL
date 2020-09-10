#Determina qual a faixa do imposto de renda que o usuário deve pagar

salario = int(input("Informe um valor(R$):"))

if salario < 1903.98:
  print("Isento")

elif salario > 1903.99 and salario < 2826.65:
  aliquota = (salario * 7.5) / 100
  print("Parcela a deduzir do IRPF: R$", aliquota)

elif salario > 2826.66 and salario < 3751.05:
  aliquota = (salario * 15) / 100
  print("Parcela a deduzir do IRPF: R$", aliquota)

elif salario > 3751.06 and salario < 4664.68:
  aliquota = (salario * 22.5) / 100
  print("Parcela a deduzir do IRPF: R$", aliquota)

elif salario > 4664.68:
  aliquota = (salario * 27.5) / 100
  print("Parcela a deduzir do IRPF: R$", aliquota)
