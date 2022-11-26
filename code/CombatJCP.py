from Combat import Combat
from Dresseur import Dresseur
from CompetenceDefense import CompetenceDefense
from CompetenceAttaque import CompetenceAttaque
from Pokemon import Pokemon
from fonctionsUtiles import *
import emoji

class CombatJCP (Combat) :
    # Déclaration du constructeur
    def __init__(self, dresseur, pokemon, capturer, niveau):
        # appel au constructeur de la super classe ( Combat )
        super().__init__(dresseur)
        self.pokemon = pokemon
        self.capturer = capturer   # "caprurer" prend 1 si on fait le choix de capturer le pokemon et 0 si non
        self.okCapturer = False    # "okCapturer" prend 1 si on a capturer le pokemon, 0 si non
        self.niveau = niveau       # "niveau" prend {1, 2 ou 3} ce sont les 3 niveau de difficulté du jeux

    # surchge de l'operateur d'afficchage
    def __str__(self) :
        return f"Combat JCP entre {self.dresseur.nom} et {self.pokemon.nom}! {emoji.emojize('👊')}{emoji.emojize('👊')}"

    # Déclaratien des méthode

    # redefinir la méthode gagnant
    def gagnant (self):
        return self.pokemon if self.score[1] > self.score[0] else self.dresseur.listePokemon[0]

    # redefinir la méthode gagnant
    def perdant(self):
        return self.pokemon if self.score[1] < self.score[0] else self.dresseur.listePokemon[0]

    # redefinir la méthode affichageScoreVie pour un combat JCP
    def affichageScoreVie(self):
        """
        cette méthode affiche le scors du combat pendant les tours
        """
        if isinstance(self.pokemon, Pokemon):
            super().affichageScoreVie()
            s = f"  * {self.pokemon.nom}: {int(self.pokemon.vieActuelle * 100 / self.pokemon.vieReference)} % {emoji.emojize('🧪')}"
            print(s)

    # redefinir la méthide affichageScireRound pour la classe CombatJCP
    def affichageScoreRound(self):
        """
        cette méthode affiche le score du combat (jouer contre pokemon) chaque fin du round
        """
        # recuperer les pokemon combatabt des dreseeur 1/2 (le prmier pokemon de la liste de chaque dresseur)
        pokemon1 = self.dresseur.listePokemon[0]  # le pokemon combatant du dresseur1
        pokemon2 = self.pokemon                         # le pokemon adverse
        pokemonGagnat = pokemon1 if self.score[0] >= self.score[1] else pokemon2  # recuperer le pokemon gagnant

        # affichage du vinceur d'un round
        s = f"{pokemonGagnat.nom} a remporte ce ROUND avec "
        s += f"FORFET " if (self.aFuit == 1 or self.aFuit == 2) else "KO "
        s += f"{emoji.emojize('✌')} apres {self.tour} "
        s += "TOUR" if self.tour in [0, 1] else "TOURS "
        s += "\nSCORE Round:"
        s += f"\n  * {self.dresseur.nom}: {self.score[0]} "
        s += "ROUND" if self.score[0] in [0, 1] else "ROUNDS"
        s += f"\n  * {pokemon2.nom} : {self.score[1]} "
        s += "ROUND" if self.score[1] in [0, 1] else "ROUNDS"
        print(s)

    def affichageScoreFinal(self):  # cette atrubut vaut True si le pokemon a été capturer si non false

        # ici on est à la fin du comba, on doit afficher les résultats final
        # @ pokemon1 : pokemon du dresseur
        # @ pokemon2 : pokemon adverse

        # si pokemon1 à fuit le combat, donc pokemo2 est vincuer avec forfet
        if self.aFuit:
            print(
                f"{self.pokemon.nom.title()} a remporte le combat FORFAIT avec un {self.scoreRound()}"
                f"{emoji.emojize('🎉')} {emoji.emojize('✌')}")

        # si le pokemon2 a été captué
        elif self.okCapturer:
            print(
                f"{self.dresseur.nom.title()} a remporte le combat en capturant {self.pokemon.nom.title()} avec un {self.scoreRound()}"
                f"{emoji.emojize('🎉')} {emoji.emojize('✌')}")

        # si le nombre de vectoire du pokemon1 superieur ou egale à celle de pokemon2
        # donc le gagant est pokemon1 avec un KO
        # car il suffit de le metre Ko une fois pour remporter le combat
        elif self.score[0] >= self.score[1]:
            print(
                f"{self.dresseur.nom.title()} a remporte le combat avec un {self.scoreRound()}"
                f"{emoji.emojize('🎉')} {emoji.emojize('✌')}")

        # si le nombre de victoire du pokemon2 superieur à celle de pokemon1, donc le gagnat est pokemon2 avec un KO
        # dans se cas le pokemon advrese à batut 3 fois le dresseur
        else:
            print(
                f"{self.pokemon.nom.title()} a remporte le combat avec un {self.scoreRound()}"
                f"{emoji.emojize('🎉')} {emoji.emojize('✌')}")


    def scoreRound(self) :
        """
        cette méthode gère le scors du à la fin du combat pour JCJ
        """
        if isinstance(self.dresseur, Dresseur) and isinstance(self.pokemon, Pokemon) :
            s = ""
            if self.score[0] >= self.score[1] :
                s += f"score ==> {self.dresseur.nom}: {self.score[0]} "
                s += "ROUNDS " if self.score[0] > 1 else "ROUND / "
                s += f"{self.pokemon.nom}: {self.score[1]} "
                s += "ROUNDS " if self.score[1] > 1 else "ROUND "

            else :
                s += f"score ==> {self.pokemon.nom}: {self.score[1]} "
                s += "ROUNDS " if self.score[1] > 1 else "ROUND / "
                s += f"{self.dresseur.nom}: {self.score[0]} "
                s += "ROUNDS " if self.score[0] > 1 else "ROUND "
            return s

    def roundCombat(self):
        pokemon1 = self.dresseur.choixPokemon()   # choisir un pokemon pour combattre
        pokemon2 = self.pokemon

        # au debut du combat le pokemon n'est pas encore capturer
        #okCpturer = False

        # le combat continu tant que les deux pokemon sont en vie et que aucun n'as fuit le combat
        while not (pokemon1.estKo()) and not (pokemon2.estKo()) and self.aFuit == False:
            print("\n-----------------------------------------------------------------------")

            print(f"Tour {self.tour + 1}")

            # jouer tour pour tour
            if self.tour % 2 == 0:
                print(f"C'est a {self.dresseur.nom} de jouer!")

                # initialiser la liste de chois possibles pour le pokemon (liste de string prend (1, 2, 3...)
                nbCompetencePokemon1 = pokemon1.nbCompetenceTotal()
                listeChoix = [str(i) for i in range(1, nbCompetencePokemon1 + 4)]

                # si on a choisie l'option capturer pokemon on doit d'abord à chaque tour verivier si on peut le capturer
                if self.capturer and pokemon2.peutEtreCapturer():   # si on a choisie l'option capturer et que le pokemon est pret à etre capturer
                    print(
                        f"{self.dresseur.nom} vous pouvez capturer le {pokemon2.nom.title()}, il est a bout de ces forces! {emoji.emojize('🧪')}")
                    print()
                    choix = saisieChoix(f"1/ non \n2/ oui\n  {emoji.emojize('👉')}  Que voulez vous faire ? (1-2)", ["1", "2"])

                    if choix == 2:

                        # vérifier si le dresseur n'a pas le mem pokemon deja dans sa liste
                        # dresseur ne peut pas avoir plusieur meme pokemon dans sa liste
                        if pokemon2 not in self.dresseur.listePokemon:
                            pokemon2.miseAJour()    # on met a jour le pokemon à captirer
                            self.dresseur.capturerPokemon(pokemon2)
                            #print(f"{self.dresseur.nom}, vous avez bien reussi a capturer {pokemon2.nom}")
                            self.okCapturer = True    # le pokemon à bété capturer
                            break                      # on sort du combat
                        else:
                            # on remet la variable capturer a False car on ne peut pas capturer ce pokemon
                            self.capturer = False
                            print(
                                f"vous ne pouver pas capture {pokemon2.nom}, il existe deja dans votre liste pokemon! {emoji.emojize('🚫')}")

                print(pokemon1)
                choix = saisieChoix(self.menu(pokemon1), listeChoix)   # affichage du menue des choix de competence

                if choix == nbCompetencePokemon1 + 3:
                    print(f"{self.dresseur.nom} vous avez fui le combat! 😓 😩")
                    self.aFuit = 1  # le pokemon a fuit le combat
                    # affiche du sucor de vie lorsque le pokemon du dresseur a fuit
                    self.affichageScoreVie()  # afichege du score de vie des pokemon combatant avant de quiter la combat
                    break  # quiter le combat

                # si on a choisie de passer le tour
                elif choix == nbCompetencePokemon1 + 2:
                    print(
                        f"{self.dresseur.nom} vous avez passez votre tour!")  # je passe mon toures danc je ne fais rien

                # si on a choisie de changer de pokemon
                elif choix == nbCompetencePokemon1 + 1:
                    print("\n-----------------------------------------------------------------------")
                    pokemon1 = self.dresseur.choixPokemon()
                    self.tour -= 1

                # si on choisie une compenetence (attaque/defense)
                else:
                    choix = choix - 1

                    # recuperer le competence utlister dans la liste des competence du pokemon
                    competence = pokemon1.listeCompetences[choix]

                    # on peut utliser une competense si seulement l'energie du pokemon > au couo de la competence
                    if pokemon1.competenceOk(competence):   # si le pokemon peut utiliser la competence choisie
                        if isinstance(competence, CompetenceDefense):
                            pokemon1.defendre(competence)
                        elif isinstance(competence, CompetenceAttaque):
                            pokemon1.attaquer(pokemon2, competence)
                    else:
                        print(f"Votre energie est insuffisante pour utiliser l'attaque {competence.nom} {emoji.emojize('🚫')}")

                        # si l'énergie est insuffisante pour utiliser une competence donnée on redemande-
                        # un nouveau choix au jour (on reste dans le meme tour)
                        self.tour -= 1
                    self.affichageScoreVie()  # affiche du score de vie des pokemons

                self.tour += 1

            # c'est au tour du pokemon de jouer
            else:
                print(f"C'est a {pokemon2.nom} de jouer!")
                print(pokemon2)
                print()

            # >> implémentation de l'IA sur notre code ( on a envisager de faire 3 mode different : débutant, amateur, Professionnel)
            # >> pour le mode professionnel l'idée c'est d'avoir un raisonnement  recursive qui calcule d'abord toute les attaque possible
            #     et de choisir la meilleure attaque ( cette méthode a minimum 85% de reussite du au facteur Cm son tenir compte de l'echeque de l'attaque)
            # >> la defense c'est d'utilisé une competence deffensive s'il possede sinon une competence a moin cout
            #      ( chaque pokemon possède au plus une seule competence defensive ).

                if self.niveau == 1:
                    # débutant : le pokemon de notre machine choisit des competence d'une maniere aléatoires
                    competence = pokemon2.cometenceAleatoir()

                #  niveau Amateur
                elif self.niveau == 2:
                    # Amateur : >>le pokemon defend si son energie ou sa vie inferieur a 20%
                    #           >>le pokemon choisie une competence qui a moin du cout
                    #           >>sinon le pokemon du l'environement attaque
                    if pokemon2.vieActuelle/pokemon2.vieReference < 0.2 or pokemon2.energieActuelle/pokemon2.energieReference < 0.2:
                        competence = pokemon2.meilleureCompetenceDefense()
                    elif pokemon2.energieActuelle/pokemon2.energieReference < 0.5:
                        competence = pokemon2.competenceAttaqueMoinCout()
                    else:
                        competence = pokemon2.cometenceAleatoir()

                # niveau Professionnel
                elif self.niveau == 3:
                    # Professionnel :
                    #                 >>le pokemon DEFEND ( la defense s'il possede sinon une competence a moin cout) :
                    # 1/ dans le cas ou son energie OR sa vie inferieur a 20%
                    # 2/ son energie AND sa vie inferieur a 50%  sachant que l'energie et la vie du l'adversaire supp a 50%
                    #                 >>le pokemon choisit une competence d'attaque qui a le moin du cout:
                    # 1/ dans le cas ou son energie est inferieur a 50% sachant que l'energie AND la vie du l'adversaire n'est pas supp a 50%
                    # 2/ dans le cas ou sa vie OR son energie est inferieur a 50%  sachant que son energie AND sa vie
                    #    soient inferieur a la vie AND energie du l'adversaire
                    #                 >>sinon le pokemon du l'environement attaque avec la meilleur attaque

                    if (pokemon2.vieActuelle/pokemon2.vieReference < 0.2 or pokemon2.energieActuelle/pokemon2.energieReference < 0.2) or\
                            ((pokemon2.vieActuelle/pokemon2.vieReference < 0.5 and pokemon2.energieActuelle/pokemon2.energieReference < 0.5) and\
                                (pokemon1.vieActuelle/pokemon1.vieReference > 0.5 and pokemon1.energieActuelle/pokemon1.energieReference > 0.5)):
                        competence = pokemon2.meilleureCompetenceDefense()
                    elif ( pokemon2.energieActuelle/pokemon2.energieReference < 0.5 ) or \
                            ((pokemon1.vieActuelle/pokemon1.vieReference < 0.5 or pokemon1.energieActuelle/pokemon1.energieReference < 0.5 ) and \
                            (pokemon2.vieActuelle/pokemon2.vieReference < pokemon1.vieActuelle/pokemon1.vieReference and\
                             pokemon2.energieActuelle/pokemon2.energieReference < pokemon1.energieActuelle/pokemon1.energieReference)):
                        competence = pokemon2.competenceAttaqueMoinCout()
                    else:
                        competence = pokemon2.meilleureCompetenceAttaque(pokemon1)

                if isinstance(competence, CompetenceAttaque):
                    print(f"{pokemon2.nom} a choisis de vous attaquer! {emoji.emojize('👊')}")
                    pokemon2.attaquer(pokemon1, competence)

                elif isinstance(competence, CompetenceDefense):
                    print(f"{pokemon2.nom} a choisis de ce defendre!")
                    pokemon2.defendre(competence)

                self.affichageScoreVie()
                self.tour += 1
        return pokemon1, pokemon2, self.aFuit, self.tour, self.okCapturer


    def combat(self):
        """
        cette méthode réalise un combat JCP
        """
        print(f"Combat JCP entre {self.dresseur.nom} et {self.pokemon.nom}! {emoji.emojize('👊')}{emoji.emojize('👊')}")

        # le combat prend fin si :
            # au plus une victoir pour le jouer
            # ou troi victoire pour le pokemon adverse
        while self.score[0] < 1 and self.score[1] < 3:
            print(
                f"\n=======================================   ROUND {self.round + 1}   ==============================================\n")
            pokemon1, pokemon2, aFuit, tour, okCapturer = self.roundCombat()  # jouer un round

            # si le pokemon1 à fuit le combat
            if self.aFuit:
                self.score[1] += 1
                # affcihage du scor de round dans le cas ou un des pokemon a fuit
                self.affichageScoreRound()
                break  # quitter le combat

            # si le pokemon1 à été capturer
            if self.okCapturer :
                self.score[0] += 1
                # affcihage du scor de round dans le cas ou un des pokemon2 a été capturer
                self.affichageScoreRound()
                # récompoenser le dek du dresseur gagnant
                pokemon2.miseAJour()
                self.dresseur.miseAJour()
                self.dresseur.bonusDekganantJCP(pokemon2)
                break
                # quitter le combat

            # si le pokemon2 est KO
            elif pokemon2.estKo():
                self.score[0] += 1
                #récompoenser le dek du dresseur gagnant
                pokemon2.miseAJour()
                self.dresseur.miseAJour()
                self.dresseur.bonusDekganantJCP(pokemon2)
                if self.capturer : self.dresseur.capturerPokemon(pokemon2); self.okCapturer == True
                break

            # si le pokemon 1 est KO
            elif pokemon1.estKo():
                self.score[1] += 1

            # affcihage du scor de round dans le cas ou un des pokemon est Ko
            self.affichageScoreRound()
            self.round += 1
            self.miseAJourTour()   # mise a jour des toures

        # ici on est à la fin du comba, on doit afficher les résultats final
        self.affichageScoreFinal()
        #self.miseAJourCombat()   # mise du combat  (scors, tour, roud)

    # Les getters
    @property
    def pokemon(self) :
        # un pokemon est déclarer privé dans une instace de type CombatJCP
        return self.__pokemon

    @property
    def capturer(self):
        # l'atribut capturer est priver dans un cambat JCP
        return self.__capturer

    # les setters
    @pokemon.setter
    def pokemon(self, pokemon) :
        # on s'assure que la variable "pokemon" passée en parametre est de type ( Pokemon )
        if isinstance(pokemon, Pokemon) :
            self.__pokemon = pokemon
            # on retrouen True si l'affectation est réussite, si non false puis un affiche un message d'erreur
            return True
        print(f"Erreur! la variabe que vous avez passez en parametre est de type {type(pokemon)} {emoji.emojize('🚫')}")
        return False

    @capturer.setter
    def capturer(self, capturer):
        # on s'assure que la variable "pokemon" passée en parametre est de type ( boolean )
        if capturer == True or capturer == False :
            self.__capturer = capturer
        else : print("La variale passée en parametre n'est pas de type boolean ! {emoji.emojize('🚫')}")

