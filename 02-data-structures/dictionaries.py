annuaire = {
"Lucas": "0601020304",
"Anass": "0611223344",
"Sarah": "0655667788"
}
nom = input("Quel nom cherches-tu ? ")
if nom in annuaire:
 print("Numéro :", annuaire[nom])
else:
    print("Contact introuvable")