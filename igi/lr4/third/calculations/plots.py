import matplotlib.pyplot as mpl
from .iteration import Iteration

class PlotService:
    def __init__(self):
        """
        Initializes an instance of the plot_service class.
        """
        pass
    
    @staticmethod
    def plot_sequence(iterations: list[Iteration]):
        """
        Plots the function values by sequence and math library.

        Parameters:
            iterations (list[Iteration]): A list of Iteration objects containing details for each iteration.

        Returns:
            None

        Saves:
            A plot in 'plot.pdf' file.

        Prints:
            'Plot Is Saved In plot.pdf'
        """
        x_points = [item.x for item in iterations]
        y_points = [item.f for item in iterations]
        math_y_points = [item.math_f for item in iterations]

        mpl.plot(x_points, y_points, color='r', label='By Sequence')
        mpl.plot(x_points, math_y_points, color='g', label='By Math Lib')

        mpl.xlabel('x')
        mpl.ylabel('ln(1 - x)')

        mpl.title('Function ln(1 - x)')
        mpl.legend()
        mpl.savefig('/home/main/igilab/l4/third/plot.pdf')

        print('Plot Is Saved In plot.pdf')

        mpl.show()
