from .service import PLSerivce

class Task:
    """
    Represents a task related to Premier League (PL) football match statistics.

    Methods:
        - execute(): Executes the task by computing and displaying relevant statistics.
    """

    def __init__(self):
        """
        Initializes an instance of the Task class.
        """
        pass

    def execute(self):
        """
        Executes the task by computing and displaying relevant statistics using PLSerivce.

        Returns:
            None
        """
        pls = PLSerivce()
        pls.stats()

        pls.victory_percent_bigger_by()
        pls.victory_percent_bigger_by_average_goals()
