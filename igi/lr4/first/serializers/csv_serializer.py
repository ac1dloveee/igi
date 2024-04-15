from .default import *
import csv

class csv_serializer(serializer):
    def __init__(self, fname=serializer.default_file_name):
        self.__fname = fname

    def serialize(self, src) -> None:
        with open(self.__fname, 'w', newline='') as file:
            names = ['name', 'century']
            writer = csv.DictWriter(file, fieldnames=names, dialect=csv.unix_dialect)
            writer.writeheader()
            writer.writerows(src)

    def deserialize(self):
        with open(self.__fname, 'r', newline='') as file:
            reader = csv.DictReader(file)
            
            for item in reader:
                yield item
