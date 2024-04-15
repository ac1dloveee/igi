from .default import *
import pickle

class pickle_serializer(serializer):
    def __init__(self, fname=serializer.default_file_name):
        self.__fname = fname

    def serialize(self, src: dict) -> None:
        with open(self.__fname, 'wb') as file:
            pickle.dump(src, file)

    def deserialize(self):
        with open(self.__fname, 'rb') as file:
            items = pickle.load(file)

        for item in items:
            yield item