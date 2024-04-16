import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Drawer:
    def __init__(self):
        """
        Initializes an instance of the Drawer class.
        """
        pass

    def draw(self, figure):
        """
        Draws a polygon based on the provided figure.

        Parameters:
            figure: An object representing the figure (e.g., triangle).

        Returns:
            None

        Saves:
            A plot in 'plot.pdf' file.

        Prints:
            'Plot Is Saved In /home/main/igilab/l4/fourth/plot.pdf'
        """
        polygon = patches.Polygon(figure.points(), color=figure.get_color(), label=figure.name)
        _, ax = plt.subplots()

        ax.add_patch(polygon)
        ax.autoscale_view()

        plt.legend(handles=[polygon], loc='upper right')
        plt.savefig('/home/main/igilab/l4/fourth/plot.pdf')
        print('Plot Is Saved In /home/main/igilab/l4/fourth/plot.pdf')
        plt.show()
