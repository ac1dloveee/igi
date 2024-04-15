import matplotlib.pyplot as mpl
from .iteration import iteration

class plot_service:
    def __init__(self):
        pass
    
    @staticmethod
    def plot_sequence(iterations: list[iteration]):
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