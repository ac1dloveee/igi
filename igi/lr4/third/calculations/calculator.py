import math as mt
from .iteration import Iteration

class Calculator:
    def __init__(self, eps):
        """
        Initializes an instance of the Calculator class.

        Parameters:
            eps (float): The desired precision (positive value).

        Raises:
            ValueError: If eps is not positive.
        """
        if eps <= 0:
            raise ValueError("Value Of 'eps' Must Be Positive")

        self.__eps = eps

    def f(self, x):
        """
        Computes the function value for a given x.

        Parameters:
            x (float): Input value.

        Returns:
            float: The result of mt.log(1 - x).
        """
        return mt.log(1 - x)
    
    def evaluate(self, x):
        """
        Evaluates the function using an iterative method.

        Parameters:
            x (float): Input value.

        Returns:
            iteration(x, n, result, math_result, self.__eps): An object containing iteration details.

        Raises:
            ValueError: If the absolute value of x exceeds 1.
        """
        if abs(x) >= 1:
            raise ValueError("Absolute Value Of 'x' Must Be Lower Or Equal To 1")
        
        n = 1
        step = -x
        result = -x
        math_result = self.f(x)

        for n in range(1, 501):
            if abs(math_result - result) <= self.__eps:
                return Iteration(x, n, result, math_result, self.__eps)
            
            step *= x * n
            step /= n + 1
            result += step

        return Iteration(x, n, result, math_result, self.__eps)
