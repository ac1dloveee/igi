import statistics as st
from math import sqrt

class sequence_statistics:
    def __init__(self, sequence: list):
        self.__sequence = sequence

    def __average(self):
        return sum([item.f for item in self.__sequence]) / len(self.__sequence)
    
    def __median(self):
        return st.median([item.f for item in self.__sequence])

    def __mode(self):
        return max(set(self.__sequence), key=self.__sequence.count).f
    
    def __variance(self):
        return sum([(item.f - self.__average()) ** 2 for item in self.__sequence]) / len(self.__sequence)

    def __standard_deviation(self):
        return sqrt(self.__variance())

    def stats(self):
        return {
            "average": self.__average(),
            "median": self.__median(),
            "mode": self.__mode(),
            "variance": self.__variance(),
            "standard_deviation": self.__standard_deviation()
        }
