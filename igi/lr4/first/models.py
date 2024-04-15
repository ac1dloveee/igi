import random as rndm

class history_event:
    def __init__(self, name: str, century: int):
        self.__name = name
        self.__century = century

    @property
    def name(self):
        return self.__name
    
    @property
    def century(self):
        return self.__century
    
    @name.setter
    def name(self, name: str):
        self.__name = name

    @century.setter
    def century(self, century: int):
        self.__century = century

    @staticmethod
    def main_events():
        events = [
            history_event("First mention of the towns Turov and Polotsk", 9),
            history_event("Foundation of the Kievan Rus", 10),
            history_event("Start of the spread of Christianity in Belarus", 10),
            history_event("Battle on the Nemiga, first mention of Minsk", 11),
            history_event("Foundation of the Grand Duchy of Lithuania", 13),
            history_event("Battle of Tannenberg", 15),
            history_event("Adoption of Magdeburg Law in Minsk", 15),
            history_event("Union of Lublin, founding of Poland-Lithuania", 16),
            history_event('Great Northern War', 18),
            history_event('Development and establishment of the Jesuit academy in Polots', 19),
            history_event('October Revolution, Proclamation of Soviet rule in Belarus', 20),
            history_event('First World War', 20),
            history_event('Outbreak of the Great Patriotic War (Russian for Second World War)', 20)
        ]

        rndm.shuffle(events)
        return events