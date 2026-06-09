mot = input("Donne un mot : ")
nb_voyelles = 0
for lettre in mot:
 if lettre in "aeiouyAEIOUY":
     nb_voyelles = nb_voyelles + 1
print("Nombre de voyelles :", nb_voyelles)