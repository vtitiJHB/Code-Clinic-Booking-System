from sys import argv
import os

from dateutil.relativedelta import relativedelta
from datetime import datetime
from pathlib import Path

try:
    from ics import Calendar, Event

except ModuleNotFoundError:
    os.system("pip3 install ics")
    from ics import Calendar, Event


def calendar_init(calendar_id, day):
    """
    creats the calendar data file to be imported by calendar
        applications

    :param calendar_id: the calendar object from google
    :type calendar_id: class object
    :param day: the number of days of data to be displayed
    :type day: int
    """
    pathname = Path.home()

    now = f"{datetime.utcnow().isoformat()}Z"
    new_t = f"{datetime.utcnow() + relativedelta(days=day)}Z".replace(" ", "T")

    event_result = calendar_id.events().list(calendarId='primary', timeMin=now,
            timeMax=new_t, singleEvents=True, orderBy='startTime').execute()

    events = event_result.get('items', [])

    c = Calendar()
    for event in events:
        e = Event()

        if 'summary' in event.keys():
            e.name = event['summary']

        else:
            e.name = 'Private'

        try:
            e.begin = datetime.strptime(event['start']['dateTime'],
                "%Y-%m-%dT%H:%M:%S+02:00")
            e.duration = {"minutes":30}

        except KeyError:
            e.begin = datetime.strptime(event['start']['date'],
                "%Y-%m-%d")

        if 'description' in event.keys():
            e.description = event['description']

        c.events.add(e)

    c.events

    with open(f'{pathname}/calendar_data.ics', 'w+') as my_file:
        my_file.writelines(c)
