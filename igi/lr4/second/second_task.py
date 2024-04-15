import re
import itertools 
from zipfile import *
import os

class task:
    def __init__(
            self, path: str = '/home/main/igilab/l4/second/data/data.txt',
            output_path='/home/main/igilab/l4/second/data/results.txt'):
        self.__filepath = path
        self.__output_filepath = output_path


    def read_data_from_file(self) -> str:
        with open(self.__filepath, 'r') as text:
            return text.read()


    def list_of_sentences(
            self, text: str) -> list[str]:
        return [item.replace(
            '\n', '') for item in re.split("[\.\?\!]", text) if len(item) > 0 ]


    def amount_of_sentences_by_ending_symbol(
            self, text: str, symbol) -> list[str]:
        return len(re.split(
            f'\{ symbol }', text)) - 1 if text.count(symbol) != 0 else 0


    def remove_non_letter_symbols(
            self, text: str) -> str:
        return re.compile('[^a-zA-Z\ ]').sub('', text)


    def average_sentence_length(
            self, sentences: list[str]) -> float:
        return sum([len(self.remove_non_letter_symbols(
            item).replace(' ', '')) for item in sentences]) / len(sentences)


    def list_of_words(
            self, sentences: list[str]) -> list[str]:
        return [item for item in list(itertools.chain.from_iterable(
            [self.remove_non_letter_symbols(item).split(' ') for item in sentences])) if item != '']


    def average_word_length(
            self, words: list[str]) -> float:
        return sum(map(len, words)) / len(words)


    def is_guid(self, text: str) -> bool:
        return re.search(
            '^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', text) is not None


    def amount_of_smiles(
            self, text: str) -> int:
        return len(re.split(
            '[:;]-*[\[\]()]', text)) - 1 if re.search(
                '[:;]-*[\[\]()]', text) else 0


    def amount_of_uppercase_letters(
            self, text: str) -> int:
        return len(re.findall('[A-Z]', text))


    def amount_of_lowercase_letters(
            self, text: str) -> int:
        return len(re.findall('[a-z]', text))


    def first_word_with_letter(
            self, words: list[str], letter):
        return [(item, words.index(item) + 1) for item in words if letter in item.lower()][0]


    def remove_words_starting_with(
            self, text: str, letter: str) -> str:
        return re.compile(f"[^a-zA-Z\-][{ letter.lower() }{ letter.upper() }][a-zA-Z\-']*").sub('', text)


    def zip_results(self):
        with ZipFile(
                '/home/main/igilab/l4/second/data/results.zip', 'w',
                compression=ZIP_DEFLATED, compresslevel=3) as zp:
            zp.write(self.__output_filepath, arcname='results.txt')
            
            for item in zp.infolist():
                print(f"Filename: {item.filename}, Date: {item.date_time}, Size: {item.file_size}")

        os.remove(self.__output_filepath)



    def execute(self):
        data = self.read_data_from_file()

        amount_of_dot_sentences = self.amount_of_sentences_by_ending_symbol(data, '.')
        amount_of_question_sentences = self.amount_of_sentences_by_ending_symbol(data, '?')
        amount_of_exclaim_sentences = self.amount_of_sentences_by_ending_symbol(data, '!')
        amount_of_sentences = amount_of_dot_sentences + amount_of_question_sentences + amount_of_exclaim_sentences

        with open(self.__output_filepath, 'w') as output:
            print(f'Amount Of Sentences Is { amount_of_sentences }', file=output)
            print(f'Amount Of Sentences Ending With "." Is { amount_of_dot_sentences }.', file=output)
            print(f'Amount Of Sentences Ending With "?" Is { amount_of_question_sentences }.', file=output)
            print(f'Amount Of Sentences Ending With "!" Is { amount_of_exclaim_sentences }.', file=output)
            print(file=output)

            sentences = self.list_of_sentences(data)
            words = self.list_of_words(sentences)

            print(f'Average Sentence Length Is { self.average_sentence_length(sentences) }.', file=output)
            print(f'Average Word Length Is { self.average_word_length(words) }.', file=output)

            print(f'Amount Of Smiles Is { self.amount_of_smiles(data) }.', file=output)
            print(file=output)

            replace_with = input('Enter Symbol To Replace Spaces With: ')[0]
            print(f'Replaced Spaces With "{ replace_with }":', file=output)
            print(data.replace(' ', replace_with), file=output)

            print(file=output)
            print(f'This Text Is { "" if self.is_guid(data) else "Not" } Guid.', file=output)
            print(f'Amount Of Lowercase Letters Is { self.amount_of_lowercase_letters(data) }.', file=output)
            print(f'Amount Of Uppercase Letters Is { self.amount_of_uppercase_letters(data) }.', file=output) 

            word_with_z, index_of_word_with_z = self.first_word_with_letter(words, 'z') 
            print(f'First Letter With Letter "Z" Is { word_with_z }, At Position { index_of_word_with_z }', file=output)

            print(file=output)
            print('Text Without Words Starting With "A":', file=output)
            print(self.remove_words_starting_with(data, 'a'), file=output)

        self.zip_results()