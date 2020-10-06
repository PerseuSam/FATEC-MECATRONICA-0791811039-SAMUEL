continuar = True

T_ON = int(input("Informe o Tempo em nível alto (ms): "))
T = int(input("Informe o Período total do sinal (ms): "))
V_ON= int(input("Informe o valor de Tensão em nível alto (V): "))

V_out = (T_ON/T)*V_ON
print(V_out, "V")

while continuar == True:
  if input("Deseja continuar (s/n)? ") == "s":
    continuar = True
  else:
    continuar = False
  break

  T_ON = int(input("Informe outro Tempo em nível alto (ms): "))
  V_out = (T_ON/T)*V_ON
  print(V_out, "V")
