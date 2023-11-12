#Comprendre comment écrire et utiliser des fonctions.
#Définissez une fonction pour convertir le CTR (Click-Through Rate) en pourcentage. Testez la fonction avec plusieurs entrées.

def calculer_ctr(views_total, clicks):
    if views_total == 0:
        return "Erreur : Le nombre total d'impressions ne peut pas être zéro."
    
    ctr = (clicks / views_total) * 100
    return ctr

views_total = float(input("Entrez le nombre total d'impressions : "))
clicks = float(input("Entrez le nombre de clics : "))
ctr_resultat = calculer_ctr(views_total, clicks)
print(f"CTR : {ctr_resultat}%")
