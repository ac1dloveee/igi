import input_sequence as inpseq
import input_service as inp

# Maximum value for the sequence.
max_value_of_number = 1000


def sum_of_numbers(numbers: list[int]) -> int:
    """
    Finds the sum of a list of numbers.

    Args:
        numbers (list[int]): The list of numbers.

    Returns:
        int: The sum of the numbers in the list.
    """

    return sum(numbers)


def amount_of_even_numbers(numbers: list[int]) -> int:
    """
    Finds the amount of even numbers in a list.

    Args:
    numbers (list[int]): The list of numbers.

    Returns:
        int: The amount of even numbers in the list.
    """
    
    return sum(map(lambda num: 1 if num % 2 == 0 else 0, numbers))


def execute():
    """
    Execute the second task. Print results to console.
    """

    print("Task 2.")
    print("Calculating sum of list and finding amount of even numbers in a list.")
    print("Enter a number greater or equal to 1000 to stop adding numbers.")
    print()

    print("Do you want to generate sequence automatically? (y/n): ")
    choice = input().lower()

    if choice == "y" or choice == "yes":
        sequence_size = inp.input_specified_type(
            int, "Enter amount of numbers in a sequence: ")
 
        numbers = list(inpseq.sequence_generator(sequence_size))
    else:
        numbers = inpseq.input_by_maximum_number(max_value_of_number)

    print(f"Your numbers: { numbers }")
    print(f"Total sum of this list: { sum_of_numbers(numbers) }")
    print(f"This list contains { amount_of_even_numbers(numbers) } even numbers")