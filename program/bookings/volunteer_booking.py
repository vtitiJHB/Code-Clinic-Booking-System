from program.bookings.user_input import user_booking_input
from program.bookings.event_creation import create_events
from program.bookings.slot_check import open_slots


def book_volunteer(clinic_events, days, v_email, c_email):
    """
    This is the main function to make the volunteer books.
    First we will check the CodingClinic's calendar to see if there 
    are any openings
    We then ask them to choose the date and time for which they are
        available.
    Finally we make the booking.

    :param clinic_events: a tuple containing all the clinics evenets
    :type clinic_events: tuple
    :param days: this is the number of days of data to show
    :type days: int
    :param v_email: this is the volunteers email address
    :type v_email: string
    :param c_email: this is the clinics email address
    :type c_email: string
    :return: the list of newly created events to be added to the
        calendar
    :rtype: list
    """

    slots = open_slots(clinic_events, days)

    if slots == None:
        return None

    print("To make a booking, select a day and time from the open slots.")

    the_date = user_booking_input(slots)

    if the_date == None:
        return None

    event_list = create_events("Code Clinic", c_email, v_email, the_date)

    return event_list
