""" # # # # # # # # # # # # # # # # # # #
    #            CLASSE DRESSEUR        #
    # # # # # # # # # # # # # # # # # # # """

from optionAndDataBase import *
from copy import deepcopy         # copie profonde
import emoji                      # bibliotheque d'emoji (faut installer)
from fonctionsUtiles import *
from Pokemon import Pokemon


class Dresseur:
    # Declaration des constructeurs
    # Constructeur "normal", tous les attributs sont connus
    def __init__(self, nom, dek):
        self.nom = nom         # appelle du setter
        # déclaration et initialisation de la liste des pokemones capturés par le Dresseur
        self.__listePokemon = []
        # copie profonde des pokemons passés en parametres (par defaut un Dresseur possède un dek)
        self.__listePokemon = [deepcopy(pokemon) for pokemon in dek]

    # Surchage de l'operateur d'affichage
    def __str__(self):
        """
        cette méthode returnant le nom du Dresseur ainsi que tous les pokemons qui a capturé
        """
        s = f"{self.who()} : {self.nom} \n"
        s += self.listeDesPokemonsCaptures()
        return s

    # surcharge de l'operateur d'egalité
    def __eq__(self, other):
        """
        On surchage l'operateur d'égalité car on sera mener à tester plus tard dans d'autre classe l'egaliter entre des
        dresseur (ex : stocher deux dresseur, il faut d'abord verifier si ce d'érnier existe deja dans la base de donnée.
        Dans notre cas on considère deux dresseurs egaux si selement ils possèdent le meme nom.
        """
        if not isinstance(other, Dresseur): return False
        if self is other: return True
        if self.nom != other.nom: return False
        return True

    # 4) Déclaration des méthodes
    def who(self):
        """
        cette méthode returnat le type de l'objet sous forme de String, ici "Dresseur"
        """
        return "DRESSEUR"

    def capturerPokemon(self, pokemon):
        """
         une méthode capturerPOOkemon(pokemon), permettant au Dresseur de capturer un Pokemon.
         capturer Pokemon <==> Ajouter un Pokemon à la liste des Pokemons capturée
         retourn (true), si la capture a réssit, (false) si non
        """
        if isinstance(pokemon, Pokemon):
            if not (pokemon in self.listePokemon) :  # on peut pas avoir deux meme pokemon pour un meme dressseur
                self.listePokemon.append(pokemon)
                print(f"{self.nom} vous avez bien reussi à capturer {pokemon.nom} {emoji.emojize('✔')}")
                return True   # capture du pokemon réussite
            else :
                print(f"{pokemon.nom} est deja present dans la liste des pokemos de {self.nom.title()}, impossible de "
                      f"de le capturer {emoji.emojize('🚫')}")
                return False  # capture du pokemon echouée
        print(f"Erreur la variable passee en parametre elle est de type ({type(pokemon)}) {emoji.emojize('🚫')}")
        return False # capture du pokemon réussite

    def listeDesPokemonsCaptures(self):
        """
        cette méthode permet de d'afficher les Pokemons capturés par le Dresseur,
        ainssi que leurs caracteristiques (attributs)
        """
        s = self.dekToString()
        s += "\n" + self.listePokemonsRemplacantsToString()
        return s

    def nombreDePokemonsCaptures(self):
        """
        cette méthode return le nombre de POOkemon capturés par le Dresseur
        """
        return len(self.listePokemon)

    def chagerPostionDesPokemon(self, i, j):   # méthode privé elle ne sera pas utliser en dehors de la classe Dresseur
        """
        cette fonction nous permet de changer de postion entres POOkemon, elle nous sera utile pour le changement
        de dek, cette méthode elle ne sera pas utilisabel par le programmeur utlisateur, donc le mieux est de la declarer
        comme méthode privée
        """
        self.listePokemon[i], self.listePokemon[j] = self.listePokemon[j], self.listePokemon[i]

    def dekToString(self):
        """
        Cette méthode retourn le dek d'un dresseur (les 3 premier pokemons de sa liste) sous forme de String
        """
        s = "Voici votre dek " + self.nom.title() + "\n"
        for i, pokemon in enumerate(self.listePokemon[:3]):
            s += "\n" + str(i + 1) + "/ "
            s += pokemon.__str__()
        return s

    def pokemonsDekVivantsToString(self):
        """
        Cette méthode retoune les pokemon vivants du dek d'un dresseur, elle nous sera utile pour le deroulement
        du combat, car on sera mener a fair un choix d'un pokemon pour combatre et in est obligatoirement que dernier
        soit vivant!
        """
        s = "Voici vos pokemons prets à combattre " + self.nom.title()
        for i, pokemon in enumerate(self.listePokemon[:3]):
            # j'affiche mon pekemon si il n'est pas KO
            if not pokemon.estKo():
                s += "\n" + str(i + 1) + "/ "
                s += pokemon.__str__()
        return s

    def listeIndicesPokemonsVivants(self) :
        """
        cette méthode retourn une liste de string comporatant les indices des pokemons (vivants) qui peuvent combattres
        elle sera utlisier pour afficher le menu qui propose le choix des pokemons qui peuvent combattres
        """
        liset_indices = []
        for i, pokemon in enumerate(self.listePokemon[:3]):
            # je recupère l'indice de mon pokemon si ce dernier est vivant
            if not pokemon.estKo() :
                liset_indices.append(str(i + 1))
        return liset_indices

    def listePokemonsRemplacantsToString(self):
        """
        cette fonction retourn la liste des pokemon remplacants sous forme de String
        """
        if(len(self.listePokemon) <= 3) :
            s = "Vous n'avez pas de Pokemons remplacants"
        else:
            s = "Voici vos Pokemons remplacants " + self.nom.title() #+"\n"
            for i, pokemon in enumerate(self.listePokemon[3:]):
                s += "\n"+str(i + 4) + "/ "
                s += pokemon.__str__()
        return s

    def changerDek( self ):
        """
        cette méthode permet au Dresseur de changer son dek. On remplassant
        les pokemon de son encien dek par les pokemons (de la liste des pokemones capturés)
        """
        # cette liste comporte les indices du dek sous forme de String
        liste_choix_dek = [str(i+1) for i in range(3)]
        # cette liste comporte les indices des pokemons remplacants sous forme de String
        liste_choix_remplacants = [str(i+1) for i in range(3, self.nombreDePokemonsCaptures())]

        # si on a des pokemon remplacant
        if len(liste_choix_remplacants) > 0 :
            menuDek = self.dekToString() + f"\n   {emoji.emojize('👉')} Quel Pokemon voulez-vous changer ? (1 - 3) : "
            menuRemplacants = self.listePokemonsRemplacantsToString() + f"\n   {emoji.emojize('👉')} Quel Pokemon voulez-vous ajouter ? (4 - " + str(len(self.listePokemon)) + ")"

            print("Changement de dek".title() + " pour le " + self.who() + " : " + self.nom)

            print("-------------------------")
            choix_dek = saisieChoix(menuDek, liste_choix_dek) - 1
            choix_remplacant = saisieChoix(menuRemplacants, liste_choix_remplacants) - 1
            print()

            self.chagerPostionDesPokemon(choix_remplacant, choix_dek)
            return True # le changement de dek est reusit
        print(f"{self.nom}, vous n'avez aucun Pokemon remplacant! {emoji.emojize('🚫')}")
        return False # le chagement de dek n'est pas efectuer car il n'existe de pokemon remplaca,ts


    def choixPokemon( self ) :
        """
        cette méthode retourn un pokemon choisie par le joueur, (pour combatre)
        """
        # récuperer la liste des indice des pokemon vivant dans une liste
        liste_indices = self.listeIndicesPokemonsVivants()

        # récupérer la liste des indice des pokemon vivant en chaine de caractères pour l'ffichege
        listeIndice2Str = '-'.join(liste_indices)

        # récuperer le String comporatant les pokmeons vivants dans "menu"
        menu = f"""{self.pokemonsDekVivantsToString()} \n    {emoji.emojize('👉')} {self.nom} Quel pokemon voulez vous utiliser ? ({listeIndice2Str})"""#{min(liste_indices)}-{max(liste_indices)}"""
        choix_pokemon = saisieChoix(menu, liste_indices) - 1

        # ici, on s'assure de mettre le pokemon choisie (pour combatre) à la première place de la liste
        # ca facilite la conseption de l'algorithme de combat insi que l'affichage
        if not choix_pokemon == 0 :         # si le pokemon choisi n'est pas à la première position de la liste
            self.chagerPostionDesPokemon(0, choix_pokemon)
        return self.listePokemon[0]        # toujour on combat avec le premier pokemon de la liste

    def niveauMoyenDuDek(self):
        """
        cette méthode retourne la valeur moyenne du niveau des pokemon dec du dresseur
        """
        niveauMoy = 0
        # parcourir les 3 prmiesr pokemons de la liste
        for pokemon in self.listePokemon[:3] :
            niveauMoy += pokemon.niveauActuelle
        return niveauMoy / 3


    def bonusDekganantJCP(self, pokemonPerdant): # si pokemon adverse est KO
        """
        ctte méthode récomponse tous les pokemons du dek, en leurs ajoutant des bonus pour
        (experience, niveau, energie, energie, resistance) pour le combat JCP
        cette méthode sera utiliser à la fin du combatJCP et si le dresseur à gagnié bien sur
        """
        for i in range(3) : # elle sera utilisé dans le cas ou le pokemon est Ko mais pas quand le pokemon est capturer
            # recuperer le ième pokemon du dek
            pokemon = self.listePokemon[i]
            pokemon.experience += round(10 + pokemonPerdant.niveauActuelle - pokemon.niveauActuelle) / 3
            # si le pokemon passse au niveau superieru alors on le récopence avec les bonnus suivant
            if pokemon.passeAuNiveauSuperieur():
                pokemon.bonusNiveau()
                pokemon.bonusEnergie()
                pokemon.bonusVie()
                pokemon.bonusResistance()

    def bonusDekganantJCJ(self, dresseurPerdant):  # dresseur1 gagnant et dreseur2 pérdant
        """"
        ctte méthode récomponse tous les pokemons du dek, en leurs ajoutant des bonus pour
        (experience, niveau, energie, energie, resistance) pour le combat JCJ
        cette méthode sera utiliser à la fin du combatJCJ pour le dresseur gagant
        """
        # d'abord on recupère le dresseur gagnant
        if  isinstance(dresseurPerdant, Dresseur) :
            for i in range(3):
                # recuperer le ième pokemon du dek
                pokemon = self.listePokemon[i]
                pokemon.experience += int(10 + dresseurPerdant.niveauMoyenDuDek() - pokemon.niveauActuelle)
                if pokemon.passeAuNiveauSuperieur() :
                    pokemon.bonusNiveau()
                    pokemon.bonusEnergie()
                    pokemon.bonusVie()
                    pokemon.bonusResistance()
        else :  print(f"La v passée en parametre n'est pas de type dresseur {emoji.emojize('🚫')}")

    def miseAJour(self):
        for i in range (3):
            self.listePokemon[i].miseAJour()

    def transformationPokemonDeDresseur(self, pokemons):
        for i in range (len(self.listePokemon)):
            self.listePokemon[i] = transformation(self.listePokemon[i],pokemons)

    # Déclaration des getters et les setters

    # Déclaration des getters
    @property
    def nom(self):
        # le nom du dresseur est privé
        return self.__nom

    @property
    def listePokemon(self):
        # la liste des pokemon du dresseur est privée
        return self.__listePokemon

     # déclaration des setters
    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    """
    Ici, on a fait le choix de ne pas mettre de settre pour liste pokemon, car si on souhaite modifier la liste des pokemons captures
    on le ferra avec la methode (capturerPokemon()), elle ne seras gamais modifier autrement!
    """

