class iteration:
    def __init__(self, x, n, f, math_f, eps):
        self.__x = x
        self.__n = n
        self.__f = f
        self.__math_f = math_f
        self.__eps = eps

    @property
    def x(self):
        return self.__x
    @property
    def n(self):
        return self.__n
    
    @property
    def f(self):
        return self.__f
    
    @property
    def math_f(self):
        return self.__math_f
    
    @property
    def eps(self):
        return self.__eps
    
        