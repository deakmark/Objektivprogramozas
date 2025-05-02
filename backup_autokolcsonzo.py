from berles import Berles

class Autokolcsonzo:
    def __init__(self, nev, admin_jelszo):
        self.nev = nev
        self.admin_jelszo = admin_jelszo
        self.autok = []  # Az autók listája
        self.berlesek = []  # Az aktív bérlések listája

    def ellenoriz_admin(self):
        """Ez a metódus ellenőrzi, hogy az admin jelszó helyes-e."""
        jelszo = input("Adja meg az admin jelszót: ").strip()
        if jelszo == self.admin_jelszo:
            return True
        else:
            print("Hibás jelszó!")
            return False

    def auto_hozzaadas(self, auto):
        """Új autó hozzáadása a kölcsönzőhöz"""
        self.autok.append(auto)
    
    def auto_berlese(self, rendszam, napok):
        """Autó bérlése a kölcsönzőből"""
        for auto in self.autok:
            if auto.rendszam == rendszam:
                # Ha az autó már bérlés alatt van, nem lehet újra bérelni
                if any(b.auto.rendszam == rendszam for b in self.berlesek):
                    print("Ez az autó már bérlés alatt áll.")
                    return False
                # Ha az autó elérhető, hozzáadjuk a bérlésekhez
                self.berlesek.append(Berles(auto, napok))
                print(f"Bérlés sikeres! Az autó {napok} napra van bérelve.")
                return True
        print("Az autó nem található.")
        return False

    def berles_lemondas(self, rendszam):
        """Autó bérlésének lemondása"""
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam:
                self.berlesek.remove(berles)
                return True
        return False

    def listaz_berleseket(self):
        """Aktív bérlések listázása"""
        if not self.berlesek:
            print("Nincs aktív bérlés.")
        for berles in self.berlesek:
            print(f"{berles.auto.rendszam} - {berles.auto.tipus} - {berles.napok} napra bérelve")

    def get_berles_ar(self, rendszam, napok):
        """Bérleti díj kiszámítása"""
        for auto in self.autok:
            if auto.rendszam == rendszam:
                # Ha megtaláljuk az autót, visszaadjuk a bérleti díjat a napok számával szorozva
                return auto.dij * napok
        print("Az autó nem található.")
        return None  # Ha nincs találat, akkor None-ot adunk vissza

    def elerheto_autok(self):
        """Az elérhető autók listájának visszaadása."""
        elerheto = [auto for auto in self.autok if not any(b.auto.rendszam == auto.rendszam for b in self.berlesek)]
        if elerheto:
            print("\nElérhető autók:")
            for auto in elerheto:
                print(f"- {auto.tipus} ({auto.rendszam}), Bérleti díj: {auto.dij} Ft/nap")
        else:
            print("Jelenleg nincs elérhető autó.")


