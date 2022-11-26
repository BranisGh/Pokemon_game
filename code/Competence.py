""" # # # # # # # # # # # # # # # # # # #
    #            CLASSE COMPETENCE      #
    # # # # # # # # # # # # # # # # # # # """

"""
    Competence est une super class abstrette
"""
from abc import ABC, abstractmethod

class Competence(ABC):
    # 1) Declaration des constructeurs
    # 1-a) Constructeur "normal", tous les attributs sont connus
    def __init__(self, nom, element, description, cout):
        self.__nom = nom
        self.__element = element
        self.__description = description
        self.__cout = cout

    # 3) Surchage de l'operateur d'affichage
    def __str__(self):
        """
        cette méthode returnant les caractériqtique et evolution d'un POOkemon
        """
        s = f"{self.__nom} ({self.__description}, {self.__element}, cout: {self.__cout}) "
        #s += f"{self.description}"
        return s

    # surchage de l'opperateur d'égalité pour la classe compétence car
    # pour ajouté une compétence à un pokemon on doit d'abord vérifier que
    # la compétence n'existe pas  pas dans sa liste de competence
    def __eq__(self, other) :
        if not isinstance(other, Competence) : return False
        if self is other : return True

        if self.__nom != other.nom : return False
        if self.__description != other.description : return False
        if self.__element != other.element : return False
        if self.__cout != other.cout : return False
        return True

    # Déclaration des getters
    @property
    def nom(self) :
        # le nom de la competence est privé
        return self.__nom

    @property
    def element(self) :
        # l'element de la competenceest privé
        return self.__element

    @property
    def description(self) :
        # la description d'une competence est privée
        return self.__description

    @property
    def cout(self) :
        # le coup d'une competence est privé
        return self.__cout

    """
    Ici on a fait le choix de ne pas mettre des setters pour les attributs d'une competence, car les competence elle sont 
    propres aux pokemon (relation de composition), elles seront crées directement dans l'instance d'un pokemon (conseille de Mr.TomaDetebeck)
    et elle ne chagent pas 
    """