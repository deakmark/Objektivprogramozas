import os

class Autokolcsonzo:
    def __init__(self, nev, admin_jelszo):
        self.nev = nev
        self.admin_jelszo = admin_jelszo
        self.autok = []  # Az autók listája
        self.berlesek = []  # A bérlések listája
        self.betolt_autok()
        self.betolt_berlesek()

    def auto_hozzaadas(self, auto):
        """Hozzáad egy autót az autók listájához és elmenti a fájlba."""
        self.autok.append(auto)
        self.mement_autok()
        print(f"{auto.tipus} ({auto.rendszam}) hozzáadva.")

    def betolt_autok(self):
        """Az autók betöltése a fájlból."""
        if os.path.exists("autok.txt"):
            with open("autok.txt", "r") as f:
                for line in f:
                    data = line.strip().split(",")
                    tipus, rendszam, dij = data[0], data[1], int(data[2])
                    if tipus.lower() == "szemely":
                        self.autok.append(Szemelyauto(rendszam, data[3], dij))
                    elif tipus.lower() == "teher":
                        self.autok.append(Teherauto(rendszam, data[3], dij))

    def mement_autok(self):
        """Az autók mentése a fájlba."""
        with open("autok.txt", "w") as f:
            for auto in self.autok:
                f.write(f"{auto.__class__.__name__.lower()},{auto.rendszam},{auto.dij},{auto.tipus}\n")

    def auto_berlese(self, rendszam, napok):
        """Autó bérlése, ha elérhető, és elmenti a bérlést a fájlba."""
        auto = next((a for a in self.autok if a.rendszam == rendszam), None)
        if auto:
            # Hozzáadjuk a bérlést
            self.berlesek.append((auto, napok))
            self.mement_berlesek()
            print(f"Bérlés sikeres! Az autó {napok} napra van bérelve.")
            return True
        else:
            print(f"Az autó ({rendszam}) nem található.")
            return False

    def betolt_berlesek(self):
        """A bérlések betöltése a fájlból."""
        if os.path.exists("berlesek.txt"):
            with open("berlesek.txt", "r") as f:
                for line in f:
                    data = line.strip().split(",")
                    rendszam, napok = data[0], int(data[1])
                    auto = next((a for a in self.autok if a.rendszam == rendszam), None)
                    if auto:
                        self.berlesek.append((auto, napok))

    def mement_berlesek(self):
        """A bérlések mentése a fájlba."""
        with open("berlesek.txt", "w") as f:
            for auto, napok in self.berlesek:
                f.write(f"{auto.rendszam},{napok}\n")
