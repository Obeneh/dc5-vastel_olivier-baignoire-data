#Structures de données - Listes et dictionnaires
#Objectif : Créer une liste de dictionnaires, où chaque dictionnaire contient des informations sur un client (nom, email, montant dépensé). Minimum 50 entrées

def creer_liste_clients():
    liste_clients = []
    i = 1
    while i <= 50:
        client = {"nom": f"Client{i}", "email": f"client{i}@example.com", "montant_depense": i * 100}
        liste_clients.append(client)
        i += 1

    return liste_clients

liste_clients_50 = creer_liste_clients()
for client in liste_clients_50:
    print(client)

