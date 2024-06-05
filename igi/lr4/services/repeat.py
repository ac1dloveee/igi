class RepeatService:
    @staticmethod
    def repeat(func):
        """
        Repeats a function until the user decides to stop.
        """
        while True:
            func()

            choice = input("Do you want to continue this task: (y/n): ").lower()
            if choice not in ['y', 'yes']:
                break