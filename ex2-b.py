#Manipuler des listes et comprendre les structures de données.
#Créez une liste des dépenses marketing mensuelles et calculez les dépenses totales de l'année.



depenses_mensuelles = [1220, 1433, 907, 1174, 1398, 945, 755, 657, 888, 425, 358, 456]

depenses_annuelles = 0
for depense in depenses_mensuelles:
    depenses_annuelles += depense

print(f"Les dépenses mensuelles sont : {depenses_mensuelles}")
print(f"Les dépenses totales de l'année sont : {depenses_annuelles}")
