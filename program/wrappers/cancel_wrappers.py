from program.canceling.cancel_booking import cancel_booking
from program.canceling.cancel_volunteer import cancel_volunteer

from program.wrappers.view_wrapper import p_local_calendar

from program.viewing.events_retrieval import return_events
from program.viewing.custom_color import color

from program.general.token_handler import clear_tokens


def p_cancel_volunteer(clinic_calendar, days, user_email):
    """
    a stored method to cancel a volunteer slot

    :param clinic_calendar: the clinics calendar object
    :type clinic_calendar: Resorce
    :param days: the number of days of calendar data to be downloaded
    :type days: int
    :param user_email: the users email address
    :type user_email: str
    :return: None
    :rtype: None
    """
    clear_tokens()
    events = return_events(clinic_calendar, days, "clinic")
    canceled_volunteer = cancel_volunteer(events, user_email, days)

    if canceled_volunteer == None:
        print(f"{color.f_b_d_y}The application has closed.{color.end}\n")
        return None

    if len(canceled_volunteer) > 0:
        for event in canceled_volunteer:
            ( clinic_calendar.events().delete( calendarId='primary',
                eventId=event['id'] ).execute() )
    p_local_calendar(clinic_calendar, days)
    clear_tokens()


def p_cancel_booking(clinic_calendar, days, user_email):
    """
    a stored method to cancel a booked slot

    :param clinic_calendar: the clinics calendar object
    :type clinic_calendar: Resorce
    :param days: the number of days of calendar data to be downloaded
    :type days: int
    :param user_email: the users email address
    :type user_email: str
    :return: None
    :rtype: None
    """
    clear_tokens()
    events = return_events(clinic_calendar, days, "clinic")
    canceled_booking = cancel_booking(events, user_email, days)

    if canceled_booking == None:
        print(f"{color.f_b_d_y}The application has closed.{color.end}\n")
        return None

    if not canceled_booking == None:
        ( clinic_calendar.events()
            .update( calendarId='primary', eventId=canceled_booking['id'],
            body=canceled_booking ).execute() )
    p_local_calendar(clinic_calendar, days)
    clear_tokens()
