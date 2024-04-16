from abc import *

class Figure(ABC):
    @abstractmethod
    def area(self):
        pass
