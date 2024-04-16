from matplotlib import colors
from matplotlib.typing import ColorType

class Color:
    """
    Represents a color using its name.

    Attributes:
        Colors (dict): A dictionary of base colors available in matplotlib.
        __color (str): The name of the color.

    Methods:
        - color (property): Get the name of the color.
    """

    Colors = colors.BASE_COLORS

    def __init__(self, color: str):
        """
        Initializes an instance of the Color class.

        Parameters:
            color (str): The name of the color.
        """
        self.__color = color

    @property
    def color(self):
        """
        Get the name of the color.

        Returns:
            str: The name of the color.
        """
        return self.__color
