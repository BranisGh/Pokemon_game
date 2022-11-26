""" # # # # # # # # # # # # # # # # # # #
    #        CLASSE Championnat         #
    # # # # # # # # # # # # # # # # # # # """

from random import shuffle    
from CombatJCJ import CombatJCJ
from Championnat import Championnat


class ChampionnatJCJ(Championnat) : 
    
    # Déclaration du constructeur
    def __init__(self, joueur, joueurs) :
        # appele au constructeur de la supper classe
        super().__init__(joueur)
        # self.joueurs et une liste 2D comporant pour chaque ligne un joueur et ses points
            # par defaut les points de tous les joueurs sont inisialisé à 0
            # le premier indice de chauque element comporte le joueur
            # le deuxième idice de chaque element comporte les points du joueur (on incrmante les points à chaque victoir d'un combat)
        self.joueurs = [[]]    
        self.joueurs = joueurs
        self.joueurs.insert(0, [joueur, 0])
        
        # ici on a fait le choix faire faire combatre :
        # les joueurs qui portent des incices paire VS les joueurs qui portent des incices impaire
        self.__joueursPaire = []        # Initialisation de la liste des joueurs portants un indice paire
        self.__joueursImpaire = []      # Initiolisation de la liste des joueurs portants un indice impaire 
           
        
     
    # Déclaration des méthodes 
    def who(self) :
        """ cette méthode retourn le nom de la classe, ici (Championnat)"""
        return "ChampionnatJCJ"
    
    def classement(self) :
        """ cette méthode classe les joueur du plus grand nombre de points au plus petit nombre"""
        #return self.joueurs.sort(self.joueurs, key=lambda joueur: joueur[-1]).reverse()
        self.joueurs.sort(key=lambda joueur: joueur[-1], reverse=True)

    
    def affichgeClassement(self) :
        self.classement()
        s = "________________________________"
        for i, joueur in enumerate(self.joueurs) :
            s += f"\n{i+1}\ {joueur[0].nom}  ({joueur[-1]} pts)"
            s += f"🥇 🏆" if i == 0 else ""
            s += f"🥈" if i == 1 else ""
            s += f"🥉" if i == 2 else ""
            s += "\n________________________________"
        print(s)
    
    
    def affichageCalendrier(self) :
        """
        cette méthode affiche le calendrier des combats, on l'utilise pour chaque tour
        afin de voir le calendrier achque nouveaux combats
        """
        self.classement()
         
        # remplicage des liste des joueur portant des indices (paire/impaire) 
        self.joueursPaire = [self.joueurs[i] for i in range(int(len(self.joueurs) / (2**self.tour))) if (i%2 == 0)]
        self.joueursImpaire = [self.joueurs[i] for i in range(int(len(self.joueurs) / (2**self.tour))) if (i%2 != 0)]
        
        # menalger les joueur dans les deux listes d'une magnière aléatoir
        shuffle(self.joueursPaire)
        shuffle(self.joueursImpaire)
        
        s =  "________________________________"
        for i in range(len(self.joueursPaire)) :
            s += f"\n|combat {i+1}| {self.joueursPaire[i][0].nom}  vs   {self.joueursImpaire[i][0].nom}"
            s += "\n________________________________"
        
        print(s)
    
    def reset(self) : 
        """
        cette méthode remet à zero les points de chaque joueur participant au championnat
        ainsi que le nombre de tour, elle sera utliser à la fin d'un championnat'
        """
        for i in range(len(self.joueurs)) : 
            self.joueurs[i][-1] = 0
        self.tour = 0
    
    def championnat(self) :
        # réaliser tout les combat de ième tour
        cpt = len(self.joueurs)
        while cpt >= 2 :
            s = ""
            if cpt == 16 : s = f"des {int(cpt/2)}eme de"
            elif cpt == 8: s = "des quart de"
            elif cpt == 4 : s = "des demi"
            elif cpt == 2 : s = "de la"
    
            if cpt != 2 : print(f"\n\nVoici le calendrier des combats " + f"{s} finale")
            else : print(f"\n\nVoici le calendrier du combat " + f"{s} finale")
        
            #print(f"Voici le calendrier des combats des (Tour {self.tour + 1})")
            self.affichageCalendrier()
            
            for i in range(len(self.joueursPaire)) :
                if len(self.joueursPaire) > 1 :
                    print(f"\n\n--------------   Combat numero {i+1} FIGHT ....   ------------------\n")
                else : print("\n\n")
                
                combat = CombatJCJ(self.joueursPaire[i][0], self.joueursImpaire[i][0])
                combat.combat()
                joueurGagnant = combat.gagnant() #self.joueursImpaire[i][0] if ( (combat.score[1] > combat.score[0]) or (combat.aFuit == 1) )  else self.joueursPaire[i][0] 
                
                if joueurGagnant == self.joueursPaire[i][0] :
                    self.joueursPaire[i][-1] += 1                           # récomponser le joueur gaganat
                else :
                    self.joueursImpaire[i][-1] += 1                         # récomponser le dresseur gaganat
            self.tour += 1
            cpt = int(cpt/2)
        
        print("\n\n\nVoici le classement final du championnat")
        self.affichgeClassement()
        self.reset()

    
    
    
    
    # Déclaration des properties
    
    #Déclaration des getters
    @property
    def joueurs(self) :
        return self.__joueurs
    
    @property
    def joueursPaire(self) : 
        return self.__joueursPaire
    
    @property
    def joueursImpaire(self) : 
        return self.__joueursImpaire
    

    # Déclaration des setters
    #Déclaration des getters
    @joueurs.setter
    def joueurs(self, joueurs) :
        
        # ici on a fait le choix de limiter le nombre de participants à 16 personnes! 
        # si on passe en parametre une liste de participant superrieur à 16 :
            # le championnat prend en compte que les 16 premiers participants  de la liste (+ un message) 
            
            # self.joueurs et une liste 2D comporant pour chaque ligne un joueur et ses points
            # par defaut les points de tous les joueurs sont inisialisé à 0
            # le premier indice de chauque element comporte le joueur
            # le deuxième idice de chaque element comporte les points du joueur (on incréponte les points à chaque victoir d'un combat)
        if len(joueurs) > 16 :
            print("Le nomre de participants à dépacé les 16 personne ! le chompionnat prend en compte que les 16 premiers inscrits")
            self.__joueurs = [[joueurs[i], 0] for i in range(16)]
        else : self.__joueurs = [[joueurs[i], 0] for i in range(len(joueurs))]
    
        
    @joueursPaire.setter
    def joueursPaire(self, joueursPaire) : 
        self.__joueursPaire = joueursPaire
    
    @joueursImpaire.setter
    def joueursImpaire(self, joueursImpaire) : 
        self.__joueursImpaire = joueursImpaire
    

        

