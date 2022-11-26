from optionAndDataBase import *
from CombatJCJ import CombatJCJ
from CombatJCP import CombatJCP
from fonctionsUtiles import *
import pandas as pd
from ChampionnatJCJ import *
from ChampionnatJCP import *
import json
import emoji
from Championnat import Championnat
from Dresseur import Dresseur

"""
pour la récupération des données fournie on a voulu crée des classeurs xlsx pour utilisé des méthode de 
base de données afin de bien gérer nos donnée et pouvoir crée un autre classeur pour stocké et récuperer les
les dressseurs et le championat pour cela on a converti le fichier text en excel.

"""
# récupération des fichier text fournie ( pokemon , attaque , defense )

pokemons = []              # liste des pokemons fournie
experience = 0            # initialisation de l'experience de chaque pokemon a 0  ( a la récuperation tout les pokemon/
                           # n'ont pas d'experience)

tab = pd.read_excel("pokemon.xlsx")                # utilisation de la bibliothèque pandas pour la recuperation
tab_attaque = pd.read_excel("attaque.xlsx")        # on a préférer fertiliser des classeurs excel pour utiliser les /
tab_defense = pd.read_excel("defense.xlsx")        # bases de données afin de stoquée et récuperer librement


for i in range(len(tab)):
    listeCompetences = []                           # c'est la liste des compétence pour chaque pokemon
    str_competences = tab.iloc[i][9][1:-1].split(', ')
    pokemons.append(Pokemon(nom = tab.iloc[i][0],    # création des pokemons
                             element = tab.iloc[i][3],
                             niveau = tab.iloc[i][4],
                             experience = 0,
                             vie = tab.iloc[i][5],
                             energie = tab.iloc[i][6],
                             regenerationEnergie = tab.iloc[i][7],
                             resistance = tab.iloc[i][8],
                             ))
    pokemons[i].apres= tab.iloc[i][2]  # récuperer la forme future de chaque pokemon apres la transformation pour l'option

             # afin de respecter la relation de composition entre pokemon et comptence on a utiliser la methode:
    for competence in str_competences:          # ajouterCompetenceAttaque si c'est une competence d'attaque
        if competence in tab_attaque["Nom"].to_list():
            pokemons[i].ajouterCompetenceAttaque(nom = competence,
                                                 element = tab_attaque[tab_attaque["Nom"] == competence].iloc[0][
                                                     "Element"],
                                                 description = tab_attaque[tab_attaque["Nom"] == competence].iloc[0][
                                                     "Description"],
                                                 cout = tab_attaque[tab_attaque["Nom"] == competence].iloc[0]["Cout"],
                                                 puissance = tab_attaque[tab_attaque["Nom"] == competence].iloc[0][
                                                     "Puissance"],
                                                 precision = tab_attaque[tab_attaque["Nom"] == competence].iloc[0][
                                                     "Precision"])
        elif competence in tab_defense["Nom"].to_list(): # ajouterCompetenceDefence si c'est une competence defensive
            pokemons[i].ajouterCompetenceDefense(nom = competence,
                                                 element = tab_defense[tab_defense["Nom"] == competence].iloc[0][
                                                     "Element"],
                                                 description = tab_defense[tab_defense["Nom"] == competence].iloc[0][
                                                     "Description"],
                                                 cout = tab_defense[tab_defense["Nom"] == competence].iloc[0]["Cout"],
                                                 soin = tab_defense[tab_defense["Nom"] == competence].iloc[0]["Soin"],
                                                 energie = tab_defense[tab_defense["Nom"] == competence].iloc[0][
                                                     "Energie"])

# l'objet pokemon est crée on passe au jeux d'instruction
########################################################################################################################
"""
notre menu est composer de d'un menu principale afin de cree ou chargé un joueur ensuite on passe au menu
secondaire pour choisir les different option et mode de jeux ainsi de pouvoir jouer !!!
"""

message_debut = """                                                    #----------------------------------------#
                                                    #        Bienvenue dans POOkemon!        #
                                                    #    le jeu de Pokemon Oriente Objet :D  #
                                                    #----------------------------------------#
                                                    """
