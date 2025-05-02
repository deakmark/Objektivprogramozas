from berles import Berles
from szemelyauto import Szemelyauto
from teherauto import Teherauto

import os

class Autokolcsonzo:
    def __init__(self, nev, admin_jelszo):
        self.nev = nev
        self.admin_jelszo = admin_jelszo
        self.autok = []
        self.berlesek = []
        self.betolt_autokat()
        self.betolt_berleseket()

    def ellenoriz_admin(self):
        jelszo = input("Adja meg az admin jelszót: ").strip()
        if jelszo == self.admin_jelszo:
            return True
        else:
            print("Hibás jelszó!")
            return False

    def auto_hozzaadas(self, auto):
        self.autok.append(auto)
        self.ment_autokat()

    def auto_berlese(self, rendszam, napok):
        for auto in self.autok:
            if auto.rendszam == rendszam:
                if any(b.auto.rendszam == rendszam for b in self.berlesek):
                    print("Ez az autó már bérlés alatt áll.")
                    return False
                self.berlesek.append(Berles(auto, napok))
                self.ment_berleseket()
                print(f"Bérlés sikeres! Az autó {napok} napra van bérelve.")
                return True
        print("Az autó nem található.")
        return False

    def berles_lemondas(self, rendszam):
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam:
                self.berlesek.remove(berles)
                self.ment_berleseket()
                print("Bérlés lemondva.")
                return True
        print("Nincs ilyen bérlés.")
        return False

    def listaz_berleseket(self):
        if not self.berlesek:
            print("Nincs aktív bérlés.")
        for berles in self.berlesek:
            print(f"{berles.auto.rendszam} - {berles.auto.tipus} - {berles.napok} napra bérelve")

    def get_berles_ar(self, rendszam, napok):
        for auto in self.autok:
            if auto.rendszam == rendszam:
                return auto.dij * napok
        print("Az autó nem található.")
        return None

    def elerheto_autok(self):
        elerheto = [auto for auto in self.autok if not any(b.auto.rendszam == auto.rendszam for b in self.berlesek)]
        if elerheto:
            print("\nElérhető autók:")
            for auto in elerheto:
                print(f"- {auto.tipus} ({auto.rendszam}), Bérleti díj: {auto.dij} Ft/nap")
        else:
            print("Jelenleg nincs elérhető autó.")

    def ment_autokat(self):
        with open("autok.txt", "w", encoding="utf-8") as f:
            for auto in self.autok:
                tipus = "szemely" if isinstance(auto, Szemelyauto) else "teher"
                f.write(f"{tipus},{auto.rendszam},{auto.tipus},{auto.dij}\n")

    def betolt_autokat(self):
        try:
            with open("autok.txt", "r", encoding="utf-8") as f:
                for sor in f:
                    tipus, rendszam, nev, dij = sor.strip().split(",")
                    if tipus == "szemely":
                        auto = Szemelyauto(rendszam, nev, int(dij))
                    elif tipus == "teher":
                        auto = Teherauto(rendszam, nev, int(dij))
                    else:
                        continue
                    self.autok.append(auto)
        except FileNotFoundError:
            pass

    def ment_berleseket(self):
        with open("berlesek.txt", "w", encoding="utf-8") as f:
            for berles in self.berlesek:
                f.write(f"{berles.auto.rendszam},{berles.napok}\n")

    def betolt_berleseket(self):
        try:
            with open("berlesek.txt", "r", encoding="utf-8") as f:
                for sor in f:
                    rendszam, napok = sor.strip().split(",")
                    auto = next((a for a in self.autok if a.rendszam == rendszam), None)
                    if auto:
                        self.berlesek.append(Berles(auto, int(napok)))
        except FileNotFoundError:
            pass

    def auto_eltavolitasa(self, rendszam):
        auto = next((a for a in self.autok if a.rendszam == rendszam), None)
        if not auto:
            print("Nincs ilyen rendszámú autó.")
            return False

        if any(b.auto.rendszam == rendszam for b in self.berlesek):
            print("Ez az autó jelenleg bérlés alatt áll, nem távolítható el.")
        return False

        self.autok.remove(auto)
        self.ment_autokat()
        print("Autó sikeresen eltávolítva.")
        return True