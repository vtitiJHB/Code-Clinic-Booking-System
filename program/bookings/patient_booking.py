from program.bookings.user_input import patient_booking_input
from program.bookings.slot_check import booked_slots


def book_patient(clinic_events, days, p_email, c_email):
    """
    This is the main function to make the patient book.
    First we will check the CodingClinic's calendar to see if there 
    are any volunteers
    We then ask them to choose the date and time for which they are
        available.
    Finally we make the booking.

    :param clinic_events: this ios a list containing all the
        calendars events for the set number of data of data to show.
    :type clinic_events: list
    :param days: the number of days of calendar data to show.
    :type days: int
    :param p_email: this is the users email address.
    :type p_email: string
    :param c_email: this is the clinics email address.
    :type c_email: str
    :return: this is the new updated list to be sent to google.
    :rtype: list
    """
    slots = booked_slots(clinic_events, days, p_email)

    if slots == None:
        return None

    text_1 = "To make a booking, select a"
    text_1 = text_1 + " day and time from the open slots.\n"
    print(text_1)
    user_input = patient_booking_input(slots)

    if user_input == None:
        return None

    add_attendees = {
            'email': p_email,
            'optional': False,
            'comment': 'client',
            'responseStatus': 'accepted'
            }

    the_event = get_updatable_event(user_input[0], clinic_events)

    if 'attendees' in the_event.keys():
        attendees = the_event['attendees']
    else:
        attendees = []

    attendees.append(add_attendees)

    the_event['attendees'] = attendees
    the_event['description'] = user_input[1]

    return the_event


def get_updatable_event(time_of_event, clinic_events):
    """
    checks to see if the event time the user entered matches an event
        time

    :param time_of_event: this is the dateTime of the event the user
        wants to subscribe for.
    :type time_of_event: dateTime
    :param clinic_events: this is the list of events from the google
        API.
    :type clinic_events: list
    :return: set of the event or None.
    :rtype: set or None
    """
    time_of_event = (str(time_of_event).replace(" ", 'T')) + '+02:00'

    for event in clinic_events:
        if time_of_event == event['start']['dateTime']:
            return event
    return None
