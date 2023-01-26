class Pojisteny:
    """
    Třída reprezentující pojištěnou osobu
    """

    def __init__(self, jmeno, prijmeni, vek, telefon):
        """
        konstruktor pro vytvoreni osoby
        :param jmeno:bude ulozen s velkymi pismeny kvuli vyhledavani
        :param prijmeni:bude ulozen s velkymi pismeny kvuli vyhledavani
        :param vek:
        :param telefon:
        """
        self.jmeno = jmeno.upper()
        self.prijmeni = prijmeni.upper()
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni} ,věk:{self.vek}, telefonní číslo:{self.telefon}"
        """ 
        metoda vraci textovou podobu objektu
        """
