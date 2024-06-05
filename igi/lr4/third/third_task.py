from .calculations import *
from services import InputService

class Task:
    """
    A class designed to execute a sequence of calculations and display statistical information.
    """

    def __init__(self):
        """
        Initializes the Task instance. Currently, the initializer does not perform any actions.
        """
        pass

    def execute(self):
        """
        Executes the main functionality of the Task class. It prompts the user for an accuracy level,
        performs a series of evaluations, and then prints and plots the statistical results.
        """
        # Prompt the user to enter the desired accuracy for calculations.
        eps = InputService.input_specified_type(float, 'Enter The Accuracy: ')
        
        # Initialize the calculator with the specified accuracy.
        calc = Calculator(eps)

        # List to store the results of the evaluations.
        iterations = []

        # Evaluate the function provided by the calculator for values from -0.99 to 0.99.
        for x in range(-99, 100):
            iterations.append(calc.evaluate(x / 100))

        # Calculate and retrieve statistics for the sequence of evaluations.
        statistics = SequenceStatistics(iterations).stats()
        
        # Print the statistical results in a formatted manner.
        print('Stats Of Sequence: ')
        print("--  ", end='')
        print('\n--  '.join([f'{ key }: { value }' for key, value in statistics.items()]))

        # Plot the sequence of evaluations using the plot service.
        PlotService.plot_sequence(iterations)
