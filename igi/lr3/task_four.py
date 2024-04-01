def amount_of_words(text: str, condition) -> int:
    """
    Counts the number of words in a string that satisfy a condition.

    Args:
        text (str): The string.
        condition (function): The condition.

    Returns:
        int: The number of words in the string that satisfy the condition.
    """

    return sum([1 if word.isalpha() and condition(word) else 0 for word in text.split(" ")])


def shortest_word(text: str, condition) -> str:
    """
    Finds the shortest word in a string that satisfies a condition.

    Args:
        text (str): The string.
        condition (function): The condition.

    Returns:
        str: The shortest word in the string that satisfies the condition.
    """

    return min([word for word in text.split(" ") if word.isalpha() and condition(word)])


def words_by_length_in_decreasing_order(text: str) -> list[str]:
    """
    Returns the words in a string in decreasing order of their length.

    Args:
        text (str): The string.

    Returns:
        list[str]: The words in the string in decreasing order of their length.
    """

    return sorted([word for word in text.split(" ") if word.isalpha()],
                   key=len, reverse=True)


def execute():
    """
    Executes the fourth task. Prints results to console.
    """
    
    print("Task 4.")
    print("Count words with less than 5 letters.")
    print("Prints shortest word that ends with letter 'd'.")
    print("Prints words in descending order.")

    text = ('So she was considering in her own mind, as well as she could, for the hot day made her feel '
            'very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble '
            'of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by '
            'her.')

    print(('Amount of words with less than 5 letters is'
           f' { amount_of_words(text, lambda word: len(word) < 5) }.'))
    print()
    
    print(('Shortest word that ends with letter '
           f'"d" - "{ shortest_word(text, lambda word: word[-1].lower() == "d") }".'))
    print()
    
    print("Words by length in decreasing order: ")
    print("--  ", end='')
    print('\n--  '.join(words_by_length_in_decreasing_order(text)))
