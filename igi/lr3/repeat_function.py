def repeat(func):
    """
    Repeats a function until the user decides to stop.
    """
    func()

    choice = input("Do you want to continue this task: (y/n): ").lower()
    if choice == "y" or choice == "yes":
        repeat(func)