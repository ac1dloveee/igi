import task_one
import task_two
import task_three
import task_four
import task_five

import input_service as inps
import repeat_function as rf

def menu():
    """
    Main menu of the program.
    """

    while True:
        # Get task number 
        task_number = inps.input_specified_type(int, "Enter number of the task to execute (1 - 5): ")

        if task_number == 1:
            rf.repeat(task_one.execute)
        elif task_number == 2:
            rf.repeat(task_two.execute)
        elif task_number == 3:
            rf.repeat(task_three.execute)    
        elif task_number == 4:
            rf.repeat(task_four.execute)
        elif task_number == 5:
            rf.repeat(task_five.execute)
        else:
            # Not in [1, 5]
            print("Invalid task number")
            continue
        
        choice = input("Do you want to continue the program? (y/n): ").lower()
        if choice != "y" and choice != "yes":
            break
    