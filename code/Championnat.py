""" # # # # # # # # # # # # # # # # # # #
    #        CLASSE Championnat         #
    # # # # # # # # # # # # # # # # # # # """


from abc import ABC, abstractclassmethod


class Championnat(ABC) : 
    
    # Déclaration du constructeur
    def __init__(self, joueur) :
        
        # la supper classe abstrecat (Championnat prend en parametre) un jouer :
            # on derrive de cette supper classe deux autre classe filles (ChampionnatJC/ChampionnatJCP)
            # ChampionnatJCJ prend en deuxième parametre une liste d'autre joueurs 
            # ChampionnatJCP prend en deuxième parametre une liste de pokemons
        self.joueur = joueur
        
        # Initialisation du tour des combat à 0
        self.__tour = 0
        
          # Initialisation de la liste des combat
            # une classe championnat possède une relastion de composition
            # un championnat crée lui meme c'est combat
        self.combats = []
        
    # Déclaration des méthodes
    @abstractclassmethod
    def who(self) : pass 
    
    
    # Déclaration des properties
    
    #Déclaration des getters
    @property
    def joueur(self) :
        return self.__joueur
    
    @property
    def tour(self) :
        return self.__tour
    
    @property
    def combats(self) :
        return self.__combats
    

    # Déclaration des setters

    @joueur.setter
    def joueur(self, joueur) :
        self.__joueur = joueur        

    
    @tour.setter
    def tour(self, tour) :
        self.__tour = tour
        
        # on ne peut pas avoire un nombre de tour négatif (mesur de sécurité)
        if self.__tour < 0 :self.__tour = 0   
    
    @combats.setter
    def combats(self, combats) :
        self.__combats = combats
    
        

