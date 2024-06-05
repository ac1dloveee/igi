class Iteration:
    def __init__(self, x, n, f, math_f, eps):
        """
        Initializes an instance of the iteration class.

        Parameters:
            x (float): The input value.
            n (int): The iteration number.
            f (float): The result of the iterative function.
            math_f (float): The expected result from the mathematical function.
            eps (float): The desired precision.

        Attributes:
            __x (float): Stores the input value.
            __n (int): Stores the iteration number.
            __f (float): Stores the iterative function result.
            __math_f (float): Stores the expected result from the mathematical function.
            __eps (float): Stores the precision value.
        """
        self.__x = x
        self.__n = n
        self.__f = f
        self.__math_f = math_f
        self.__eps = eps

    @property
    def x(self):
        """
        Get the input value.

        Returns:
            float: The input value.
        """
        return self.__x

    @property
    def n(self):
        """
        Get the iteration number.

        Returns:
            int: The iteration number.
        """
        return self.__n

    @property
    def f(self):
        """
        Get the result of the iterative function.

        Returns:
            float: The iterative function result.
        """
        return self.__f

    @property
    def math_f(self):
        """
        Get the expected result from the mathematical function.

        Returns:
            float: The expected result from the mathematical function.
        """
        return self.__math_f

    @property
    def eps(self):
        """
        Get the desired precision.

        Returns:
            float: The precision value.
        """
        return self.__eps
