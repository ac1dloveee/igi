import math as mt
from .iteration import iteration

class calculator:
    def __init__(self, eps):
        if eps <= 0:
            raise ValueError("Value Of 'eps' Must Be Positive")

        self.__eps = eps

    def f(self, x):
        return mt.log(1 - x)
    
    def evaluate(self, x):
        if abs(x) >= 1:
            raise ValueError("Absolute Value Of 'x' Must Be Lower Or Equal To 1")
        
        n = 1
        step = -x
        result = -x
        math_result = self.f(x)

        for n in range(1, 501):
            if abs(math_result - result) <= self.__eps:
                return iteration(x, n, result, math_result, self.__eps)
            
            step *= x * n
            step /= n + 1
            result += step

        return iteration(x, n, result, math_result, self.__eps)