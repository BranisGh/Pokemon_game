""" # # # # # # # # # # # # # # # # # # #
    #    CLASSE COMPETENCE DEFENSE      #
    # # # # # # # # # # # # # # # # # # # """

from Competence import Competence

class CompetenceDefense(Competence):
    # 1) Declaration des constructeurs
    # Constructeur "normal", tous les attributs sont connus
    def __init__(self, nom, element , description, cout, soin, energie):
        # Appel du constructeur de la super classe (Competence)
        super().__init__(nom, element, description, cout)
        self.__soin = soin
        self.__energie = energie

    # Redefinition de la surchage de l'operateur d'affichage
    def __str__(self):
        """
        cette méthode returnant les caractériqtique et evolution d'un POOkemon
        """
        s = super().__str__()
        return s

    # Redefinition de l'operateur d'egalité
    def __eq__(self, other) :
        super().__eq__(other)
        if not isinstance(other, CompetenceDefense) : return False
        if self is other : return True
        if self.__soin != other.soin : return False
        if self.__energie != other.energie : return False
        return True

    def gainEnergie(self) :
        # a revoir !!
        return self.__energie

    def gainVie(self) :
        # a revoir !!
        return self.__soin

    # Déclaration de getters
    @property
    def precision(self):
        # la précision d'une competence est privée
        return self.__precision

    @property
    def soin(self):
        # la précision d'une competence est privée
        return self.__soin