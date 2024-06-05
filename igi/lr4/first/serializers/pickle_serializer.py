from .default import *
import pickle

class PickleSerializer(Serializer):
    """
    A serializer that handles the serialization and deserialization of Python objects using pickle.

    Attributes:
        __fname (str): Filename where the serialized object will be stored. Defaults to the filename specified in the parent class.
    """

    def __init__(self):
        """
        Initializes the pickle_serializer instance, setting the filename to the default file name defined in the parent class.
        """
        self.__fname = super()._default_file_name

    def serialize(self, src: dict) -> None:
        """
        Serializes the given source dictionary into a file using pickle.

        Args:
            src (dict): The dictionary to serialize.

        Returns:
            None
        """
        with open(self.__fname, 'wb') as file:
            pickle.dump(src, file)

    def deserialize(self):
        """
        Deserializes the contents of the file back into a Python object.

        Yields:
            The deserialized Python objects from the file.
        """
        with open(self.__fname, 'rb') as file:
            items = pickle.load(file)

        for item in items:
            yield item
