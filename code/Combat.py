from Dresseur import Dresseur
from Pokemon import Pokemon
import emoji
from abc import ABC, abstractmethod


class Combat(ABC) :
    # Déclaration du constructeur
    def __init__(self, dresseur) :
        # ici, on à fait le choix
        self.dresseur = dresseur
        # tous les combats en un score, il sera representer comme un vecteur de 2 element, score[alement1, element2]
            # element1 : nombre de victoires du joueur 1
            # element2 : nombre de victoires du (joueur 2 ou pokemon 2) autrement dit (joueur advers ou pokemon advers)
            # au départ le score est initialisé a zero, donc [0, 0]
        self.__score = [0, 0]
        # un combat et caractèriser par un round
        self.round = 0   # au debut du combat, le round est à 0
        # un combat et caractèriser par un tour car le combat sera realisé, en tour par tour
        self.tour = 0   # au debut, le tour est à 0
        # cette atribut vaut :
            # 0 si aucun des joueurs/pokemon à fuit le combat
            # 1 si le jouer1 (dresseur1) a fuit le combat
            # 2 si le jouer2 (dresseur2 ou pokemon2) a fuit le combat
        self.aFuit = 0  # au depart aucun des joueurs/dresseus n'a fuit le combat

    @abstractmethod
    def __str__(self): pass

    def affichageScoreVie(self) :
        """
        cette méthode affiche le scors du combat pendant les tours
        """
        # recuperer le pokemon de la prmière liste du dresseur (pokemon qui combat à l'instant)
        pokemon = self.dresseur.listePokemon[0]
        if isinstance(pokemon, Pokemon) :
            s = "SCORE Vie:"
            s += f"\n  * {pokemon.nom}: {int(pokemon.vieActuelle * 100 / pokemon.vieReference)} % {emoji.emojize('🧪')}"
            print(s)  # affichege du score



    def menu(self, pokemon):
        """
        cette méthode retourn un menu comportant des choix à faire lors d'un combat, on a crée se menu pour qu'il
        s'addapte du magnière dynamique au pokemon passé en parametre, car tous les pokemon n'ont pas les meme caracteriques
        """
        # recuperer le nombre de competence total des deux pokemon
        nbCompetencePokemon = pokemon.nbCompetenceTotal()

        # recuperer la liste des competence des deux pokemon
        listeCompetencePokemon = pokemon.listeDesCompetenseToString()

        # initialiser les numero des choix possible du menu dans une liste de String
        listeChoix = [str(i) for i in range(1, nbCompetencePokemon + 4)]

        s =  f"{listeCompetencePokemon}\n{nbCompetencePokemon + 1}/ Changer de pokemon"
        s += f"\n{nbCompetencePokemon + 2}/ Passer votre tour"
        s += f"\n{nbCompetencePokemon + 3}/ Fuir le combat"
        s += f"\n   {emoji.emojize('👉')} Que voulez vous faire ? (1-{nbCompetencePokemon+ 3})"
        return  s

    def miseAJourCombat(self) :
        # remise à zero du score
        self.score = [0, 0]
        self.score = [1, 0]
        # remise à zero do round
        self.round = 0
        # remise à zero du tour
        self.tour = 0
        # remise a zéro de aFuit
        self.aFuit = 0

    def miseAJourTour(self):
        # remise à zero du tour
        self.tour = 0

    @abstractmethod
    def gagnant (self) : pass

    @abstractmethod
    def perdant(self) : pass

    # # Déclaration des méthode
    # @abstractmethod
    # def who(self):
    #     """
    #     Cette méthode retourn le type de l'instance, ici on la déclarer abstraite car on ne souhaite pas crée
    #     des instance de type (Combat), mais elle sera redefinie d'une magnère polymorphqie dans les sous classe de combat
    #     """
    #     pass

    # Déclaration des getters et les setters

    # Les getters
    @property
    def dresseur(self):
        # un dresseur est declarer privé dans une instance combat
        return self.__dresseur

    @property
    def score(self):
        # le score d'un combat est déclarer privé
        return self.__score

    @property
    def round(self):
        # le round est declarer privé dans un combat
        return self.__round

    @property
    def tour(self):
        # le tour est declarer privé dans un combat
        return self.__tour

    @property
    def aFuit(self):
        # aFuir est declaré privé dans un combat
        return self.__aFuit

    @dresseur.setter
    def dresseur(self, dresseur):
        # d'abord s'assurer que le dresseur passé en parametre et de type dresseur
        # on retourn True si l'affectation est réussite, si non False
        if isinstance(dresseur, Dresseur) :
            self.__dresseur = dresseur
            return True
        # si l'affectation à échoiée !
        print(f"Erreur! la variabe que vous avez passez en parametre est de type {type(dresseur)}")
        return False

    @score.setter
    def score(self, indice_score):
        # on passe en parametres un vecteur de 2 element
            # element 1 : indice du  vecteur score[]
            # element 2 : la valeur affectée au score, (la nouvelle valeur)
        self.__score[indice_score[0]] = indice_score[1]

        # le score et compris entre [0, 3]
        if self.__score[indice_score[0]] > 3:
            self.__score[indice_score[0]] = 3
            return False
        elif self.__score[indice_score[0]] < 0:
            self.__score[indice_score[0]] = 0
            return False
        return True

    @round.setter
    def round(self, round):
        self.__round = round
        # un round ne peut pas etre negatif
        if self.__round < 0 : self.__round = 0

    @tour.setter
    def tour(self, tour):
        self.__tour = tour
        # un tour ne peut pas etre negatif
        if self.__tour < -1: self.__tour = 0

    @aFuit.setter
    def aFuit(self, aFuit):
        self.__aFuit = aFuit






