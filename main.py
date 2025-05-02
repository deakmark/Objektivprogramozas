from autokolcsonzo import Autokolcsonzo
from szemelyauto import Szemelyauto
from teherauto import Teherauto

def main():
    kolcsonzo = Autokolcsonzo("Deák Márk Autókölcsönzője", "admin123")

    print("=" * 40)
    print("   🚗 Deák Márk Autókölcsönzője 🚗")
    print("=" * 40)

    # Előre feltöltött autók
    #kolcsonzo.auto_hozzaadas(Szemelyauto("ABC-123", "Opel Astra", 10000))
    #kolcsonzo.auto_hozzaadas(Teherauto("XYZ-987", "Ford Transit", 15000))
    #kolcsonzo.auto_hozzaadas(Szemelyauto("QWE-456", "Suzuki Swift", 9000))
    #kolcsonzo.auto_hozzaadas(Szemelyauto("RRR-123", "Fiat Punto", 6000))

    while True:
        print("\n1. Autó bérlése")
        print("2. Bérlés lemondása")
        print("3. Bérlések listázása")
        print("4. Új autó hozzáadása")
        print("5. Elérhető autók listázása")
        print("6. Autó eltávolítása")
        print("0. Kilépés")

        valasztas = input("Választás: ")

        if valasztas == "1":
            rendszam = input("Adja meg az autó rendszámát: ")
            napok = int(input("Hány napra szeretné bérelni? "))
            if kolcsonzo.auto_berlese(rendszam, napok):
                ar = kolcsonzo.get_berles_ar(rendszam, napok)
                if ar is not None:
                    print(f"Bérlés sikeres. Ár: {ar} Ft")
                else:
                    print("Bérleti díj nem elérhető.")
        
        elif valasztas == "2":
            # Bérlés lemondása logika
            rendszam = input("Add meg a lemondani kívánt autó rendszámát: ")
            if kolcsonzo.berles_lemondas(rendszam):
                print("Bérlés sikeresen lemondva.")
            else:
                print("Nem található ilyen bérlés.")
        
        elif valasztas == "3":
            # Bérlések listázása logika
            kolcsonzo.listaz_berleseket()

        elif valasztas == "4":
            if kolcsonzo.ellenoriz_admin():
                auto_tipus = input("Típus (szemely/teher): ").strip().lower()
                rendszam = input("Rendszám: ")
                tipus = input("Típusnév: ")
                dij = int(input("Bérleti díj (Ft/nap): "))

                if auto_tipus == "szemely":
                    kolcsonzo.auto_hozzaadas(Szemelyauto(rendszam, tipus, dij))
                elif auto_tipus == "teher":
                    kolcsonzo.auto_hozzaadas(Teherauto(rendszam, tipus, dij))
                else:
                    print("Ismeretlen típus.")
            else:
                print("Nincs jogosultsága autó hozzáadására.")
        elif valasztas == "5":
            kolcsonzo.elerheto_autok()
        elif valasztas == "6":
            rendszam = input("Adja meg az eltávolítandó autó rendszámát: ")
            kolcsonzo.auto_eltavolitasa(rendszam)
        elif valasztas == "0":
            break
        else:
            print("Érvénytelen választás.")

if __name__ == "__main__":
    main()
