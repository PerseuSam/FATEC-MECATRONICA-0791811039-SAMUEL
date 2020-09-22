print("Fórmula de Bhaskara ax^2+bx+c")
a = float(input("Insira o valor de a: "))
b = float(input("Insira o valor de b: "))
c = float(input("Insira o valor de c: "))

delta = (b**2) - (4*a*c)

if delta < 0:
  print("Não possui raízes reais")

elif delta > 0:
  x1 = (-b + (delta**0.5)) / (2*a)
  x2 = (-b - (delta**0.5)) / (2*a)
  print("x1 = ",x1)
  print("x2 = ",x2)

else:
  x = (-b + (delta**0.5)) / (2*a)
  print("x = ",x)
