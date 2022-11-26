""" # # # # # # # # # # # # # # # # # # #
    #    CLASSE COMPETENCE ATTAQUE      #
    # # # # # # # # # # # # # # # # # # # """

from Competence import Competence
from random import randint

class CompetenceAttaque(Competence):

    #  Declaration des constructeurs
    #  Constructeur "normal", tous les attributs sont connus
    def __init__(self, nom, element , description, cout, puissance, precision):
        # Appel du constructeur de la super classe (Competence)
        super().__init__(nom, element, description, cout)
        self.__puissance = puissance
        self.__precision = precision

    # Redefinition de la surchage de l'operateur d'affichage
    def __str__(self):
        s = super().__str__()
        return s

    # Redefinition de la surcharge de l'operateur d'egalité
    def __eq__(self, other) :
        super().__eq__(other)
        if not isinstance(other, CompetenceAttaque) : return False
        if self is other : return True
        if self.__puissance != other.puissance : return False
        if self.__precision != other.precision : return False
        return True

    def attaqueReussite(self):
        """
        Cette méthode return True si l'attaque est réussite , False si non
        """
        return randint(0, 100) < self.__precision

    # Déclaration des setters
    @property
    def puissance(self):
        # la puissance d'une competence est privée
        return self.__puissance

    @property
    def precision(self):
        # la précision d'une competence est privée
        return self.__precision

