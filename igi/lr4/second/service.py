import re
import itertools

class TextServiceMixin:
    """
    A mixin class providing various text processing services such as sentence splitting, 
    sentence and word analysis, and pattern matching within texts.
    """

    def list_of_sentences(self, text: str) -> list[str]:
        """
        Splits the given text into a list of sentences.

        Args:
            text (str): The text to split into sentences.

        Returns:
            list[str]: A list of sentences without newline characters and empty entries.
        """
        return [item.replace('\n', '') for item in re.split("[\.\?\!]", text) if len(item) > 0]

    def amount_of_sentences_by_ending_symbol(self, text: str, symbol) -> list[str]:
        """
        Counts the number of sentences ending with a specific symbol.

        Args:
            text (str): The text to analyze.
            symbol (str): The sentence-ending punctuation to count.

        Returns:
            list[str]: The count of sentences ending with the specified symbol.
        """
        return len(re.split(f'\{symbol}', text)) - 1 if text.count(symbol) != 0 else 0

    def remove_non_letter_symbols(self, text: str) -> str:
        """
        Removes all non-letter symbols from the text.

        Args:
            text (str): The text to clean.

        Returns:
            str: The text with only letters and spaces.
        """
        return re.compile('[^a-zA-Z\ ]').sub('', text)

    def average_sentence_length(self, sentences: list[str]) -> float:
        """
        Calculates the average length of sentences in a list.

        Args:
            sentences (list[str]): A list of sentences.

        Returns:
            float: The average length of the sentences.
        """
        return sum([len(self.remove_non_letter_symbols(item).replace(' ', '')) for item in sentences]) / len(sentences)

    def list_of_words(self, sentences: list[str]) -> list[str]:
        """
        Creates a list of words from a list of sentences.

        Args:
            sentences (list[str]): A list of sentences.

        Returns:
            list[str]: A list of words.
        """
        return [item for item in list(itertools.chain.from_iterable([self.remove_non_letter_symbols(item).split(' ') for item in sentences])) if item != '']

    def average_word_length(self, words: list[str]) -> float:
        """
        Calculates the average length of words in a list.

        Args:
            words (list[str]): A list of words.

        Returns:
            float: The average length of the words.
        """
        return sum(map(len, words)) / len(words)

    def is_guid(self, text: str) -> bool:
        """
        Checks if the given text is a valid GUID.

        Args:
            text (str): The text to check.

        Returns:
            bool: True if the text is a valid GUID, False otherwise.
        """
        return re.search('^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', text) is not None

    def amount_of_smiles(self, text: str) -> int:
        """
        Counts the number of smiley faces in the text.

        Args:
            text (str): The text to analyze.

        Returns:
            int: The count of smiley faces.
        """
        return len(re.split('[:;]-*\[\]', text)) - 1 if re.search('[:;]-*\[\]', text) else 0

    def amount_of_uppercase_letters(self, text: str) -> int:
        """
        Counts the number of uppercase letters in the text.

        Args:
            text (str): The text to analyze.

        Returns:
            int: The count of uppercase letters.
        """
        return len(re.findall('[A-Z]', text))

    def amount_of_lowercase_letters(self, text: str) -> int:
        """
        Counts the number of lowercase letters in the text.

        Args:
            text (str): The text to analyze.

        Returns:
            int: The count of lowercase letters.
        """
        return len(re.findall('[a-z]', text))

    def first_word_with_letter(self, words: list[str], letter):
        """
        Finds the first word containing the specified letter and its position in the list.

        Args:
            words (list[str]): A list of words.
            letter (str): The letter to search for.

        Returns:
            tuple: A tuple containing the word and its position (1-indexed) in the list.
        """
        return [(item, words.index(item) + 1) for item in words if letter in item.lower()][0]

    def remove_words_starting_with(self, text: str, letter: str) -> str:
        """
        Removes words starting with the specified letter from the text.

        Args:
            text (str): The text to process.
            letter (str): The letter that the words start with to be removed.

        Returns:
            str: The text with specified words removed.
        """
        return re.compile(f"[^a-zA-Z\-][{letter.lower()}{letter.upper()}][a-zA-Z\-']*").sub('', text)
