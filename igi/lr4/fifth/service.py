import numpy as np

class ArrayService:
    """
    Provides array-related services.

    Attributes:
        __arr (ndarray): The array.

    Methods:
        - get_array(): Get the current array.
        - set_array(arr): Set the array.
        - random_array(n, m): Generate a random array of shape (n, m).
        - odd_numbers(): Get the odd numbers from the array.
        - even_numbers(): Get the even numbers from the array.
        - correlation(): Compute the correlation between odd and even numbers.
        - data(): Get statistics about the array (odd count, even count, correlation).
    """

    def __init__(self):
        """
        Initializes an instance of the ArrayService class.
        """
        self.__arr = np.array([[]])

    def get_array(self):
        """
        Get the current array.

        Returns:
            ndarray: The current array.
        """
        return self.__arr
    
    def set_array(self, arr):
        """
        Set the array.

        Parameters:
            arr (ndarray): The array to set.
        """
        self.__arr = arr
    
    @staticmethod
    def random_array(n: int, m: int):
        """
        Generate a random array of shape (n, m).

        Parameters:
            n (int): Number of rows.
            m (int): Number of columns.

        Returns:
            ndarray: A random array.
        """
        return np.random.randint(100, size=(n, m))

    def odd_numbers(self):
        """
        Get the odd numbers from the array.

        Returns:
            ndarray: An array containing odd numbers.
        """
        return self.__arr[self.__arr % 2 == 1]

    def even_numbers(self):
        """
        Get the even numbers from the array.

        Returns:
            ndarray: An array containing even numbers.
        """
        return self.__arr[self.__arr % 2 == 0]
    
    def correlation(self):
        """
        Compute the correlation between odd and even numbers.

        Returns:
            float: The correlation value.
        """
        try:
            return np.corrcoef(self.odd_numbers(), self.even_numbers())[0, 1]
        except Exception as _:
            print('Correlation Cannot Be Found As Matrix Does Not Contain The Same Amount Of Odd And Even Numbers')

    def data(self):
        """
        Get statistics about the array (odd count, even count, correlation).

        Returns:
            tuple: A tuple containing the following values:
                - int: Amount of odd numbers.
                - int: Amount of even numbers.
                - float: Correlation between odd and even numbers.
        """
        return len(self.odd_numbers()), len(self.even_numbers()), self.correlation()
