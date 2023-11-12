#Parcourir la liste des clients et afficher ceux qui ont dépensé plus de 100€.

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
    if client["montant_depense"] > 100:
        print(client)
