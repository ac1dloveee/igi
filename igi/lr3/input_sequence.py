import input_service as inp

def default_input(number_type: type):
    """
    Returns a list of numbers entered by the user.

    Args:
        number_type (type): The type of the numbers in the list.

    Returns:
        list[number_type]: The list of numbers entered by the user.
    """

    numbers = []

    while True:
        number = inp.input_specified_type(number_type, "Enter a number: ")
        # Add entered number to the list.
        numbers.append(number)

        choise = input("Do you want to continue? (y/n): ").lower()
        if choise != "y" and choise != "yes":
            break

    return numbers


def input_by_maximum_number(max_value_of_number: int):
    """
    Returns a list of numbers entered by the user.
    If the user enters a number greater than the maximum number, input ends.

    Args:
        max_value_of_number (int): The maximum number.

    Returns:
        list[int]: The list of numbers entered by the user.

    """

    numbers = []

    while True:
        number = inp.input_specified_type(int, "Enter a number: ")

        # Check if the number is greater than maximum.
        if number > max_value_of_number:
            break

        numbers.append(number)

    return numbers

def sequence_generator(last_number: int):
    """
    Returns a generator that generates a sequence of numbers.

    Args:
        last_number (int): The last number in the sequence.

    Returns:
        generator[int]: The generator that generates a sequence of numbers.
    """

    for number in range(1, last_number + 1):
        yield number