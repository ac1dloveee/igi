from .input import InputService as inps
from .repeat import RepeatService as rf
from first.first_task import Task as task_one
from second.second_task import Task as task_two
from third.third_task import Task as task_three
from fourth.fourth_task import Task as task_four
from fifth.fifth_task import Task as task_five
from sixth.sixth_task import Task as task_six

class MenuService:
    @staticmethod
    def menu():
        """
        Main menu of the program.
        """

        while True:
            # Get task number 
            task_number = inps.input_specified_type(int, "Enter number of the task to execute (1 - 6): ")

            if task_number == 1:
                ts = task_one()
                rf.repeat(ts.execute)
            elif task_number == 2:
                ts = task_two()
                rf.repeat(ts.execute)
            elif task_number == 3:
                ts = task_three()
                rf.repeat(ts.execute)    
            elif task_number == 4:
                ts = task_four()
                rf.repeat(ts.execute)
            elif task_number == 5:
                ts = task_five()
                rf.repeat(ts.execute)
            elif task_number == 6:
                ts = task_six()
                rf.repeat(ts.execute)
            else:
                # Not in [1, 6]
                print("Invalid task number")
                continue
            
            choice = input("Do you want to continue the program? (y/n): ").lower()
            if choice != "y" and choice != "yes":
                break