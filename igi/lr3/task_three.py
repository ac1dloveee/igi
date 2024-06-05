def amount_of_spaces(string: str) -> int:
    """
    Counts the number of spaces in a string.

    Args:
        string (str): The string.

    Returns:
        int: The number of spaces in the string.
    """

    return len(string.split(' ')) - 1

def output_decorator(function):
    """
    Decorates a function that outputs a string.

    Args:
        function (function): The function to decorate.

    Returns:
        function: The decorated function.
    """

    def wrapper(s):
        return " ".join(["The string contains", str(function(s)), "spaces."])

    return wrapper

def execute():
    """
    Execute the third task. Print results to console.
    """

    print("Task 3.")
    print("Count spaces in a string.")
    print()

    string = input("Enter a string: ")

    print(f"Your string: '{string}'")
    output = output_decorator(amount_of_spaces)
    print(output(string))
