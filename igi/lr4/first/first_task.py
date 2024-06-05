from.models import *
from.serializers import CSVSerializer 
from.serializers import PickleSerializer
from.serializers import default as dflt
from services import InputService

class Task:
    def __init__(self):
        pass


    def pick_serializer(self) -> dflt.Serializer:
        """Prompts the user to select a serializer and returns the selected serializer.

        Returns:
            The selected serializer.
        """
        while True:
            choice = input('Pick Serializer: 1 - CSV; 2 - Pickle: ')

            if choice in ['1', '2']:
                return CSVSerializer() if choice == '1' else PickleSerializer()

            print('Wrong Input, Try Again')


    def search_by_century(self, src: list[dict], century: int) -> list:
        """Searches a list of events by century.

        Args:
            src (list[dict]): The list of events.
            century (int): The century to search for.

        Returns:
            list: The list of events that match the specified century.
        """
        return sorted([event for event in src if str(event['century']) == str(century)],
                      key=lambda item: item['century'])


    def dictionary_of_events(self):
        """Creates a dictionary of events from the main_events list.

        Returns:
            dict: A dictionary of events, where the key is the event name and the value is the century.
        """
        src = HistoryEvent.main_events()
        events = []
        for item in src:
            events.append({ "name": item.name, "century": item.century })

        return events


    def execute(self):
        """Executes the task.

        This includes prompting the user to select a serializer, serializing the dictionary of events, and searching for events by century if the user requests it.
        """
        serializer = self.pick_serializer()
        
        serializer.serialize(self.dictionary_of_events())
        ds = list(serializer.deserialize())

        choice = input('Do You Want To Search Events By Century? (y/n): ').lower()

        if choice in ['y', 'yes']:
            request = InputService.input_specified_type(int, 
                                "What Century Do You Want To Search: ")
            response = self.search_by_century(ds, request)
            
            if len(response) == 0:
                print('Events Are Not Found')
            else:
                print("--  ", end='')
                print('\n--  '.join([item["name"] for item in response]))