#Listas dentro de um dicionário

Usuarios = {}
Usuarios[1] = "Carlos Augusto", "augusto.carlos@gmail.com", "2358"
Usuarios[2] = "Ana Carolina", "ana.carlo@gmail.com", "6752"
Usuarios[3] = "Igor Moraes", "imoraes.raes@gmail.com", "1374"


nome = input("Coloca um nome: ")


if nome in Usuarios[1]:
  print("Dahora")
else:
  print("Ruim")

print(Usuarios)
