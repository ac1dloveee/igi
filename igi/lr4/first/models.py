import random as rndm

class HistoryEvent:
    """
    A class to represent a historical event.

    Attributes:
        name (str): The name of the event.
        century (int): The century in which the event occurred.

    Methods:
        __init__(self, name: str, century: int): Initializes a new instance of the HistoryEvent class.
        name(self): Gets the name of the event.
        century(self): Gets the century in which the event occurred.
        name.setter(self, name: str): Sets the name of the event.
        century.setter(self, century: int): Sets the century in which the event occurred.
        main_events(self): Returns a list of main events in the history of Belarus.
    """

    def __init__(self, name: str, century: int):
        self.__name = name
        self.__century = century

    @property
    def name(self):
        """
        Gets the name of the event.

        Returns:
            str: The name of the event.
        """
        return self.__name
    
    @property
    def century(self):
        """
        Gets the century in which the event occurred.

        Returns:
            int: The century in which the event occurred.
        """
        return self.__century
    
    @name.setter
    def name(self, name: str):
        """
        Sets the name of the event.

        Args:
            name (str): The new name of the event.
        """
        self.__name = name

    @century.setter
    def century(self, century: int):
        """
        Sets the century in which the event occurred.

        Args:
            century (int): The new century in which the event occurred.
        """
        self.__century = century

    @staticmethod
    def main_events():
        """
        Returns a list of main events in the history of Belarus.

        Returns:
            list: A list of main events in the history of Belarus.
        """
        events = [
            HistoryEvent("First mention of the towns Turov and Polotsk", 9),
            HistoryEvent("Foundation of the Kievan Rus", 10),
            HistoryEvent("Start of the spread of Christianity in Belarus", 10),
            HistoryEvent("Battle on the Nemiga, first mention of Minsk", 11),
            HistoryEvent("Foundation of the Grand Duchy of Lithuania", 13),
            HistoryEvent("Battle of Tannenberg", 15),
            HistoryEvent("Adoption of Magdeburg Law in Minsk", 15),
            HistoryEvent("Union of Lublin, founding of Poland-Lithuania", 16),
            HistoryEvent('Great Northern War', 18),
            HistoryEvent('Development and establishment of the Jesuit academy in Polots', 19),
            HistoryEvent('October Revolution, Proclamation of Soviet rule in Belarus', 20),
            HistoryEvent('First World War', 20),
            HistoryEvent('Outbreak of the Great Patriotic War (Russian for Second World War)', 20)
        ]

        rndm.shuffle(events)
        return events