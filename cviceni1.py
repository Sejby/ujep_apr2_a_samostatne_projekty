# státnice budou z každého předmětu, 1. otázka
# zápočet bude program na 2 hodiny bez internetu naprogramovat, pak na ústní s programem k fišerovi

# kachni typovani
''' def zamnoukej(kocka):
    print(f"Kočka {kocka['jmeno']} mnouka mnaumnau")

def main():
    mica = {
        "jmeno" : "Mica",
        "vek" : 2,
        "majitele" : ["Jiri", "Jakub"]
    }
    zamnoukej(kocka=mica)
    
main() '''


import random
class Kocka:
    max_pocet_kocek_na_svete = 10 #datový člen/atribut třídy
    
    #initor
    def __init__(self, jmeno, vek, majitele) -> None: 
        self._jmeno = jmeno     #atributy (v pythonu datové členy)
        self._vek = vek
        self._majitele = majitele
    
    @classmethod
    def jak_dela_kocka(cls):
        print(cls.max_pocet_kocek_na_svete)
        return "Mnau"
    
    @staticmethod
    def jak_nedela_kocka():
        return "vselijak jenom ne mnau"
    
    @property
    def jmeno(self):
        return self._jmeno
    
    @property
    def majitele(self):
        return self._majitele
    
    @property
    def vek(self):
        return self._vek
    #setter
    @jmeno.setter
    def jmeno(self, value):
        self._jmeno = value if len(value) > 3 else self._jmeno

    def mnoukej(self):
        print(f"Kocka {self._jmeno} mnouka mnouk mnouk")
    #metody (funkce uvnitř tříd)
    
    def vykad_se(self, kam):
        print(f"Kocka {self._jmeno} se vykadila do {kam}")
    
    #magicke metody / dandr metody (napr. přetěžování operátorů)
    def __ge__(self, other): #přetěžování operátoru >=
        if not isinstance(other, Kocka):
            raise Exception(f"Objekt {other} neni kocka!")
        else:
            return self._vek >= other.vek

    # Napište funkci, která přetěžuje operátor + a to tak, že pokud sečtu dvě kočky, tak vznikne kotatko (nova kočka).
    # Jmeno bude spojeni jmen obou kocek
    # vek = 1, majitele bude nahodny vyber z majitelu obou kocek
    
    def __add__(self, other):
        if not isinstance(other, Kocka):
            raise Exception("Error")
        else:
            pole_majitelu = self._majitele + other.majitele
                
            kotatko = Kocka(jmeno={self._jmeno + other.jmeno}, vek=1, majitele=random.choice(pole_majitelu))
            return kotatko.jmeno
        
    
    
def main():
    #objekt je instancí (zhmotněním) třídy
    mica = Kocka(jmeno="Mica", vek=5, majitele=["Petr", "Milan"])
    mikes = Kocka(jmeno="Mikeš", vek=3, majitele=["Alex"])
    # print(mica >= mikes) #mica.__ge__(other=mikes)
    print(mica + mikes)
    print(Kocka.jak_dela_kocka())
    
main()