from Combat import Combat
from Dresseur import Dresseur
from CompetenceDefense import CompetenceDefense
from CompetenceAttaque import CompetenceAttaque
from Pokemon import Pokemon
from random import randint
from fonctionsUtiles import *
import emoji
from abc import ABC, abstractmethod

class CombatJCJ (Combat) :
    # Déclaration du constructeur
    def __init__(self, dresseur, dresseur2):
        # appel au constructeur de la super classe ( Combat )
        super().__init__(dresseur)
        self.dresseur2 = dresseur2

    # surchge de l'operateur d'afficchage
    def __str__(self) :
        return f"Combat JCJ entre {self.dresseur.nom} et {self.dresseur2.nom}! {emoji.emojize('👊')}{emoji.emojize('👊')}"


    # Déclaration des méthodes

    # redefinir la méthode gagnant
    def gagnant(self):
        return self.dresseur2 if ( (self.score[1] > self.score[0]) or (self.aFuit == 1) )  else self.dresseur 

    # redefinir la méthode gagnant
    def perdant(self):
        return self.dresseur2 if self.score[1] < self.score[0] else self.dresseur

    # redefinir la méthode affichageScoreVie pour un combat JCJ
    def affichageScoreVie(self) :
        """
        cette méthode affiche le scors du combat pendant les tours
        """
        # recuperer le pokemon de la prmière liste du dresseur adverse (pokemon qui combat à l'instant)
        pokemon = self.dresseur2.listePokemon[0]
        if isinstance(pokemon, Pokemon):
            super().affichageScoreVie()
            s = f"  * {pokemon.nom}: {int(pokemon.vieActuelle * 100 / pokemon.vieReference)} % {emoji.emojize('🧪')}"
            print(s)


    def affichageScoreRound(self):
        """
        cette méthode affiche le score du combat (jouer contre joueur) chaque fin du round
        """
        # recuperer les pokemon combatabt des dreseeur 1/2 (le prmier pokemon de la liste de chaque dresseur)
        pokemon1 = self.dresseur.listePokemon[0]  # le pokemon combatant du dresseur1
        pokemon2 = self.dresseur2.listePokemon[0]  # le pokemon combatatnt du dresseur 2

        pokemonGagnat = pokemon1 if self.score[0] > self.score[1] else pokemon2 # recupere le pokemon gagnant
        # affichage du vinceur d'un round
        s = f"{pokemonGagnat.nom} a remporte ce ROUND avec "
        s += f"FORFET " if (self.aFuit == 1 or self.aFuit == 2) else "KO "
        s += f"{emoji.emojize('✌')} apres {self.tour} "
        s += "TOUR " if self.tour in [0, 1] else "TOURS "
        s += "\nSCORE Round: "
        s += f"\n  * {self.dresseur.nom}: {self.score[0]} "
        s += "ROUND" if self.score[0] in [0, 1] else "ROUNDS"
        s += f"\n  * {self.dresseur2.nom} : {self.score[1]} "
        s += "ROUND" if self.score[1] in [0, 1] else "ROUNDS"
        print(s)

    def affichageScoreFinal(self):
        # ici on est à la fin du comba, on doit afficher les résultats final
        # si pokemon 1 à fuit le combat, donc pokemo2 est vinceur avec forfet
        if self.aFuit == 1:
            print(
                f"{self.dresseur2.nom} a remporte le combat FORFAIT avec un {self.scoreRound()} "
                f"{emoji.emojize('🎉')} {emoji.emojize('✌')}")

        # si le pokemon 2 à fuit le combat, donc pokemon1 est viceur avec forfet
        elif self.aFuit == 2:
            print(
                f"{self.dresseur.nom} a remporte le combat FORFAIT avec un {self.scoreRound()} "
                f"{emoji.emojize('🎉')} {emoji.emojize('✌')}")

        # si le nombre de vectoire du pokemon1 superieur à celle de pokemon2, donc le gagant est pokemon1 avec un KO
        elif self.score[0] > self.score[1]:
            print(
                f"{self.dresseur.nom} a remporte le combat avec un {self.scoreRound()} "
                f"{emoji.emojize('🎉')} {emoji.emojize('✌')}")

        # si le nombre de victoire du pokemon2 superieur à celle de pokemon1, donc le gagnat est pokemon2 avec un KO
        else:
            print(
                f"{self.dresseur2.nom} a remporte le combat avec un {self.scoreRound()} "
                f"{emoji.emojize('🎉')} {emoji.emojize('✌')}")


    def scoreRound(self) :
        """
        cette méthode gère le scors du à la fin du combat pour JCJ
        """
        if isinstance(self.dresseur, Dresseur) and isinstance(self.dresseur2, Dresseur) :
            s = ""
            if self.score[0] >= self.score[1] :
                s += f"score ==> {self.dresseur.nom}: {self.score[0]} "
                s += "ROUNDS " if self.score[0] > 1 else "ROUND / "
                s += f"{self.dresseur2.nom}: {self.score[1]} "
                s += "ROUNDS " if self.score[1] > 1 else "ROUND "

            else :
                s += f"score ==> {self.dresseur2.nom}: {self.score[1]} "
                s += "ROUNDS " if self.score[1] > 1 else "ROUND / "
                s += f"{self.dresseur.nom}: {self.score[0]} "
                s += "ROUNDS " if self.score[0] > 1 else "ROUND "
            return s

    def roundCombat(self) :
        """
        cette méthode organise un round JCJ, elle sera utlisé dans la méthode combat JCJ
        """
        # récuperer le choix du dresseur1 (choix du pokemon combatabt) dans la variable pokemon1
        pokemon1 = self.dresseur.choixPokemon()
        print("\n-----------------------------------------------------------------------")
        # récuperer le choix du dresseur2 (choix du pokemon combatabt) dans la variable pokemon2
        pokemon2 = self.dresseur2.choixPokemon()

        # tent que les deux pokemons, ne sont pas ko et ils n'ont pas abnandonnés le combat (le combat continue)
        while not (pokemon1.estKo()) and not (pokemon2.estKo() ) and self.aFuit == False :

            print("\n-----------------------------------------------------------------------")
            print(f"Tour {self.tour + 1}")

            # jouer tour pour tour
            if self.tour % 2 == 0 :
                pokemonJoueur = pokemon1
                pokemonNonJoueur = pokemon2
                dresseurJoueur = self.dresseur
                # dresseurNonJoueur = self.dresseur2
            else :
                pokemonJoueur = pokemon2
                pokemonNonJoueur = pokemon1
                dresseurJoueur = self.dresseur2
                # dresseurNonJoueur = self.dresseur

            # recuperer le nombre de competence du pokemonJouer pour adapter le menu d'affichage
            nbCompetencePokemon = pokemonJoueur.nbCompetenceTotal()
            listeChoix = [str(i) for i in range(1, nbCompetencePokemon + 4)]

            print(f"C'est a {dresseurJoueur.nom} de jouer!")
            print(pokemonJoueur)
            choix = saisieChoix(self.menu(pokemonJoueur), listeChoix)

            # choisir de fuir le combat
            if choix == nbCompetencePokemon + 3:
                print(f"{dresseurJoueur.nom} vous avez fui le combat! 😓 😩")
                self.aFuit = 1 if self.tour % 2 == 0 else 2   # le pokemon1/2 a fuit le combat
                # Affichage du scors de vie des pokemons dans le cas ou un des pokemon a fuit
                self.affichageScoreVie()
                break   # quittez le round

            # choisir de passé son tour
            elif choix == nbCompetencePokemon + 2:
                print(f"{dresseurJoueur.nom} vous avez passez votre tour!") # je passe mon toures danc je ne fais rien

            # choisir de changer de pokemon
            elif choix == nbCompetencePokemon + 1:
                print("\n-----------------------------------------------------------------------")
                if self.tour % 2 == 0 : pokemon1 = dresseurJoueur.choixPokemon()
                else :  pokemon2 = dresseurJoueur.choixPokemon()
                self.tour -= 1

            # choisir une competence attaque/defense
            else :
                choix = choix - 1
                competence =  pokemonJoueur.listeCompetences[choix]
                # vérifier la type de la competence qui a été choisie pour utliser la bonne méthode (attaque / defendre)
                if pokemonJoueur.competenceOk(competence):  # si le pokemo peut utiliser la competence choisie
                    if isinstance(competence, CompetenceDefense):
                        pokemonJoueur.defendre(competence)
                    elif isinstance(competence, CompetenceAttaque):
                        pokemonJoueur.attaquer(pokemonNonJoueur, competence)
                else:
                    print(f"Votre energie est insuffisante pour utiliser l'attaque {competence.nom}! {emoji.emojize('🚫')}")
                    self.tour -= 1
            self.tour += 1
            # Affichage du scors de vie des pokemons dans le cas ou un des pokemon et ko
            self.affichageScoreVie()

        # on retourn les deux pokemon et le variable "aFuit" qui nous indique quelle pokemon a fuit ou pas
        return pokemon1, pokemon2, self.aFuit, self.tour


    def combat(self) :
        """
        cette méthode réalise un combat JCJ
        """
        print(f"Combat JCJ entre {self.dresseur.nom} et {self.dresseur2.nom}! {emoji.emojize('👊')}{emoji.emojize('👊')}")
        # initialiser le nombre de victoires pour chaque Roud

        # il faut tois victoir pour un gagnant
        while self.score[0] < 3 and self.score[1] < 3 :
            print(f"\n=======================================   ROUND {self.round + 1}   ==============================================\n")
            pokemon1, pokemon2, aFuit, tour = self.roundCombat()

            #si le pokemon1 à fuit le combat
            if aFuit == 1:
                pokemonPerdant = pokemon1
                dresseurGagnant = self.dresseur2
                dresseurPerdant = self.dresseur
                self.score[1] += 1
                # affcihage du scor de round dans le cas ou un des pokemon a fuit
                self.affichageScoreRound()
                # récomponser le dresseur dresseurGagnant
                dresseurGagnant.miseAJour()
                dresseurPerdant.miseAJour()
                dresseurGagnant.bonusDekganantJCJ(dresseurPerdant)
                break    # quitter le combat

            # si le pokemon 2 à fuit le combat
            elif aFuit == 2 :
                pokemonPerdant = pokemon2
                dresseurGagnant = self.dresseur
                dresseurPerdant = self.dresseur2
                self.score[0] += 1
                # affcihage du scor de round dans le cas ou un des pokemon a fuit
                self.affichageScoreRound()
                # récomponser le dresseur dresseurGagnant
                dresseurGagnant.miseAJour()
                dresseurPerdant.miseAJour()
                dresseurGagnant.bonusDekganantJCJ(dresseurPerdant)
                break  # quiter le combat

            # si le pokemon2 est KO
            elif pokemon2.estKo() :
                pokemonGagnant = pokemon1
                pokemonPerdant = pokemon2
                dresseurGagnant = self.dresseur
                dresseurPerdant = self.dresseur2
                self.score[0] += 1

            # si le pokemon 1 est KO
            elif pokemon1.estKo() :
                pokemonGagnant = pokemon2
                pokemonPerdant = pokemon1
                dresseurGagnant = self.dresseur2
                dresseurPerdant = self.dresseur
                self.score[1] += 1

            # affcihage du scor de round dans le cas ou un des pokemon est Ko
            self.affichageScoreRound()
            self.round += 1
            self.miseAJourTour()

        # ici on est à la fin du comba, on doit afficher les résultats final
        self.affichageScoreFinal()

        # récompoenser le dek du dresseur gagnant
        dresseurGagnant.miseAJour()
        dresseurPerdant.miseAJour()
        dresseurGagnant.bonusDekganantJCJ(dresseurPerdant)
        #self.miseAJourCombat()
        
    # Déclaration des setters et les getters

    # Les getters
    @property
    def dresseur2(self) :
        # un dresseur est déclarer privé dans une instace de type CombatJCJ
        return self.__dresseur2

    # les setters
    @dresseur2.setter
    def dresseur2(self, dresseur2) :
        # on s'assure que la variable "dresseur2" passée en parametre est de type ( Dresseur )
        if isinstance(dresseur2, Dresseur) :
            self.__dresseur2 = dresseur2
            # on retrouen True si l'affectation est réussite, si non false puis un affiche un emessage d'erreur
            return True
        print(f"Erreur! la variabe que vous avez passez en parametre est de type {type(Dresseur)} {emoji.emojize('🚫')}")
        return False