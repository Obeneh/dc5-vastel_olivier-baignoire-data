#Utiliser les instructions conditionnelles et les boucles.
#Écrivez un script qui détermine si une campagne a été rentable en comparant le coût de la campagne au revenu généré.

cout_campagne = float(input("Entrez le coût de la campagne : "))
revenu_genere = float(input("Entrez le revenu généré par la campagne : "))

# Vérification si la campagne est rentable
if revenu_genere > cout_campagne:
    print("La campagne a été rentable.")
elif revenu_genere == cout_campagne:
    print("La campagne a couvert ses coûts, mais n'a pas généré de profit.")
else:
    print("La campagne n'a pas été rentable.")