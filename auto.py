from abc import ABC, abstractmethod

class Auto:
    def __init__(self, rendszam, tipus, dij):
        self.rendszam = rendszam  # Az autó rendszáma
        self.tipus = tipus        # Az autó típusa
        self.dij = dij            # Bérleti díj

    @abstractmethod
    def get_info(self):
        pass
