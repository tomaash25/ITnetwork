
from pojisteny import Pojisteny

class Pojisteni:

    """
    Třída reprezentující správu pojištěných
    """

    def __init__(self):
        self.seznam_pojistenych = []
    """ konstruktor  deklarace seznamu"""

    def pridej_pojistence(self, pojisteny):
        self.seznam_pojistenych.append(pojisteny)


    def vypis_vsechny(self):
        for pojisteny in self.seznam_pojistenych:
            print(pojisteny)

    def najdi_pojistence(self, jmeno, prijmeni):
        jmeno = jmeno.upper()
        prijmeni = prijmeni.upper()
        for pojisteny in self.seznam_pojistenych:
            if pojisteny.jmeno.upper() == jmeno and pojisteny.prijmeni.upper() == prijmeni:
                return pojisteny
        return None
