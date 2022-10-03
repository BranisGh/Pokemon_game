from Dresseur import *
import pickle
from Pokemon import *

""" 
>>>>On a fait le choix de deviser les deux fichier optionAndDataBase et le fichier de FonctionsUtiles 
    ou on a rassembler toutes nos fonction qu'on a utiliser et que nous semblent utiles et qui n'appartient
    a aucune classe afin d'éviter des erreures d'importations entre les differents fichiers et qu'on a 
    rencontrer durant notre projet     ## Importations circulaires (cycliques) ##

>>>> pour ce projet on a crée une Data Base qui stocke les dresseurs dont on auras le choix de charger un 
     dresseur déja stocké par la fontion fileDresseurToListe (pour afficher nos dresseures en premier lieu 
     puis de choisir Un), ou de crée un nouveau puis l'enregistrie grace a la fonction enregistrement 
     ainsi pouvoir supprimer un dresseur 

     >>> chaque dresseur est représenté par son nom sela dit il y'auras pas 2 dresseurs qui ont le meme nom

>>>> on a implémenter une option de transformation qui est pour but d'évolution d'un pokemon a un autre
    pokemon plus performant (plus de compétence et plus puissant)  
"""


def enregistrement(dresseur, nomFichier):
    """
    cette fonction prend en parametre un dresseur est le stocke dans une basse de données (fichier.txt)
    """
    list_dresseurs = []
    if isinstance(dresseur, Dresseur):
        file = open(nomFichier, 'rb')
        list_dresseurs = pickle.load(file)

    # pour enregistrer un dresseur deja enregistrer (present dans la liste des dresseurs) on le remplace directement
    try:
        for d in list_dresseurs:
            if d.nom == dresseur.nom:
                list_dresseurs.remove(d)
        list_dresseurs.append(dresseur)
        with open(nomFichier, 'wb') as fh:
            pickle.dump(list_dresseurs, fh)

    # sinon on l'ajoute directement a notre liste des dresseurs
    except:
        with open(nomFichier, 'wb') as fh:
            pickle.dump(list_dresseurs, fh)

        print(f"le dresseur {dresseur.nom} est bien enregistrer {emoji.emojize('✔')}")
        return True  # enregistrement reussit
    print(f"La variable passée en parametres n'est pas de type dresseur {emoji.emojize('🚫')}")
    return False  # enregistrement non reussit


def supprimerDresseur(indice):
    """
    cette fonction sert a supprimer un dresseur au choix dans notre base de données
    """
    file = open("dresseurs.txt", 'rb')
    list_dresseurs = pickle.load(file)
    list_dresseurs.remove(list_dresseurs[indice])
    with open('dresseurs.txt', 'wb') as fh:
        pickle.dump(list_dresseurs, fh)


def fileDresseurToListe(nomFichier):
    """
    cette fonction récupère un la liste des dresseurs stockés dans la DATA BASE (fichier.txt), et la retourn
    """
    try:
        with open(nomFichier, 'rb') as fh:
            dresseurs = pickle.load(fh)
    except:
        dresseurs = []
    return dresseurs


def creerDresseur(liste_pokemons):
    """
     cette fonction permet de cree un dresseur, elle prend en parametre une liste de pokemon. par defaut un dresseur doit
     avoir un dek (3 pokemon) et nom. pour ce fair on fait appel aux fonctions "choixDek", "demandeNom" et "pokemonToString"
    """
    indicesPokemons = [str(i + 1) for i in range(len(liste_pokemons))]  # recuperer les indices des pokemons
    print()
    print(f"* ETAPE 1 :")
    nom = demandeNom(f"  {emoji.emojize('👉')} Entrez votre nom : ")  # recuperer le nom du nouveau dresseur
    print()
    print(pokemonToString(liste_pokemons))  # affichage de la liste des pokemon
    print()
    print(f"* ETAPE 2: \nChoisisez votre DEK {nom.title()} (3 pokemons) ")
    dek = choixDek(indicesPokemons, liste_pokemons)  # recuperer le dek choisie dans la liste dek[]
    dresseur = Dresseur(nom, dek)  # cree le dresseur
    return dresseur


def transformation(pokemon, pokemons):
    """
    cette fonction prend en parametre un pokemon et la listes de tout les pokemons qui verifier d'abord si
    le pokemon peut se transformer ensuite le transformer a son apres ( sa forme apres l'évolution )
    car pas tous  peuvent se transformer.
    """
    if pokemon.peutTransformer():
        for pek in pokemons:
            if pek.nom == pokemon.apres:
                print(f"félicitation le pokemon {pek.nom} est transformer en {pokemon.apres}")
                return deepcopy(pek)

    # sinon pas de transformation
    else:
        return pokemon


def transDresseur(Dresseur, pokemons):
    """
    cette fonction permet parcourir tout les pokemons d'un dresseur et les transformer
    """
    for pokemon in Dresseur.listePokemon :
        transformation(pokemon, pokemons)
        #print("VOILA ICI ON APLIQUE UNE TRANSFORMATION")


def transJoueurs(joueurs, pokemons):
    """
        cette fonction permet parcourir tout les joueurs d'une championat et transformer leur pokemons
    """
    for joueur in joueurs:
        transDresseur(joueur, pokemons)
