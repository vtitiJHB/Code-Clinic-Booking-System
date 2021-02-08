from program.calendar_export.init_calendar import calendar_init

from program.viewing.events_retrieval import return_events
from program.viewing.event_printout import print_events
from program.viewing.custom_color import color


def p_view(clinic_calendar, days, user_calendar):
    """
    a stored method to view the clinc and users calendar

    :param clinic_calendar: the clinics calendar object
    :type clinic_calendar: Resorce
    :param user_calendar: the users calendar object
    :type user_calendar: Resorce
    :param days: the number of days of calendar data to be downloaded
    :type days: int
    """
    events = return_events(clinic_calendar, days, 'clinic')
    print_events(events, days, 'Clinic')
    events = return_events(user_calendar, days, 'users')
    print_events(events, days, 'User')


def p_local_calendar(clinic_calendar, days):
    """
    a stored method to update the local calendars data

    :param clinic_calendar: the google calendar object
    :type clinic_calendar: Resorce
    :param days: the number of days of data to be stored
    :type days: int
    """
    print(f"{color.f_b_d_y}Your local calendar data has been updated{color.end}\n"
        .center(100))
    calendar_init(clinic_calendar, days)
