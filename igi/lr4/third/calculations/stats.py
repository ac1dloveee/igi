import statistics as st
from math import sqrt

class SequenceStatistics:
    def __init__(self, sequence: list):
        """
        Initializes an instance of the sequence_statistics class.

        Parameters:
            sequence (list): A list of Iteration objects.

        Attributes:
            __sequence (list): Stores the input sequence.
        """
        self.__sequence = sequence

    def __average(self):
        """
        Computes the average value of the function results in the sequence.

        Returns:
            float: The average value.
        """
        return sum([item.f for item in self.__sequence]) / len(self.__sequence)
    
    def __median(self):
        """
        Computes the median value of the function results in the sequence.

        Returns:
            float: The median value.
        """
        return st.median([item.f for item in self.__sequence])

    def __mode(self):
        """
        Computes the mode value of the function results in the sequence.

        Returns:
            float: The mode value.
        """
        return max(set(self.__sequence), key=self.__sequence.count).f
    
    def __variance(self):
        """
        Computes the variance of the function results in the sequence.

        Returns:
            float: The variance value.
        """
        return sum([(item.f - self.__average()) ** 2 for item in self.__sequence]) / len(self.__sequence)

    def __standard_deviation(self):
        """
        Computes the standard deviation of the function results in the sequence.

        Returns:
            float: The standard deviation value.
        """
        return sqrt(self.__variance())

    def stats(self):
        """
        Calculates and returns various statistical measures for the sequence.

        Returns:
            dict: A dictionary containing the following statistics:
                - "average": The average value.
                - "median": The median value.
                - "mode": The mode value.
                - "variance": The variance value.
                - "standard_deviation": The standard deviation value.
        """
        return {
            "average": self.__average(),
            "median": self.__median(),
            "mode": self.__mode(),
            "variance": self.__variance(),
            "standard_deviation": self.__standard_deviation()
        }
