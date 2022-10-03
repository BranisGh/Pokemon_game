from copy import deepcopy
import emoji
""" 
ce fichier est pour but de rassembler toutes nos fonctions qui seront utiles a notre projet 
( optimisation du code)
"""
def saisieChoix(menu, liste_choix) :
    """
    cette fonction prend en parametre un menu et une liste comportant les indice des choix possible en parametre
    et retourn le choix de l'utilisateur, avec le choix de l'utlistateur copris entre [liste_choix[0], liste_choix[1]]
    """
    choix = ""
    while (len(choix) == 0) or (not choix.isdigit()) or (not choix in liste_choix):
        choix = input(menu)
        if (len(choix) == 0) or (not choix.isdigit()) or (not choix in liste_choix):
            print(f"Error de la saisie! {emoji.emojize('🚫')}")
            print("Reesayer")
            print()
    return int(choix)


def demandeNom(message) :
    """
    cette fonction demande le nom de l'utilisateur, et le rtourn .
    prend en parametre une chaine de caracteres (message)
    """
    nom = ""
    while not nom.isalpha() or len(nom) == 0 :
        nom = input(message)
        if not nom.isalpha() or len(nom) == 0 :
            print(f"Error de la saisie! {emoji.emojize('🚫')}")
            print("Reesayer")
            print()
    return nom.title()

def pokemonToString(pokemons) :
    """
    cette fonction prend en paramedte une liste de pokemon est retourn la méthode __str__() pour tous les pokemon
    dans la liste
    """
    # d'abord en vérifie si la liste passée en parametre est de type pokemon!
    if len(pokemons) < 1 :
        s = f"Vous n'avez pas de pokemon deja stokes {emoji.emojize('🚫')}"
    else :
        s = ""
        for i, pokemon in enumerate(pokemons) :
            s += f"\n{i + 1}/ {pokemon.__str__()}"
        #s += f"\n   ==> Quel pokemon voulez-vous choisir?"
    return s


def dresseurToString(dresseurs) :
    """
    cette fonction prend en paramedte une liste de dresseur est retourn la méthode __str__() pour tous les dresseur
    dans la liste
    """
    # d'abord en vérifie si la liste passée en parametre est de type dresseur!
    if len(dresseurs) < 1 :
        s = f"Vous n'avez pas de dresseur deja stokes {emoji.emojize('🚫')}"
    else :
        s = ""
        for i, dresseur in enumerate(dresseurs) :
            s += "-------------------------------------------------------------------------"
            s += f"\n{i + 1}/ {dresseur.__str__()}\n"
        #s += f"\n   ==> Quel pokemon voulez-vous choisir?"
    return s

def choixDek(indicePokemon, pokemons):
    """
    cette  fonction prend en parametres une liste de pokemon est une liste d'indice de ces derniès.
    permet a un utilisateur de choisir 3 pokemons de cette liste et de les retourner dans une liste
    """
    listeDesChoix = []
    dek = []
    # indice = 0
    for i in range(3):
        menu = f"    {emoji.emojize('👉')} pokemon numero {i+1} parmis cette liste : "
        indice = str(saisieChoix(menu, indicePokemon))
        while str(indice) in listeDesChoix :
            print(f"Vous ne pouvez pas avoir deux pokemons similaires! {emoji.emojize('🚫')}")
            print("resseyez")
            indice = str(saisieChoix(menu, indicePokemon))
        listeDesChoix.append(str(indice))
        dek.append(pokemons[int(indice) - 1])
    return dek


def choixIndice(liste_indice) :
    if len(liste_indice) > 0 :
        menu = f"    {emoji.emojize('👉')} saisze votre choix : "
        choix = saisieChoix(menu, liste_indice)
        return choix
    else :
        print(f"vous n'avez aucun dresseur sauvgardé {emoji.emojize('🚫')}")

def chargerDresseur(liste_dresseurs) :
    """
    cette fonction nous permet de choisir et récuperer un dresseur dans une liste de dresseurs passé en parametre
    """
    print(f"{emoji.emojize('📜')} voici la liste des dresseurs sauvgarder ")
    indicesDresseurs = [str(i + 1) for i in range(len(liste_dresseurs))]  # recuperer les indices des dresseurs
    print(f"{dresseurToString(liste_dresseurs)}")           # affichage des dresseurs deja de
    indice = choixIndice(indicesDresseurs)                  # recuperer l'indice du dresseur choisie
    return liste_dresseurs[(indice) - 1]                    # recuperer le dresseur choisie


def pokemonACombattre(liste_pokemons) :
    """
     cette méthode nous permet de choisir un pokemon advers lors d'un combaJCP, elle fait appel au fonction
     "choix indice" pour recupere l'indice du pokemon dans la liste passé en paramtre, et "deepcopy" pour cree
     recuperer et recuperer un pokimon similaire au choix que on a fait mais stocké dans une autre zone mémoire
    """
    indicesPokemons = [str(i + 1) for i in range(len(liste_pokemons))]  # recuperer les indices des pokemons
    i = choixIndice(indicesPokemons)                                    # recuperer l'indice du pokemon choisie
    return deepcopy(liste_pokemons[i - 1])                                    # recuperer le pokemon avec une copie profonde pour ne pas modifier

    # le comptenu de la liste des pokemon stokes dans la liste "pokemons"
    # print()
    # choisir le niveau de difficulté du combat [debutant, amateur, professionnel]
    # menu pour choisir le niveau de difficulté du combat

def niveauDifficulte() :
    """
    cette méthode nous permet de retourner le niveau de difficlter que on a choisie lors d'un combat JCP
    # 1 : debutant
    # 2 : amateur
    # 3 : professionnel
    """
    menuNiveau = f"1/ Debutant \n2/ Amateur \n3/ Professionnel \n   {emoji.emojize('👉')} Choisissez un niveau de difficulté : "
    # liste des indices des niveau possible
    niveau = saisieChoix(menuNiveau, ["1", "2", "3"])
    return niveau

def modeCombat() :
    """
    cette méthode nous permet de retourner le mode de combat que on a choisie lors d'un combat JCP
    # 1 : entrainement
    # 2 : capturer le pokemon
    """
    # choisir l'option capturer ou entrainement
    menuCapture = f"1/ Entrainement \n2/ Capturer le pokemon \n    {emoji.emojize('👉')} Choisisez un mode de combat : "
    capturer = saisieChoix(menuCapture, ["1", "2"])
    return (capturer - 1)

