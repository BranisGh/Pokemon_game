""" # # # # # # # # # # # # # # # # # # #
    #        CLASSE ChampionnatJCJ         #
    # # # # # # # # # # # # # # # # # # # """

from random import shuffle    
from CombatJCP import CombatJCP
from Championnat import Championnat
from fonctionsUtiles import *
from optionAndDataBase import *

class ChampionnatJCP(Championnat) :
    
    # Déclaration du constructeur
    def __init__(self, joueur, pokemons) :
        # appel au constructeur de la supper classe
        super().__init__(joueur)

        # self.pokemons et une liste 1D comporant les pokemons inscrits pout le championnat
        self.pokemons = pokemons
        
    # Déclaration des méthodes 
    def who(self) :
        """ cette méthode retourn le nom de la classe, ici (ChampionnatJCP)"""
        return "Championnat"
    
    
    def affichageCalendrier(self) :
        """
        cette méthode affiche le calendrier des combats, on l'utilise au début du championnat pour afficher
        tous les combats aui aura lieu
        """
        s =  "________________________________"
        for i in range(len(self.pokemons)) :
            s += f"\n|combat {i+1}| {self.joueur.nom}  vs   {self.pokemons[i].nom}"
            s += "\n________________________________"
        
        print(s)
    
    def reset(self) : 
        """
        cette méthode remet à zero le nombre de tour'
        """
        self.tour = 0

    
    def championnat(self) :

        # initialisation du nombre de victoires
        cpt = 0

        print(f"\n\nVoici le calendrier des combas du championnat")
        #print(f"Voici le calendrier des combats des (Tour {self.tour + 1})")
        self.affichageCalendrier()

        for i in range(len(self.pokemons)) :
            if len(self.pokemons)-1 == i :
                print(f"\n\n--------------   Combat final FIGHT ....   ------------------\n")
            else : print(f"\n\n--------------   Combat numero {i+1} FIGHT ....   ------------------\n")

            print()
            niveau = niveauDifficulte()  # recuperer le niveau de difficulté
            print()
            capturer = modeCombat()  # recuprrer le mode du combat capturer/entrainement
            print()

            combat = CombatJCP(self.joueur, self.pokemons[i], capturer, niveau)
            combat.combat()
            ganant = combat.gagnant()

            # si le joueur perd devant un seul pokemon ! le jeux s'arrete ( le joueur à perdu), on quitte le combat
            if ganant == self.pokemons[i]:
                print(f"{self.joueur.nom}, vous avez perdue aux combat numero {self.tour+1}  😓😞")
                break
            else :
                cpt += 1
                #print(f"vous aves remporté le combat numero {self.tour+1}  💪👊")
        self.tour += 1

        if cpt == len(self.pokemons) :
            print()
            print(f"Bravot!! {self.joueur.nom} vous avez remporté le championnat 🥇🏆")


    
    
    
    
    # Déclaration des properties
    
    #Déclaration des getters
    @property
    def pokemons(self) :
        return self.__pokemons

    # Déclaration des setters

    # Déclaration des getters
    @pokemons.setter
    def pokemons(self, pokemons) :
        
        # ici on a fait le choix de limiter le nombre de participants à 16 pokemons!
        # si on passe en parametre une liste de participant superrieur à 16 :
            # le championnat prend en compte que les 16 premiers participants (pokemons)  de la liste (+ un message)
        if len(pokemons) > 16 :
            print("Le nomre de participants à dépacé les 16 pokemons ! le chompionnat prend en compte que les 16 premiers pokemons inscrits")
            self.__pokemons = [pokemons[i] for i in range(16)]
        else : self.__pokemons = pokemons


    
    

        

