nombres = [12, 5, 8, 20, 3]
plus_grand = nombres[0]
for nombre in nombres:
    if nombre > plus_grand:
     plus_grand = nombre
print("Le plus grand nombre est :", plus_grand)