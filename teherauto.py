from auto import Auto

class Teherauto(Auto):  # Feltételezve, hogy a Teherauto is az Auto osztályból származik
    def __init__(self, rendszam, tipus, dij):
        super().__init__(rendszam, tipus, dij)  # Az Auto osztály konstruktora meghívása
