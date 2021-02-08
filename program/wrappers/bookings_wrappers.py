from program.bookings.volunteer_booking import book_volunteer
from program.bookings.patient_booking import book_patient

from program.general.token_handler import clear_tokens

from program.viewing.events_retrieval import return_events
from program.viewing.custom_color import color

from program.wrappers.view_wrapper import p_local_calendar


def p_booking(clinic_calendar, days, user_email, clinic_email):
    """
    a stored method to make a booking on the code clinics google
        calendar

    :param clinic_calendar: the clinics calendar object
    :type clinic_calendar: Resorce
    :param days: the number of days of calendar data to be downloaded
    :type days: int
    :param user_email: the users email address
    :type user_email: str
    :param clinic_email: the clinics email address
    :type clinic_email: str
    :return: None
    :rtype: None
    """
    clear_tokens()
    events = return_events(clinic_calendar, days, "clinic")
    booked_event = book_patient(events, days, user_email, clinic_email)

    if booked_event == None:
        print(f"{color.f_b_d_y}The application has closed.{color.end}\n")
        return None

    ( clinic_calendar.events()
        .update( calendarId='primary', eventId=booked_event['id'],
        body=booked_event ).execute() )
    p_local_calendar(clinic_calendar, days)
    clear_tokens()


def p_volunteer(clinic_calendar, days, user_email, clinic_email):
    """
    a stored method to setup a volunteer on the code clinics google
        calendar

    :param clinic_calendar: the clinics calendar object
    :type clinic_calendar: Resorce
    :param days: the number of days of calendar data to be downloaded
    :type days: int
    :param user_email: the users email address
    :type user_email: str
    :param clinic_email: the clinics email address
    :type clinic_email: str
    :return: None
    :rtype: None
    """
    clear_tokens()
    events = return_events(clinic_calendar, days, 'clinic')
    events_list = book_volunteer(events, days, user_email, clinic_email)

    if events_list == None:
        print(f"{color.f_b_d_y}The application has closed.{color.end}\n")
        return None

    for event in events_list:
        ( clinic_calendar.events()
            .insert( calendarId='primary', body=event )
            .execute() )
    p_local_calendar(clinic_calendar, days)
    clear_tokens()
