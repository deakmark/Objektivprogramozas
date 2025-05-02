from auto import Auto

class Szemelyauto(Auto):  # Feltételezve, hogy az Szemelyauto az Auto osztályból származik
    def __init__(self, rendszam, tipus, dij):
        super().__init__(rendszam, tipus, dij) 
