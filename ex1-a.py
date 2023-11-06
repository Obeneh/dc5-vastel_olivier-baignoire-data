#Créez des variables pour stocker le nom d'une entreprise, le nombre de clients et le revenu moyen par client. 
#Calculez et affichez le revenu total.

nom_entreprise=input("Le nom de votre entreprise est :")
nombre_client=int(input("Votre nombre de clients : "))
revenu_moy=int(input("Ce qu'ils vous rapportent en moyenne ?"))
total= nombre_client*revenu_moy

print(f"Le revenu total de {nom_entreprise} est de : {total}")