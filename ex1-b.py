#Manipulation de chaînes : Demandez à l'utilisateur de saisir une phrase, 
#puis affichez la phrase en majuscules, en minuscules et le nombre de mots

chain_user = input("Donnez votre chaîne de caractère : ")

def majuscule(chain_user):
    chain_majuscule =''
    for i in chain_user:
        if( 'a'<= i <= 'z'):
            chain_majuscule= ord(i) - 32
        else:
            chain_majuscule=chain_user
    print(f"La chaine majuscule c'est : {chain_majuscule}")

def minuscule(chain_user):
    chain_minuscule =''
    for i in chain_user:
        if('A' < i < 'Z'):
            chain_minuscule= ord(i) + 32
        else:
            chain_minuscule= chain_user
    print(f"La chaine majuscule c'est : {chain_minuscule}")

def nombre_mots(chain_user):
    nombre_mots=0
    in_word = False
    for i in chain_user:
        if ('A' <= i <= 'Z' or 'a' <= i <= 'z' or i in ['!', '?', 'à', 'é', 'è', 'ê', 'ë', 'î', 'ï', 'ô', 'ö', 'ù', 'û', 'ü']) and not in_word:
            in_word = True
            nombre_mots += 1
        elif not ('A' <= i <= 'Z' or 'a' <= i <= 'z' or i in ['!', '?', 'à', 'é', 'è', 'ê', 'ë', 'î', 'ï', 'ô', 'ö', 'ù', 'û', 'ü']):
            in_word = False
    print(f"Le nombre de mots est : {nombre_mots}")
# utilises les ranges dans ascii ils sont collés dans l'ascii
majuscule(chain_user)
minuscule(chain_user)
nombre_mots(chain_user)