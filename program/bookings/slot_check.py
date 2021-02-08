from dateutil.relativedelta import relativedelta
from datetime import datetime

from program.viewing.custom_color import color
from program.viewing.event_printout import day_of_week


def open_slots(events_id, days):
    """
    This function will check the open slots for a certain amount of
        days and check if the slot is open from a certain time then
        also print them out

    :param events_id: The list full of the events & days,
        number of days to check for
    :type events_id: tuple
    :param days: this is the number of days of data to show
    :type days: int
    :return: a dict of all the events or None
    :rtype: dict or None
    """

    valid_times = ['08:30', '10:00', '11:30', '13:00', '14:30', '16:00']

    result_map = {}
    days_passed = 0

    for day in range(days):
        now = datetime.utcnow()
        curr = now + relativedelta(days=day)
        curr_str = curr.strftime("%Y-%m-%dT%H:%M:%S")
        curr_day = day_of_week(curr_str[:19])
        now = datetime.now().strftime("%Y-%m-%d %H:%M")

        available_times = []
        used_times = []

        for time_slot in valid_times:
            if ( now[8:10] == curr_str[8:10] and time_slot[0:5]  < now[11:16]):
                used_times.append(time_slot)

        for event in events_id:
            start = event['start'].get('dateTime', event['start'].get('date'))

            if ( curr.day == int(start[8:10]) and start[11:16] in valid_times
                    and not start[11:16] in used_times):
                used_times.append(start[11:16])

        available_times = [x for x in valid_times if x not in used_times]

        if len(available_times) == 0:
            days_passed += 1
            continue

        new_curr = datetime.strftime(curr, '%Y-%h-%d')
        print(f"\n{color.f_b_c}{new_curr}{color.end}  -  "
            f" The available times for this day are listed below")

        print(f"{25*'-'}\n|", end='')

        print(f"{color.f_b_u_c}{curr_day}{color.end}".center(28)+'|', end='')
        print(f"{color.f_b_u_c}Time{color.end}".center(20) + '|')

        print(f"{25*'-'}")

        for pos_time in valid_times:
            if pos_time in available_times:
                print('|' + f"{color.f_green}" + "Available".center(15),end='')
                print(f"{color.end}" + '|', end='')
                print(f"{color.f_green}{pos_time}{color.end}".center(16) + '|')
                print(f"{25*'-'}")
            else:
                print('|' + f"{color.f_l_r}" + "Booked".center(15),end='')
                print(f"{color.end}" + '|', end='')
                print(f"{color.f_l_r}{pos_time}{color.end}".center(18) + '|')
                print(f"{25*'-'}")
        print()
        result_map['{0}-{1}'.format(curr.month, curr.day)] = available_times

    if days_passed == days:
        message = "Sorry there are no open slots please try again later"
        print('\n' + f"{color.f_b_b}{message}{color.end}".center(100) + '\n')
        return None

    return result_map


def booked_slots(events_id, days, email):
    """
    This function will check the booked slots for a certain amount of
        days. Check if the slot is booked from a certain time then
        also print them out

    :param events_id: The list full of the events & days,
        number of days to check for.
    :type events_id: list
    :param days: this is the number of days of data to be shown
    :type days: int
    :param email: the paitents email
    :type email: str
    :return: returns a dictionary of the booked slots or None.
    :rtype: dictionary or None
    """
    valid_times = ['08:30', '09:00', '09:30', '10:00', '10:30', '11:00',
                    '11:30', '12:00', '12:30', '13:00', '13:30', '14:00',
                    '14:30', '15:00', '15:30', '16:00', '16:30', '17:00',
                    '17:30']

    now = datetime.utcnow()
    result_map = {}
    total_passed = 0

    for day in range(days):
        curr = now + relativedelta(days=day)
        curr_str = curr.strftime("%Y-%m-%dT%H:%M:%S")
        curr_day = day_of_week(curr_str[:19])

        used_times = []

        for event in events_id:
            if 'dateTime' in event['start'].keys():
                start = event['start'].get('dateTime', event['start']
                    .get('date'))

            if ('description' in event.keys() and 'attendees' in event.keys() 
                    and len(event['attendees']) == 1
                    and email != event['attendees'][0]['email'] ):

                if ((curr.day == int(start[8:10])) 
                        and start[11:16] in valid_times):
                    used_times.append(start[11:16])

        if len(used_times) == 0:
            total_passed += 1
            continue

        new_curr = datetime.strftime(curr, '%Y-%h-%d')
        print(f"\n{color.f_b_c}{new_curr}{color.end}  -  "
            f" The available times for this day are listed below")

        print(f"{25*'-'}\n|", end='')

        print(f"{color.f_b_u_c}{curr_day}{color.end}".center(28)+'|', end='')
        print(f"{color.f_b_u_c}Time{color.end}".center(20) + '|')

        print(f"{25*'-'}")

        for time in used_times:
            print('|' + f"{color.f_green}" + "Available".center(15),end='')
            print(f"{color.end}" + '|', end='')
            print(f"{color.f_green}{time}{color.end}".center(16) + '|')
            print(f"{25*'-'}")

        result_map['{0}-{1}'.format(curr.month, curr.day)] = used_times

    if total_passed == days:
        message = "Sorry there are no open slots please try again later"
        print('\n' + f"{color.f_b_b}{message}{color.end}".center(100) + '\n')
        return None

    return result_map
