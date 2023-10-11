from abc import ABC, abstractmethod

class Cloneable(ABC):
    
    @abstractmethod
    def clone(self):
        pass