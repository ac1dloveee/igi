from .calculations import *
from services import input_service

class task:
    def __init__(self):
        pass

    def execute(self):
        eps = input_service.input_specified_type(float, 'Enter The Accuracy: ')
        calc = calculator(eps)

        iterations = []

        for x in range(-99, 100):
            iterations.append(calc.evaluate(x / 100))

        statistics = sequence_statistics(iterations).stats()
        print('Stats Of Sequence: ')
        print("--  ", end='')
        print('\n--  '.join([f'{ key }: { value }' for key, value in statistics.items()]))

        plot_service.plot_sequence(iterations)