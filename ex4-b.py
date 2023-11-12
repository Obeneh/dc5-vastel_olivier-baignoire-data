#Comprendre comment écrire et utiliser des fonctions.
#Fonctions : Écrivez une fonction qui calcule le factoriel d'un nombre.

def calcul_factoriel(nombre):
    if nombre == 0 or nombre == 1:
        return 1
    else:
        fact = 1
        i = 2
        while i <= nombre:
            fact *= i
            i += 1
        return fact

nombre_utilisateur = int(input("Entrez un nombre pour calculer le factoriel : "))
resultat_factoriel = calcul_factoriel(nombre_utilisateur)
print(f"Le factoriel de {nombre_utilisateur} est : {resultat_factoriel}")
