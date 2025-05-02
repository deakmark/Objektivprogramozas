class Berles:
    def __init__(self, auto, napok):
        self.auto = auto  # Az autó objektum
        self.napok = napok  # Bérlés napjainak száma

    def get_osszeg(self):
        return self.auto.berleti_dij

    def __str__(self):
        return f"{self.auto.rendszam} bérlése {self.datum} napra, Ár: {self.get_osszeg()} Ft"
    
    
def auto_berlese(self, rendszam, napok):
    for auto in self.autok:
        if auto.rendszam == rendszam:
            if any(b.auto.rendszam == rendszam for b in self.berlesek):
                print("Ez az autó már bérlés alatt van.")
                return False
            self.berlesek.append(Berles(auto, napok))
            self.ment_berleseket()  # <-- mentés
            print(f"Bérlés sikeres! Az autó {napok} napra van bérelve.")
            return True
    print("Nem található ilyen rendszámú autó.")
    return False