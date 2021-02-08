from program.bookings.user_input import user_booking_input
from program.canceling.patient_bookings import get_patients


def cancel_booking(clinic_events, u_email, days):
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

    booked_slots = get_patients(clinic_events, days, u_email)

    if booked_slots == None:
        return None

    user_input = user_booking_input(booked_slots)

    if user_input == None:
        return None

    removed_attendee = {
            'email': u_email,
            'comment': 'client',
            'responseStatus': 'accepted'
    }

    canceled_booking = get_canceled_event(user_input, clinic_events, u_email)
    if 'attendees' in canceled_booking:
        attendees = canceled_booking['attendees']

    attendees.remove(removed_attendee)
    canceled_booking['attendees'] = attendees
    canceled_booking['description'] = 'Volunteer Available'

    return canceled_booking


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

    event_time = (str(event_time).replace(" ", 'T')) + '+02:00'

    for event in clinic_events:

        if (event_time == event['start']['dateTime'] and
            ( (event['attendees'][0]['comment'] == 'client' and
            event['attendees'][0]['email'] == user_email) or
            (event['attendees'][1]['comment'] == 'client' and
            event['attendees'][1]['email'] == user_email) ) ):

            return event
