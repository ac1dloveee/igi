# CSV Serializer Class

from .default import *
import csv

class CSVSerializer(Serializer):
    def __init__(self):
        """
        Initializes the CSVSerializer class.
        """
        self.__fname = super()._default_file_name

    def serialize(self, src) -> None:
        """
        Serializes a list of dictionaries into a CSV file.

        Args:
            src (list[dict]): List of dictionaries to be serialized.

        Returns:
            None
        """
        with open(self.__fname, 'w', newline='') as file:
            fieldnames = ['name', 'century']
            writer = csv.DictWriter(file, fieldnames=fieldnames, dialect=csv.unix_dialect)
            writer.writeheader()
            writer.writerows(src)

    def deserialize(self):
        """
        Deserializes data from a CSV file and yields each item as a dictionary.

        Yields:
            dict: A dictionary containing data from the CSV file.
        """
        with open(self.__fname, 'r', newline='') as file:
            reader = csv.DictReader(file)
            
            for item in reader:
                yield item
