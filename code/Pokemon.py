""" # # # # # # # # # # # # # # # # # # #
    #         CLASSE POOKEMON           #
    # # # # # # # # # # # # # # # # # # # """

from random import randint
from random import uniform
from CompetenceAttaque import CompetenceAttaque
from CompetenceDefense import CompetenceDefense
from fonctionsUtiles import *
from copy import deepcopy    


class Pokemon :
    # Declaration des constructeurs
    def __init__(self, nom, element, niveau, experience, vie, energie, regenerationEnergie, resistance):
        """
        Ici, on a fait le choix de mettre les underscore "__", car on ne souhaite pas appeler les setters lors de
        l'afectation des attributs dans les constructeur. car les setters utilise d'autre attribut du pokemon,
        alors que a ce statde d'implementation les attributs du pokemon ne son pas définie!
        """
        self.__nom = nom
        self.__element = element
        self.__niveauActuelle = int(niveau.split("-")[0])
        self.__niveauMaximal = int(niveau.split("-")[-1])
        self.__experience = experience
        self.__vieReference = int(vie.split("-")[0])
        self.__vieActuelle = self.__vieReference
        self.__vieMaximal = int(vie.split("-")[-1])
        self.__energieReference = int(energie.split("-")[0])
        self.__energieMaximal = int(energie.split("-")[-1])
        self.__energieActuelle = self.__energieReference
        
        # On a choisit un random() entre les deux valeurs données dans le fichier.txt (cases : regénération, résistance)
        self.__regenerationEnergie = randint(int(regenerationEnergie.split("-")[0]), int(regenerationEnergie.split("-")[-1]))
        self.__resistanceActuelle = randint(int(resistance.split("-")[0]), int(resistance.split("-")[-1]))
        self.__resistanceMaximal = int(resistance.split("-")[-1])
        self.__listeCompetences = []  # tableaus de competences (gérer par la fonction ajouterCompetence)
        self.apres = None
        
        

    # Surchage de l'operateur d'affichage
    def __str__(self):
        """
        cette méthode returnant les caractériqtiques et evolution d'un POOkemon, sous forme de String
        (nom, nuveau, energie ...)
        """
        s = f"{self.nom} (Lvl {self.niveauActuelle}, {(self.niveauActuelle)*100}/{(self.niveauActuelle+1)*100}, {self.element} "
        if self.element == "Feu" : s+= str(emoji.emojize('🔥'))
        elif self.element == "Eau" : s += str(emoji.emojize('🌊'))
        elif self.element == "Air" : s += str(emoji.emojize('🦅'))
        else : s += str(emoji.emojize('🌎'))
        s += f"): Vie {self.vieActuelle}/{self.vieReference}"
        s += f", Energie {self.energieActuelle}/{self.energieReference} (+{self.regenerationEnergie})"
        s += f", Experience {self.experience}"
        s += f", resistance {self.resistanceActuelle}"
        
        # parcourir la liste des competences de pokemon, pour afficher le nom ces competences
        for competence in self.listeCompetences :
            s += f", {competence.nom}"
        return s

    # Surchage de l'opérateur d'égalité
    def __eq__(self, other) :
        """
        On surchage l'operateur d'égalité car on sera mener à tester plus tard dans d'autre classe l'egalité entre des
        pokemons. Dans notre cas on considère deux pokemon egaux si selement ils possèdent le meme nom et element!
        """
        if not isinstance(other, Pokemon) : return False
        if self is other : return True
        if self.nom != other.nom : return False
        if self.element != other.element : return False

        return True

    # Déclaration des méthodes 
    def listeDesCompetenseToString(self):
        """
        cette méthode retourn toutes les competences d'un pokemon sous forme d'un String
        """
        s = ""
        for i, competence in enumerate(self.listeCompetences):
            s += "\n" + str(i + 1) + "/ "
            s += competence.__str__()
        return s

    def listeDesCompetencesAttaqueToString(self):
        """
        cette méthode retourn toutes les competences d'attaques d'un pokemon sous forme d'un String
        """
        
        # si le pokemon possède au moins une compétence d'attque, on retourn toutes les competences sous forme d'un String
        if self.nbCompetenceAttaque() > 0 :
            s = "Voici les competences offensives de " + self.nom.title()
            for i, competence in enumerate(self.listeCompetences):
                
                # d'abord, vérifier si la competence est de type ComperenceAttaque
                if isinstance(competence, CompetenceAttaque):
                    s += "\n" + str(i + 1) + "/ "
                    s += competence.__str__()
            return s

        # si non on affiche le message suivant
        print(f"{self.nom} ne possede pas de competences offensives ")

    def listeDesCompetencesDefenseToString(self):
        """
        cette méthode retourn toutes les competences de defense d'un POOkemon sous forme de String
        """
        
        # si le pokemon possède au moins une compétence défensive, on retourn toutes les competences sous forme d'un String
        if self.nbCompetenceDefense() > 0 :
            s = "Voici les competences defensives de " + self.nom.title()
            for i, competence in enumerate(self.listeCompetences):
                
                # d'abord, verifier si la competence est de type CompetenceDefense
                if isinstance(competence, CompetenceDefense):
                    s += "\n" + str(i + 1) + "/ "
                    s += competence.__str__()
            return s

        # si non on affiche le message suivant
        print(f"{self.nom} ne possède pas de competences de defesives ")

    def competenceOk(self, competence) :
        """
        cette méthode vérifie si le pokemon peut utiliser une competence (attaque/defense), 
        c'est à dire (son energie est supperieur au cout de la competence), ainsi on retourn (true or false)
        """
        return self.energieActuelle >= competence.cout

    def attaquer(self, pokemon, competenceAttaque):
        """
        cette methode, permet d'utiliser une competence d'attque contre un pookemon adversse
        """
        # d'abord on vérifie :
            # si la comptence passée en parametre est de type CompetenceAttaque
            # si le pokemon (adversaire) passé en parametre est du type Pokemon
            # si le pokemon (instance courante) est vivant (n'est pas ko)
        if isinstance(pokemon, Pokemon) and isinstance(competenceAttaque, CompetenceAttaque) and not self.estKo() :
            
            # vérification, si l'attaque est réussite
            if competenceAttaque.attaqueReussite():
                degats_infliges = self.degatsInfliges(pokemon, competenceAttaque)  # calcule des degats infligées
                pokemon.vieActuelle -= int(degats_infliges)
                
                # message indicant la réussite de l'attaque
                print(f"attaque reussite {emoji.emojize('✔')} {emoji.emojize('👌')} ({competenceAttaque.nom}) : {degats_infliges} degats infliges {emoji.emojize('⚔')}")
            else :
                
                # message indicant l'échèque de l'attaque
                print(f"echeque de l'attaque ({competenceAttaque.nom}) : {0} degat infliges")

            # dans tous les cas on soustrait le coup de la competence à l'énergie du pokemon
            self.energieActuelle -= competenceAttaque.cout
            
        # si les types de variable passées en parametre son incorecte, on affiche le message suivant
        else :
            
            # si les types des variables passées en parametres ne conviennes pas on affiche le message suivant
            print(f"Erreur! les variables passees en parametres sont du ({type(pokemon)}), ({type(competenceAttaque)}) {emoji.emojize('🚫')}")


    def defendre(self, competenceDefense):
        """
        cette methode, permet d'utiliser une competence défensive contre un pookemon adversaire, (regénération d'un gain de vie/energie)
        """
        
        # d'abord on vérifie :
            # si la comptence passée en est de type CompetenceDefense
            # si le pokemon (instance courante) est vivant
        if isinstance(competenceDefense, CompetenceDefense) and not self.estKo() :
            gainEnergie = competenceDefense.gainEnergie()
            gainVie = competenceDefense.gainVie()

            # régénération d'un gain d'énergie
            self.energieActuelle += gainEnergie
            
            # régénération d'un gain de vie
            self.vieActuelle += gainVie

            # soustraire le cout de la competence à l'énergie du pokemon
            self.energieActuelle -= competenceDefense.cout
            print(f"regeneration d'un gain d'énergie de {gainEnergie} {emoji.emojize('💓')}")
            print(f"regeneration d'un gain de vie de {gainVie} {emoji.emojize('💓')}")
        else :
            
            # normalament on ne seras jamais dans ce cas car si le pokemon est ko le (round) s'arrete
            if self.estKo() : print(f"{self.nom.title()}, ne peut pas utiliser de competence car il KO!")
            else: print(f"Erreur! la competence passes en parametre est de type {type(competenceDefense)}! {emoji.emojize('🚫')}")


    def estKo(self) :
        """
        cette methode retourn un boulean (true/false), indiquant si le pokmon est KO ou pas
        """
        cpt = 0  # compteur de competences possedant un cout superieur à l'énergie du pokemon
        for competence in self.listeCompetences :
            if self.energieActuelle < competence.cout : cpt += 1
        # le pokemon est mort si sa vie <= 0 ou bien il n'as pas assez d'energie pour utiliser au mois une competence
        energieEpuisee = True if cpt == len(self.listeCompetences) else False
        return self.vieActuelle <= 0 or energieEpuisee or self.energieActuelle <= 0


    def nbCompetenceAttaque(self):
        """
        cette méthode retourn le nombre de competence d'attaque d'un pokemon
        """
        cpt = 0  # compteur de competence d'attaque
        for i, competence in enumerate(self.listeCompetences) :
            if isinstance(competence, CompetenceAttaque) : cpt += 1
        return cpt

    def nbCompetenceDefense(self) :
        """
        cette méthode retourn le nombre de competence defensive d'un pokemon
        """
        cpt = 0  # compteur de competences de defense
        for i, competence in enumerate(self.listeCompetences) :
            if isinstance(competence, CompetenceDefense): cpt += 1
        return cpt


    def nbCompetenceTotal(self):  # return le nombre de comperences total
        """
        cette méthode nous retourn le nombre de competence total d'un pokemon
        """
        return len(self.listeCompetences)

    def bonusEnergie(self):
        """
        cette méthode ajoute un bonus pour l'energie d'un pokemon (un random() entre 1 et 5)
        """
        val = randint(0, 5) + self.energieActuelle
        self.__energieActuelle = int(val)

    def bonusVie(self):
        """
        cette méthode ajoute un bonus pour la vie d'un pokemon (un random() entre 1 et 5)
        """
        val = randint(0, 5) + self.vieActuelle
        self.__vieActuelle = int(val)

    def bonusResistance(self):
        """
        cette méthode ajoute un bonus pour la résistance d'un pokemon (un random() entre 1 et 5)
        """
        val = randint(0, 5) + self.resistanceActuelle
        self.__resistanceActuelle = int(val)

    def bonusNiveau(self):
        """
        cette méthode ajoute un bonus pour le niveau d'un pokemon
        """
        self.niveauActuelle = int(self.experience // 100 if (self.experience // 100 < self.niveauMaximal) else self.niveauMaximal)


    def passeAuNiveauSuperieur(self) :
        """
        cette méthode nous retourn (true) si le pokemon passe au niveau superieur si non (false)
        """
        return self.niveauActuelle < (self.experience // 100)

    def peutTransformer(self) :
        """
        cette méthode nous retourn (true) si le pokemon peut se transformer au niveau superieur si non (false)
        """
        return (self.niveauActuelle-1) % 5 == 0 and self.apres != ""


    def ajouterCompetenceAttaque(self, nom, element, description, cout, puissance, precision):
        """
        cette methode assure une relation de composition entre un pokemon est ces competences, car ce dernier crée ces
        propres compentences et ne les partages pas avec d'autre pokemon.
        cette méthode prend en entrée les information nécessaire à la creation d'une competence d'attques, plus tot que une competence
        """
        competence = CompetenceAttaque(nom, element, description, cout, puissance, precision)
        
        # vérifier si la competence est déja présente dans la liste des competence du Pokemon
        # donc surchargé l'opperateur d'egalité "__eq__()" pour de la classe compétence (mesure de securité)
        if not competence in self.listeCompetences:
            self.listeCompetences.append(competence)
              

    def ajouterCompetenceDefense(self, nom, element, description, cout, soin, energie):
        """
        cette methode assure une relation de composition entre un pokemon est ces competences, car ce dernier crée ces
        propres compentences et ne les partages pas avec d'autre pokemon.
        cette méthode prend en entrée les information nécessaire à la creation d'une competence de defense, plus tot que une competence
        """
        competence = CompetenceDefense(nom, element, description, cout, soin, energie)
        
        # vérifier si la competence est déja présente dans la liste des competence du Pokemon
        # donc surchargé l'opperateur d'egalité "__eq__()" pour de la classe compétence (mesure de securité)
        if not competence in self.listeCompetences:
            self.listeCompetences.append(competence)

    def degatsInfliges(self, pokemon, attaque): 
        """
        cette méthode calcule et retourn les dégats infligées par une competence d'attaque contre un autre  adversaire passé en parametre
        """
        
        # d'abord on vérifie :
            # l'attaque passée en parametre est de type CompetenceAttaque
            # pokemon passé en parametre est de type pokemon
        if isinstance(attaque, CompetenceAttaque) and isinstance(pokemon, Pokemon):
            liste_element = ["Air", "Eau", "Feu", "Terre"]
            coefs_b = [[1, 1, 0.5, 0.5],
                       [1.5, 1, 1, 0.5],
                       [0.5, 1.5, 1, 1],
                       [1, 0.5, 1.5, 1]]
            
            i = liste_element.index(pokemon.element)    
            j = liste_element.index(attaque.element)
            b = coefs_b[i][j]
            cm = b * uniform(0.85, 1)

            degat_infliger = cm * (((attaque.puissance * (4*self.niveauActuelle + 2)) / self.resistanceActuelle) + 2)
        return round(degat_infliger)

    def peutEtreCapturer(self):
        """
        cette méthode retourn (true) si le pokemon advesaire et prét a etre capturer si non (false)
        """
        proba = 4 * ( 0.2 - (self.vieActuelle/self.vieReference) )
        return proba < uniform(0,1) and (self.vieActuelle / self.vieReference) < 0.2

    def miseAJour(self):
        """
        cette méthode remet à jour l'energie et la vie actuelle d'un pokemon à leurs valeurs initiales, après chaque combat
        """
        self.energieActuelle = self.energieReference
        self.vieActuelle = self.vieReference

    def cometenceAleatoir(self):
        """
        cette méthode retourn une competence aleatoir, d'un pokemon (attaque ou defense)
        """
        alea = randint(0, len(self.listeCompetences) -1)
        return self.listeCompetences[alea]

    def cometenceAleatoirAttaque(self):
        """
        cette méthode retourn une competence d'attaque aleatoire d'un pokemon
        """
        
        # initialiser la competence a la première competence de liste des competense
        competence = self.listeCompetences[0]

        # tant que on a pas choisie une competence defensive en continue de generer un choix aleatoire
        while not isinstance(competence, CompetenceAttaque):
            alea = randint(0, len(self.listeCompetences) - 1)
            competence = self.listeCompetences[alea]
        return competence

    def meilleureCompetenceAttaque(self, pokemon):
        """
        Cette méthode retourn la meilleur competence d'attaque qu'un pokemon possède en calculant d'une manière récursive
        la competence d'attque qui engendre plus de gégats (ce n'est qu'une aproximation sans tenir compte de la valeur aléatoire dans le calcule des dégat inflifés)
        cette méthode sera utlisée pour l'implémentation de l'algorithme de l'intelligence artificielle  
        """
        
        # initialisé les variable maxDega (le degas le plus grave engendré par la meilleur compétence)
        # création d'une liste de degats avec une copie profonde d'un pokemon
        maxDega = None
        maxIdx = None
        listDega=[]
        for i in range(0, len(self.listeCompetences)) :
            if isinstance(self.listeCompetences[i], CompetenceAttaque):
                listDega.append(self.degatsInfliges(deepcopy(pokemon), self.listeCompetences[i]))
        for idx, dega in enumerate(listDega):
            if (maxDega is None or dega > maxDega):
                maxDega = dega
                maxIdx = idx
            return self.listeCompetences[maxIdx]

    def meilleureCompetenceDefense(self):
        """
        on remarque que chaque pokemon posède au plus une seule competence défensive pour le coup on prefere retourné
        directement la competence s'il possède sinon il retourne une competence à cout minimale
        """
        for i in range(0, len(self.listeCompetences)):
            try:
                if isinstance(self.listeCompetences[i], CompetenceDefense):
                    return self.listeCompetences[i]
            except:
                return self.competenceMoinCout

    def competenceAttaqueMoinCout(self) :
        """
        cette méthode return la competence qui possède le cout minimale 
        """
        # parcourir toutes les competences possedées par un pokemon et retourner la competence a cout minimale
        coutMin = None
        idxMin = None
        for idx, competence in enumerate(self.listeCompetences):
            if isinstance(competence, CompetenceAttaque):
                if (coutMin is None or competence.cout < coutMin):
                    coutMin = competence.cout
                    idxMin = idx
        return self.listeCompetences[idxMin]


    # Déclaration des setters et les getters

    # Déclaration getters
    @property
    def nom(self):
        # le nom du pokemon est privé
        return self.__nom

    @property
    def element(self):
        # l'element do pokemon est privé
        return self.__element

    @property
    def niveauActuelle(self):
        # le niveau du pokemon est privé
        return self.__niveauActuelle

    @property
    def niveauMaximal(self):
        # le niveau maximal du pokemon est privé
        return self.__niveauMaximal

    @property
    def experience(self):
        # l'experience du pokemon est privée
        return self.__experience

    @property
    def vieActuelle(self):
        # la vie actuelle du pekemon est privée
        return self.__vieActuelle

    @property
    def vieMaximal(self):
        # la vie actuelle du pekemon est privée
        return self.__vieMaximal

    @property
    def vieReference(self):
        # la vie actuelle du pekemon est privée
        return self.__vieReference

    @property
    def energieActuelle(self):
        # l'energie actuelle du pokeomn est privée
        return self.__energieActuelle

    @property
    def energieReference(self):
        # l'energie actuelle du pokeomn est privée
        return self.__energieReference

    @property
    def energieMaximal(self):
        # l'energie actuelle du pokeomn est privée
        return self.__energieMaximal

    @property
    def regenerationEnergie(self):
        # le gain de regeneration du pokemon est privé
        return self.__regenerationEnergie

    @property
    def resistanceActuelle(self):
        # la resistance actuelle du pokemon est privée
        return self.__resistanceActuelle

    @property
    def resistanceMaximal(self):
        # la resistance maximal du pokemon est privée
        return self.__resistanceMaximal

    @property
    def listeCompetences(self):
        # la liste des competences du pokemon est privée
        return self.__listeCompetences

    # Declaration des setters
    @nom.setter
    def nom(self, nom):
        # le nom du pokemon est privé
        self.__nom = int(nom)

    # logiquement l'element d'un pokemon ne sera jamais modifier !! A revoir
    @element.setter
    def element(self, element):
        # l'element do pokemon est privé
        self.__element = int(element)

    @niveauActuelle.setter
    def niveauActuelle(self, niveau):
        # le niveau du pokemon est privé
        self.__niveauActuelle = int(niveau)
        if self.__niveauActuelle > self.__niveauReference :
            self.__niveauActuelle = self.__niveauReference
        elif self.__niveauActuelle < 0:
            self.__niveauActuelle = 0

    @niveauMaximal.setter
    def niveauMaximal(self, niveau):
        # le niveau du pokemon est privé
        self.__niveauMaximal = int(niveau) if niveau > 0 else 0

    @experience.setter
    def experience(self, experience):
        # l'experience du pokemon est privée
        self.__experience = int(experience)
        if self.__experience < 0 :
            self.__experience = 0

    @vieActuelle.setter
    def vieActuelle(self, vie):
        # la vie actuelle du pekemon est privée
        self.__vieActuelle = int(vie)
        if self.__vieActuelle > self.__vieReference :
            self.__vieActuelle = self.__vieReference
        elif self.__vieActuelle < 0 :
            self.__vieActuelle = 0

    @vieMaximal.setter
    def vieMaximal(self, vie):
        # la vie maximal du pekemon est privée
        self.__vieuMaximal = int(vie) if vie > 0 else 0

    @vieReference.setter
    def vieReference(self, vie):
        # la vie Reference du pekemon est privée
        self.__vieuReference = int(vie)
        if self.__vieuReference > self.__vieMaximal:
            self.__vieuReference = self.__vieMaximal
        elif self.__vieuReference < 0:
            self.__vieuReference = 0


    @energieActuelle.setter
    def energieActuelle(self, energie):
        # l'energie actuelle du pokeomn est privée
        self.__energieActuelle = int(energie)
        if self.__energieActuelle > self.__energieReference:
            self.__energieActuelle = self.__energieReference
        elif self.__energieActuelle < 0 :
            self.__energieActuelle = 0

    @energieReference.setter
    def energieReference(self, energie):
        # l'energie Reference du pokeomn est privée
        self.__energieReference = int(energie)
        if self.__energieReference > self.__energieMaximal:
            self.__energieReference = self.__energieMaximal
        elif self.__energieReference < 0:
            self.__energieReference = 0

    @energieMaximal.setter
    def energieMaximal(self, energie):
        # l'energie actuelle du pokeomn est privée
        self.__energieMaximal = int(energie) if energie > 0 else 0


    @regenerationEnergie.setter
    def regenerationEnergie(self, regenerationEnergie):
        # le gain de regeneration du pokemon est privé
        self.__regenerationEnergie = int(regenerationEnergie)
        if self.__regenerationEnergie[0] > self.__regenerationEnergie[-1] :
            self.__regenerationEnergie[0] = self.__regenerationEnergie[-1]
        elif self.__regenerationEnergie[0] < 0 :
            self.__regenerationEnergie[0] = 0

    @resistanceActuelle.setter
    def resistanceActuelle(self, resistance):
        # le gain de regeneration du pokemon est privé
        self.__resistanceActuelle = int(resistance)
        if self.__resistanceActuelle > self.__resistanceMaximal :
            self.__resistanceActuelle = self.__resistanceMaximal
        elif self.__resistanceActuelle < 0 :
            self.__resistanceActuelle = 1     # car on peut avoir une division par 0 lors du calcule des degats infligets (mesur de securité)

    @resistanceMaximal.setter
    def resistanceMaximal(self, resistance):
        # le gain de regeneration du pokemon est privé
        self.__resistanceMaximal = int(resistance) if resistance > 0 else 1

    """
    Ici, on a fait le choix de ne pas mettre un setters pour la liste des competences du pokemon, car on ne souhaite pas 
    fair des modifications de competences pour un pkemon donnée 
    """
    # @listeCompetences.setter
    # def listeCompetences(self, listeCompetences):
    #     # le gain de regeneration du pokemon est privé
    #     # s'assurer que tous les element de la liste sont de type Competence
    #     self.__listeCompetences = listeCompetences
