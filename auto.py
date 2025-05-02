from abc import ABC, abstractmethod

class Auto:
    def __init__(self, rendszam, tipus, dij):
        self.rendszam = rendszam  
        self.tipus = tipus        
        self.dij = dij            

    @abstractmethod
    def get_info(self):
        pass
