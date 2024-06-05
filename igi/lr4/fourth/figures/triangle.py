from .figure import Figure
import math as mt
from .color import Color as clr

class Triangle(Figure):
    """
    Represents a triangle.

    Attributes:
        __a (float): Length of side a.
        __b (float): Length of side b.
        __c (float): Value of the angle between these sides (in degrees).
        __color (Color): Color of the triangle.
        __name (str): Name of the figure.

    Methods:
        - area(): Calculates the area of the triangle.
        - get_color(): Gets the color of the triangle.
        - available_colors(): Returns available color options.
        - points(): Returns the coordinates of the triangle's vertices.
    """

    def __init__(self, a=3, b=4, c=90, color='r'):
        """
        Initializes an instance of the Triangle class.

        Parameters:
            a (float): Length of side a.
            b (float): Length of side b.
            c (float): Value of the angle between these sides (in degrees).
            color (str): Color of the triangle.

        Raises:
            ValueError: If side lengths or angle are invalid.
        """
        if not color in clr.Colors.keys():
            raise ValueError('Unknown Color')
        
        if a <= 0 or b <= 0:
            raise ValueError('Length Of Side Must Be Positive')

        if c <= 0 or c >= 180:
            raise ValueError('Angle Must Be In 0..180')

        self.__a = a
        self.__b = b
        self.__c = c
        self.__color = clr(color)
        self.__name = ''

    @property
    def name(self):
        """
        Get the name of the triangle.

        Returns:
            str: The name of the triangle.
        """
        return self.__name
    
    @name.setter
    def name(self, value):
        """
        Set the name of the triangle.

        Parameters:
            value (str): The name to set.
        """
        self.__name = value

    def area(self):
        """
        Calculates the area of the triangle.

        Returns:
            float: The area of the triangle.
        """
        return (self.__a * self.__b * mt.sin(self.__rad(self.__c))) / 2.0
    
    def __str__(self):
        """
        Returns a string representation of the triangle.

        Returns:
            str: A formatted string describing the triangle.
        """
        return 'Triangle; a={}, b={}, c={}, area={}.'.format(
            self.__a, self.__b, self.__c, self.area())
    
    def get_color(self):
        """
        Gets the color of the triangle.

        Returns:
            str: The color of the triangle.
        """
        return self.__color.color

    def available_colors(self):
        """
        Returns available color options.

        Returns:
            list: A list of available color names.
        """
        return clr.colors().keys()
    
    def __rad(self, vl: float):
        """
        Converts degrees to radians.

        Parameters:
            vl (float): Angle in degrees.

        Returns:
            float: Angle in radians.
        """
        return mt.pi * vl / 180.0

    def points(self):
        """
        Returns the coordinates of the triangle's vertices.

        Returns:
            list: A list of tuples representing the vertices' coordinates.
        """
        return [
            (1, 1),
            (1 + self.__b, 1),
            (1 + self.__a * mt.cos(self.__rad(self.__c)), 1 + self.__a * mt.sin(self.__rad(self.__c)))]
