#-------------------------------------------------------------------------------
# Name:        Pojisteni
#
# Author:      Tomas Juranek
#
# Created:     26.01.2023
# Copyright:   (c) tomaash 2023
#-------------------------------------------------------------------------------

from pojisteni import Pojisteni
from pojisteny import Pojisteny

def main():
    pojisteni = Pojisteni()


    while True:
        print("\n----------------------\n Evidence pojištěných\n----------------------")
        print("Vyberte si akci:")
        print("1 - Přidat nového pojištěného")
        print("2 - Vypsat všechny pojištěné")
        print("3 - Vyhledat pojištěného")
        print("4 - Konec")
        akce = input("")
        print("")
        if akce == "1":
            jmeno = input("Zadejte jméno pojištěného: ")
            prijmeni = input("Zadejte příjmení: ")

            pokracovat = True
            while(pokracovat):
                try:
                    vek = int(input("Zadejte věk: "))
                    pokracovat = False
                except:
                    print("Toto není číslo!")
                continue

            pokracovat = True
            while(pokracovat):
                try:
                    telefon = int(input("Zadejte telefonní číslo: "))
                    pokracovat = False
                except:
                    print("Toto není číslo!")
                continue

            try:
                pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
            except ValueError as e:
                print(e)
                continue
            pojisteni.pridej_pojistence(pojisteny)

        elif akce == "2":
            pojisteni.vypis_vsechny()

        elif akce == "3":
            jmeno = input("Zadejte jméno pojištěného: ")
            prijmeni = input("Zadejte příjmení: ")
            pojisteny = pojisteni.najdi_pojistence(jmeno, prijmeni)
            if pojisteny:
                print(pojisteny)
            else:
                print("Osoba nenalezena.")

        elif akce == "4":
            print("Děkuji za použití programu >> Evidence pojištěných << \nNashledanou")
            break
        else:
            print("Chyba! \n Vyberte si z nabízených akcí.")


if __name__ == "__main__":
    main()