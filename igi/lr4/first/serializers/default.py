from abc import ABC, abstractmethod

class Serializer(ABC):
    """
    This class provides an interface for serializing and deserializing data.
    The class defines the abstract methods for serializing and deserializing data.
    The default file name for saving the serialized data is 'data.txt'.
    The location of the file can be changed by modifying the '_default_file_name' attribute.
    The class saves the data in JSON format.
    """

    _default_file_name = '/home/main/igilab/l4/first/data/data.txt'

    @abstractmethod
    def serialize(self, data: dict) -> None:
        """
        This function takes a python dictionary as input and saves it to a file.
        The input dictionary is assumed to contain the data that needs to be serialized.
        The function saves the data to a file named 'data.txt' by default.
        The location of the file can be changed by modifying the '_default_file_name' attribute.
        The function saves the data in JSON format.
        The function does not return any value.

        Parameters:
            data (dict): The python dictionary that needs to be serialized.

        Returns:
            None
        """

    @abstractmethod
    def deserialize(self) -> dict:
        """
        This function loads the serialized data from the file and returns it as a python dictionary.
        The function assumes that the data is stored in JSON format.
        The function does not return any value.

        Returns:
            dict: The deserialized data.
        """