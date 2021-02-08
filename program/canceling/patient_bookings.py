from dateutil.relativedelta import relativedelta
from datetime import datetime

from program.viewing.custom_color import color
from program.viewing.event_printout import day_of_week


def get_patients(events_id, days, email):
    """
    retrives a list of events that the users is a patient for

    :param events_id: the list of calendar events
    :type events_id: list
    :param days: the number of days of data to be displayed
    :type days: int
    :param email: the users email address
    :type email: str
    """

    valid_times = ['08:30', '09:00', '09:30', '10:00', '10:30', '11:00',
                    '11:30', '12:00', '12:30', '13:00', '13:30', '14:00',
                    '14:30', '15:00', '15:30', '16:00', '16:30', '17:00',
                    '17:30']

    now = datetime.utcnow()
    result_map = {}
    days_passed = 0

    for day in range(days):
        curr = now + relativedelta(days=day)
        curr_str = curr.strftime("%Y-%m-%dT%H:%M:%S")
        curr_day = day_of_week(curr_str[:19])
        booked_times = []

        for event in events_id:
            start = event['start'].get('dateTime', event['start'].get('date'))

            if not 'attendees' in event.keys():
                continue
            if ('description' in event.keys() and len(event['attendees']) == 2
                    and ((email == event['attendees'][0]['email']
                    and event['attendees'][0]['comment'] == 'client') 
                    or ( email == event['attendees'][1]['email']
                    and event['attendees'][1]['comment'] == 'client') ) ):

                if start[:10] == curr.strftime('%Y-%m-%d'):
                    booked_times.append(start[11:16])

        if len(booked_times) == 0:
            days_passed += 1
            continue

        new_curr = datetime.strftime(curr, '%Y-%h-%d')
        print(f"\n{color.f_b_c}{new_curr}{color.end}  -  "
            f" The available times for this day are listed below")

        print(f"{25*'-'}\n|", end='')

        print(f"{color.f_b_u_c}{curr_day}{color.end}".center(28)+'|', end='')
        print(f"{color.f_b_u_c}Time{color.end}".center(20) + '|')

        print(f"{25*'-'}")

        for time in booked_times:
            print(f"|\t\t|", end='')
            print(f"{color.f_green}{time}{color.end}".center(16) + '|')
            print(f"{25*'-'}")

        result_map['{0}-{1}'.format(curr.month, curr.day)] = booked_times

    if days_passed == days:
        text = f"{color.f_b_b}You have not booked any help slots{color.end}"
        print('\n' + text.center(100) + '\n')
        return None

    return result_map
