from dateutil.relativedelta import relativedelta
from datetime import datetime

from program.viewing.custom_color import color
from program.viewing.event_printout import day_of_week


def get_volunteers(events_id, days, email):
    """
    retrives a list of events that the users is a clinician for

    :param events_id: the list of calendar events
    :type events_id: list
    :param days: number of days of data to be displayed
    :type days: int
    :param email: the users email address
    :type email: str
    """
    now = datetime.utcnow()
    result_map = {}
    booked_times = get_booked_times(events_id, email)
    days_passed = 0

    for day in range(days):
        curr = now + relativedelta(days=day)
        curr_date = curr.strftime("%Y-%m-%d")
        curr_day = day_of_week(curr.strftime("%Y-%m-%dT%H:%M:%S"))
        times_list = []

        if len(booked_times) == 0:
            days_passed += 1
            continue

        for date in booked_times:
            if date[1] == curr_date:
                times_list.append(date[0])

        if len(times_list) == 0:
            continue

        new_curr = datetime.strftime(curr, '%Y-%h-%d')
        print(f"\n{color.f_b_c}{new_curr}{color.end}  -  "
            f" The available times for this day are listed below")

        print(f"{31*'-'}\n|", end='')

        print(f"{color.f_b_u_c}{curr_day}{color.end}".center(28)+'|', end='')
        print(f"{color.f_b_u_c}Time{color.end}".center(26) + '|')

        print(f"{31*'-'}")

        for the_time in times_list:
            print(f"|\t\t|", end='')
            print(f"{color.f_green}{the_time}{color.end}".center(22) + '|')
            print(f"{31*'-'}")

        result_map[f'{curr.month}-{curr.day}'] = times_list

    if days_passed == days:
        text_1 = f"{color.f_b_b}You have no volunteer slots{color.end}"
        print('\n' + text_1.center(100) + '\n')
        return None

    return result_map


def get_booked_times(events_id, email):
    """
    gets a list of events that you have registered as a clinician for

    :param events_id: a list google calendar events
    :type events_id: list
    :param email: the users email address
    :type email: str
    """
    valid_times = ['08:30:00', '10:00:00', '11:30:00',
        '13:00:00', '14:30:00', '16:00:00']
    booked_times = []

    for index, event in enumerate(events_id):
        try:
            start = datetime.strptime(event['start'].get('dateTime',
                event['start'].get('date')), "%Y-%m-%dT%H:%M:%S+02:00")

        except ValueError:
            start = datetime.strptime(event['start'].get('dateTime',
                event['start'].get('date')), "%Y-%m-%d")


        if ('attendees' in event.keys() and len(event['attendees']) == 1
                and email == event['attendees'][0]['email'] 
                and str(start.time()) in valid_times):

            if ('attendees' in events_id[index+1].keys() 
                    and len(events_id[index+1]['attendees']) == 1
                    and email == events_id[index+1]['attendees'][0]['email'] 
                    and 'attendees' in events_id[index+2].keys() 
                    and len(events_id[index+2]['attendees']) == 1
                    and email == events_id[index+2]['attendees'][0]['email'] ):

                booked_times.append( [str(start.strftime("%H:%M")),
                    str(start.strftime("%Y-%m-%d"))])

    return booked_times
