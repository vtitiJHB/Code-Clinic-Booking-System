from dateutil.relativedelta import relativedelta

from program.bookings.user_input import user_booking_input
from program.canceling.volunteer_bookings import get_volunteers


def cancel_volunteer(clinic_events, u_email, days):
    """
    This is the main function to cancel the patient book.
    First we will check the CodingClinic's calendar to see if there 
    are any bookings they are in.
    We then ask them to choose the date and time for which they are
        available
    Finally we make the booking.

    :param clinic_events: this ios a list containing all the
        calendars events for the set number of data of data to show
    :type clinic_events: list
    :param u_email: this is the users email address.
    :type u_email: str
    :param days: the neumber of days to be shown from calendar
    :type days: int
    :return: the new list of attendees to be sent to google or None
    :rtype: list or None
    """
    booked_slots = get_volunteers( clinic_events, days, u_email )

    if booked_slots == None:
        return None

    user_input = user_booking_input( booked_slots )

    if user_input == None:
        return None

    return get_canceled_event( user_input, clinic_events, u_email )


def get_canceled_event(event_time, clinic_events, user_email):
    """
    checks to see if the event time the user entered matches an event
        time and the comment key to see if they're a patient

    :param event_time: this is the dateTime of the event the user
        wants to cancel attendance for.
    :type event_time: dateTime
    :param clinic_events: this is a list of events from google
    :type clinic_events: list
    :param user_email: this is the user's email
    :type user_email: str
    :return: set of the event
    :rtype: set
    """
    the_list = []

    for _ in range(3):
        event_time_str = (str(event_time).replace(" ", 'T')) + '+02:00'
        event_time = event_time + relativedelta(minutes=30)

        for event in clinic_events:

            if ('dateTime' in event['start'].keys() and
                    event_time_str == event['start']['dateTime']):

                if ('attendees' in event.keys() and 
                        event['attendees'][0]['email'] == user_email):

                    the_list.append(event)
    return the_list