menuPrincipal = \
f"""                                
                                                        # ======== MENU PRINCIPAL  ======== #
                                                        # ======== --------------- ======== #
                                    
1\ Charger mon dresseur
2\ Créer un dresseur
3\ Quitter
    {emoji.emojize('👉')} Que voulez vous faire ?  """

# liste des indice du menu principale, (les choix possible)
listeMenuPrincipal = ["1", "2","3"]

# menu principale
menuSecondaire = \
f"""                                
                                                      # ======== MENU SECONDAIRE ======== #
                                                      # ======== --------------- ======== #
                                    
1\ Changer mon dek
2\ Entrainement / capturer un pokemon
3\ Combattre un autre deresseur
4\ Championat 
5\ Enregistrer/Supprimer un dresseur 
6\ Retour au menu principale
    {emoji.emojize('👉')} Que voulez vous faire ?  """

# liste des indices du menu secondaire (les choix possible)
listeMenuSecon2daire = ["1", "2", "3", "4", "5", "6"]

# les indices des pokemon dans la base de données
indicePokemon = [str(i + 1) for i in range(len(pokemons))]

# message de depart
print(message_debut)
print()

            # ==================================== MENU 1 ===========================================#
            #===================================== ------ ============================================#
while True :
    # saisire son choix du menu principal
    choix = saisieChoix(menuPrincipal, listeMenuPrincipal)
    print()
    # charger un dresseur dans la base de donées
    if choix == 1:
        dresseurs = fileDresseurToListe('dresseurs.txt')  # recuperer la liste des dresseur déja stockés dans liste
        if len(dresseurs) > 0:
            dresseur1 = chargerDresseur(dresseurs)
            print()
            print(dresseur1.dekToString())              # afficher le dek du dresseur recuperer
            print()
        else:
            print("vous n'avez pas de dresseur deja sauvgardés, vous devez cree un pour jouer")
            print()
            choix = 2  # on est obligé de choisir l'option cree un dresseur car on n'as pas de dresseur à charger

    # création d'un nouveua dresseur
    if choix == 2:  # ici on a pas fait le "elif"  car on veux que à chaque fois tester cette condition
        dresseur1 = creerDresseur(pokemons)      # cree un dresseur
        print()
        print(dresseur1.dekToString())           # afficher les pokemon du dresseur
        print()

    # quitez le combat
    elif choix == 3:
        print()
        print(f"Vous avez quittez le jeu! A bientot {emoji.emojize('👋')}")
        break  # quiter le jeux

        # ==================================== MENU 2 =========================================== #
        # ==================================== ------ =========================================== #

    # apres avoir fait le choix du menu principale, un second s'affiche!
    while True :
        # recuperer le choix du menu 2
        choix = saisieChoix(menuSecondaire, listeMenuSecon2daire)

        # changer le dek du dresseur
        if choix == 1 :
            print()
            dresseur1.changerDek()
            print()

        # combat dresseurJCP
        elif choix == 2:
            
            # affichge des pokemon récupeprer dans la base de données
            print(pokemonToString(pokemons))                          # affichege de la liste des pokemon
            print(f"   {emoji.emojize('👉')} Quel pokemon souhaitez-vous combattre ? ")
            pokemon  = pokemonACombattre(pokemons)                    # recuperer le pokemon choisie
            print()
            niveau = niveauDifficulte() # recuperer le niveau de difficulté
            print()
            capturer  = modeCombat()    # recuprrer le mode du combat capturer/entrainement
            print()
            # crée un combat JCP
            combat = CombatJCP(dresseur1, pokemon, capturer, niveau)
            combat.combat()
            transDresseur(dresseur1, pokemons)
            transformation(pokemon, pokemons)  # option de transformation de pokemon
            print()

        # combat dresseurJCJ
        elif choix == 3:
            menuChoixDresseur2 = f"1/ Charger mon dresseur \n2/ Créer un deuxième dresseur\n   {emoji.emojize('👉')} Que voulez-vous faire ? "
            print()
            # recuperer le choix (charger ou cree un dresseur)
            choix = saisieChoix(menuChoixDresseur2, ["1", "2"])

            # changer de dresseur
            if choix == 1:
                # recuper les dressurs stockés dans une base de données en une liste
                dresseurs = fileDresseurToListe('dresseurs.txt')
                # si il existe un/des dresseur déja sauvgardés
                if len(dresseurs) > 0 :
                    dersseur2 = chargerDresseur(dresseurs)
                    # affichege du dek du dresseur
                    print()
                    print(dersseur2.dekToString())
                    print()
                    # cree un combat
                    combat = CombatJCJ(dresseur1, dersseur2)
                    combat.combat()
                    transDresseur(dresseur1, pokemons)  # option transformation
                    transDresseur(dersseur2, pokemons)
                    print()
                else :
                    print("vous n'avez pas de dresseur deja sauvgardés, vous devez cree un pour jouer")
                    choix = 2   # dans ce cas il faut choisir l'option cree un dresseur
                    print()

            # Cree un deuxième dressseur
            if choix == 2:   # cette condition on devrai la tester à chaque fois car il se peut que on a pas de dresseur a charger
                dersseur2 = creerDresseur(pokemons)      # cree un dresseur
                # afficher le de du dresseur
                print()
                print(dersseur2.dekToString())
                print()
                # cree un combatJCJ
                combat = CombatJCJ(dresseur1, dersseur2)
                combat.combat()   # combattre
                transDresseur(dresseur1, pokemons)  # option transformation
                transDresseur(dersseur2, pokemons)
                print()

        elif choix == 4:
            
            #  choisir un championnat JCJ ou JCP
            print("\n")
            choix = saisieChoix(f"1\ ChampionnatJCJ \n2\ ChampionnatJCP \n   {emoji.emojize('👉')} Que voulez vous faire ? ", ["1", "2"])

            # si on choisis un championnat JCJ
            if choix == 1 :

                # Initialisation de la liste des joueurs participants au championnat
                joueurs = []

                # D'abord ajouter le dresseur choisis dans le menu principale
                #joueurs.append(dresseur1)

                # Initilaisation du menu
                menu = f"""                                
    1\ Charger mon dresseur
    2\ Créer un dresseur
        {emoji.emojize('👉')} Que voulez vous faire ?  """

                # choisir le nombre maximum de participants (4 , 8, 16)
                    # 4 est le nombre minimum de particiants pour organiser un tournoi
                    # 16 est le nombre maximum de particiants pour organiser un tournoi

                choix = saisieChoix("combient de participant souhaitez-vous ? (4, 8 ou 16) ", ["4", "8", "16"])

                # remplissage de la liste, avec les joueurs participants au championnat
                for i in range(choix - 1) :
                    # saisire son choix du menu
                    print(f"\n\nJoueur numero {i+2} en attente d'inscription...")
                    choix = saisieChoix(menu, ["1", "2"])
                    print()
                    # charger un dresseur dans la base de donées
                    if choix == 1:
                        dresseurs = fileDresseurToListe('dresseurs.txt')  # recuperer la liste des dresseur déja stockés dans liste
                        if len(dresseurs) > 0:
                            dresseur = chargerDresseur(dresseurs)
                            print()
                            print(dresseur.dekToString())              # afficher le dek du dresseur recuperer
                            print()
                        else:
                            print("vous n'avez pas de dresseur deja sauvgardés, vous devez cree un pour jouer")
                            print()
                            choix = 2  # on est obligé de choisir l'option cree un dresseur car on n'as pas de dresseur à charger

                    # création d'un nouveua dresseur
                    if choix == 2:  # ici on a pas fait le "elif"  car on veux que à chaque fois tester cette condition
                        dresseur = creerDresseur(pokemons)      # cree un dresseur
                        print()
                        print(dresseur.dekToString())           # afficher les pokemon du dresseur
                        print()

                        # ajouter le dresseur cree dans la liste des joueurs participents au championnat
                    joueurs.append(dresseur)

                # Création d'un championnat on lui passant la liste des participant en parametre
                print()
                championnatJCJ = ChampionnatJCJ(dresseur1, joueurs)

                # Affichage du calendrier des combats
                championnatJCJ.championnat()
                transJoueurs(joueurs, pokemons)  # option transformation
        
        
            # si on a choisie un championnat JCP
            elif choix == 2 :

                print('\n')
                print("c'est patrie à la chasse aux pokemon ... 🎃")

                # initiliser la liste des pokemons participants
                pokemonsCham = []

                choix1 = saisieChoix(f"combient de participant souhaitez-vous ? (4, 8 ou 16) ", ["4", "8", "16"])
                print()
                choix2 = saisieChoix(f"1\ pokemons génerés aleatoirement \n2\ pokemons choisis par l'utilisateur \n  {emoji.emojize('👉')} Que voulez vous faire ?  ? ", ["1", "2"])

                # si on a choisie de générer des pokemon aleatoirement
                if choix2 == 1 :
                    pokemonsCham = [deepcopy(pokemons[randint(0, len(pokemons))]) for i in range(choix1)]
                
                # si on a choisis l'option de choisir les pokemon à combatre
                elif choix2 == 2 :
                    
                    # affichge des pokemon récupeprer dans la base de données
                    print(pokemonToString(pokemons))
                    for i in range(choix1) :
                        print()
                        choix = saisieChoix(f"pokemon numero {i+1} en attente d'inscriptions ...\n   {emoji.emojize('👉')} Quel pokemon souhaitez-vous combattre ?", [str(i) for i in range(len(pokemons))])
                        pokemonsCham.append(deepcopy(pokemons[choix-1]))
            
                # Création d'un championnat on lui passant la liste des participant en parametre
                print()
                championnatJCP = ChampionnatJCP(dresseur1, pokemonsCham)
                    
                # Affichage du calendrier des combats
                championnatJCP.championnat()
                transDresseur(dresseur1, pokemons)  # option transformation
                transformation(pokemonsCham, pokemons)
        # Enregistrer ou suprimer un pokemon!   ######################################"
        elif choix == 5:
            menuChoixEnregistrerSupprimer = f"1/ Enregistrer \n2/ Supprimer \n  {emoji.emojize('👉')} Que voulez-vous ?\n"
            choix = saisieChoix(menuChoixEnregistrerSupprimer, ["1", "2"])

            # Enregistrer un pokemon
            if choix == 1 :
                try:
                    # choisire le dresseur que vous voulez suprimer
                    menuChoixEnregistrer = f"1/ dresseur : {dresseur1.nom} \n2/ dresseur : {dersseur2.nom} \n   {emoji.emojize('👉')} Que voulez-vous enregistrer?\n"

                    choix = saisieChoix(menuChoixEnregistrer, ["1", "2"])
                    if choix == 1:
                        # enregistrement du dresseur 1
                        enregistrement(dresseur1, 'dresseurs.txt')
                        # enregistrement du dresseur 2
                    elif choix == 2:
                        enregistrement(dersseur2, 'dresseurs.txt')
                except:
                    menuChoixEnregistrer2 = f"\n1/ oui \n2/ non\n  {emoji.emojize('👉')} souhaitez-vous enregistrer {dresseur1.nom} ? "
                    choix = saisieChoix(menuChoixEnregistrer2, ["1", "2"])

                    if choix == 1:
                        enregistrement(dresseur1, 'dresseurs.txt')

                    elif choix == 2:
                        print("\npas de soucis ")

            # suprimer le dresseur
            elif choix == 2:
                dresseurs = fileDresseurToListe('dresseurs.txt')
                if len(dresseurs) == 0 :
                    print("aucun dresseur!!!!")


                else :
                    # recuperer les indices des dresseurs dans la liste "dresseur"
                    indiceDresseur = [str(i + 1) for i in range(len(dresseurs))]
                    print(dresseurToString(dresseurs))
                    print("Quel dresseur souhaitez-vous supprimer")
                    # recuperer l'indiced du dresseur à supprimer
                    indice = choixIndice(indiceDresseur) - 1
                    # suprimer le dresseur choisie
                    supprimerDresseur(indice)
                    print(f"le dresseur {dresseurs[indice].nom} est supprimer")


            else :
                print("\nJe n'ai pas compris votre choix ")

        # retourn au menu principale
        elif choix == 6:
            print()
            break

        else :
            print ("\nJ'ai pas compris votre choix ")

