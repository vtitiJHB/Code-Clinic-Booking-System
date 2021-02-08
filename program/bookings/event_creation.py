from dateutil.relativedelta import relativedelta
from datetime import datetime

def create_events(event_name, clinic_email, user_email, start):
    """
    Returns a list of 3 different events that are 30 minutes apart
        from eachother and setup for the volunteer.

    :param event_name: the name of the event
    :type event_name: str
    :param clinic_email: the clinics email address
    :type clinic_email: str
    :param user_email: the users email address
    :type user_email: str
    :param start: the starting time of the event
    :type start: datetime
    :return: 3 sets containing data for event creation
    :rtype: set (3 sets)
    """
    description = 'Volunteer Available'
    GMT_OFF = '+02:00'

    event_list = []

    for i in range(3):
        new_start = start + relativedelta(minutes=(30*i))
        new_end = start + relativedelta(minutes=(30*(i+1)))
        event = {
            'summary': event_name,
            'description': description,
            'maxAttendee': 2,
            'start': {
                'dateTime': new_start.isoformat() + GMT_OFF ,
                'timeZone': 'Africa/Johannesburg',
                },
            'end': {
                'dateTime': new_end.isoformat() + GMT_OFF,
                'timeZone': 'Africa/Johannesburg',
                },
            'organizer': {
                'email': clinic_email,
                },
            'attendees': [
                {
                'email': user_email,
                'optional': False,
                'comment': 'volunteer',
                'responseStatus': 'accepted',
                }
            ]
        }
        event_list.append(event)

    return event_list
