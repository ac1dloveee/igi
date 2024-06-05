def input_specified_type(type_to_convert_into: type, input_message: str):
    """
    Input value for the specified type with the specified input message.
    """

    while True:
        try:
            return type_to_convert_into(input(input_message))
        except ValueError as e:
            print("Incorrect input. Try again.")