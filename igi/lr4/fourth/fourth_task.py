from .drawer import Drawer as drwr
from .figures import Triangle
from .figures import Color
from services import InputService

class Task:
    def __init__(self):
        """
        Initializes an instance of the Task class.
        """
        pass

    def __input_params(self):
        """
        Collects input parameters for creating a triangle.

        Returns:
            tuple: A tuple containing the following values:
                - a (float): Length of side a.
                - b (float): Length of side b.
                - c (float): Value of the angle between these sides.
                - clr (str): Color of the triangle.
                - name (str): Name of the figure.
        """
        a = InputService.input_specified_type(float, 'Input Length Of Side a: ')
        b = InputService.input_specified_type(float, 'Input Length Of Side b: ')
        c = InputService.input_specified_type(float, 'Input Value Of Angle Between These Sides: ')

        print(f'Available Colors: {Color.Colors.keys()}')
        clr = input('Pick One Of Them: ')

        name = input('Enter Name Of Your Figure: ')

        return a, b, c, clr, name

    def execute(self):
        """
        Executes the task to create and draw a triangle.

        Returns:
            None
        """
        drawer = drwr()
        a, b, c, clr, name = self.__input_params()

        try:
            tr = Triangle(a, b, c, clr)
            tr.name = name
        except ValueError as ve:
            print(ve)
            print('Using Default Triangle')
            tr = Triangle()
            tr.name = name

        print(tr)
        drawer.draw(tr)
