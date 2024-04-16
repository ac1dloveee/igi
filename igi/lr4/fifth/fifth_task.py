from services import InputService
from .service import ArrayService

class Task:
    """
    Represents a task that generates a random array and computes statistics.

    Methods:
        - __dimensions(): Collects input dimensions for the array.
        - execute(): Executes the task by generating the array and computing statistics.
    """

    def __init__(self):
        """
        Initializes an instance of the Task class.
        """
        pass

    def __dimensions(self):
        """
        Collects input parameters for the array dimensions.

        Returns:
            tuple: A tuple containing the following values:
                - n (int): Number of rows.
                - m (int): Number of columns.
        """
        n = InputService.input_specified_type(int, 'Enter Amount Of Rows: ')
        m = InputService.input_specified_type(int, 'Enter Amount Of Columns: ')

        return n, m

    def execute(self):
        """
        Executes the task by generating a random array and computing statistics.

        Returns:
            None
        """
        n, m = self.__dimensions()

        asv = ArrayService()
        asv.set_array(ArrayService.random_array(n, m))
        print('Generated Array:')
        print(asv.get_array())

        odd_amount, even_amount, correlation = asv.data()
        print(f'Amount Of Odd Numbers Equals {odd_amount}')
        print(f'Amount Of Even Numbers Equals {even_amount}')
        if correlation is not None:
            print(f'Correlation Between Odd And Even Numbers Of Array Equals {correlation}')
