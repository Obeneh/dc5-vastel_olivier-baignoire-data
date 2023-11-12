#Manipuler des listes et comprendre les structures de données.
#Listes : Créez une liste de 10 nombres, trouvez le maximum, le minimum, et calculez la moyenne.

def trouver_maximum(liste):
    maximum = liste[0]
    for nombre in liste:
        if nombre > maximum:
            maximum = nombre
    return maximum

def trouver_minimum(liste):
    minimum = liste[0]
    for nombre in liste:
        if nombre < minimum:
            minimum = nombre
    return minimum

def calculer_moyenne(liste):
    somme = sum(liste)
    moyenne = somme / len(liste)
    return moyenne

liste_nombres = [42, 17, 8, 56, 23, 91, 34, 12, 75, 5]

maximum = trouver_maximum(liste_nombres)
minimum = trouver_minimum(liste_nombres)
moyenne = calculer_moyenne(liste_nombres)

print(f"La liste de nombres est : {liste_nombres}")
print(f"Le maximum est : {maximum}")
print(f"Le minimum est : {minimum}")
print(f"La moyenne est : {moyenne}")