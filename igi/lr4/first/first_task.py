from .models import *
from .serializers import csv_serializer 
from .serializers import pickle_serializer
from .serializers import default as dflt
from services import input_service

class task:
    def __init__(self):
        pass


    def pick_serializer(self) -> dflt.serializer:
        while True:
            choice = input(
                '''Pick Serializer 
    1. CSV  
    2. Pickle
- ''')
            
            if choice in ['1', '2']:
                return csv_serializer() if choice == '1' else pickle_serializer()
            
            print('Wrong Input, Try Again')


    def search_by_century(self, src: list[dict], century: int) -> list:
        return sorted([event for event in src if str(event['century']) == str(century)],
                      key=lambda item: item['century'])


    def dictionary_of_events(self):
        src = history_event.main_events()
        events = []
        for item in src:
            events.append({ "name": item.name, "century": item.century })

        return events


    def execute(self):
        serializer = self.pick_serializer()
        
        serializer.serialize(self.dictionary_of_events())
        ds = list(serializer.deserialize())

        choice = input('Do You Want To Search Events By Century? (y/n): ').lower()

        if choice in ['y', 'yes']:
            request = input_service.input_specified_type(int, 
                                "What Century Do You Want To Search: ")
            response = self.search_by_century(ds, request)
            
            if len(response) == 0:
                print('Events Are Not Found')
            else:
                print("--  ", end='')
                print('\n--  '.join([item["name"] for item in response]))

