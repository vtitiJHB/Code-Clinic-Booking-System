from sys import argv
import os.path
import pickle

from dateutil.relativedelta import relativedelta
from datetime import datetime

from program.general.file_handling import create_folder
from program.general.token_handler import token_check

from program.general.file_handling import create_folder
from program.general.token_handler import token_check

def return_events(calendar_id, download_days, calendar_type):
    """
    checks the token 10min token to see if it is expired and if so
    re-downloads the events, else it just returns the data from a
        pickled file.

    :param calendar_id: the built calendar item AKA our calendarID
    :type calendar_id: class object
    :param download_days: the number of days of data to download
    :type download_days: int
    :return: returns the events dictionary that holds all events and
        the data for each one
    :rtype: dict
    """
    pathname = os.path.abspath(os.path.dirname(argv[0])) + '/program'

    create_folder(f'{pathname}/saves')
    if token_check(f'token_calendar_{calendar_type}'):
        if os.path.exists(f'{pathname}/saves/{calendar_type}_events.pickle'):
            with open(f"{pathname}/saves/{calendar_type}_events.pickle",
                    'rb') as data:
                events = pickle.load(data)
            return events
    events = update_events(calendar_id, download_days, calendar_type)

    return events


def update_events(calendar_id, day, calendar_type):
    """
    updates current data with google calendar data using the API
    
    :param calendar_id: the calendar build data
    :type calendar_id: class object
    :param day: number of days of events to download
    :type day: int
    :param calendar_type: the name / owner of the token file
    :type calendar_type: str
    :return: returns the dictionary of events
    :rtype: dict
    """
    pathname = os.path.abspath(os.path.dirname(argv[0])) + '/program'

    now = f"{datetime.utcnow().isoformat()}Z"
    new_t = f"{datetime.utcnow() + relativedelta(days=day)}Z".replace(" ", "T")

    event_result = calendar_id.events().list(calendarId='primary', timeMin=now,
            timeMax=new_t, singleEvents=True, orderBy='startTime').execute()

    events = event_result.get('items', [])
    with open(f"{pathname}/saves/{calendar_type}_events.pickle",
            'wb') as file_name:
        pickle.dump(events, file_name)

    with open(f"{pathname}/tokens/token_calendar_{calendar_type}.pickle",
            'wb') as name:
        pickle.dump(now, name)

    return events
