temperaturas = [34.5, 67.8, 89.7, 45.8, 23.45]

temp_media = sum(temperaturas)/len(temperaturas)

for temperatura in temperaturas:
  if temperatura > temp_media:
    print(temperatura)
