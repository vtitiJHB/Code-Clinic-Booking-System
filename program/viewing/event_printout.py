from program.viewing.custom_color import color
from datetime import datetime
from termcolor import colored


def print_events(events, days, owner):
    """
    Prints out the events in a nice format, either from the storage
        file or the updated data from the API

    :param events: a list of calendar events
    :type events: list
    :param days: the number of days of data to be showen
    :type days: int
    :param owner: the owner of the calendar events
    :type owner: str
    :return: None
    :rtype: None
    """
    print()
    print(f"{color.f_b_u_c}{color.bold}{owner}'s Calendar{color.end}"
        .center(115))

    if not events:
        print(f"{color.f_b_b_i_m}No upcoming events found.{color.end}"
            .center(115))
        return print("\n")

    else:
        print(f"{99*'-'}\n|", end='')

        print(f"{color.f_b_y}Day{color.end}".center(30)+'|', end='')
        print(f"{color.f_b_y}Time{color.end}".center(40)+'|', end='')
        print(f"{color.f_b_y}Description{color.end}".center(50)+'|',end='')
        print(f"{color.f_b_y}Availability{color.end}".center(30)+'|')

    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))

        try:
            time = datetime.strftime(datetime.strptime(start[:19], \
                '%Y-%m-%dT%H:%M:%S'), '%B %d - %H:%M')

        except ValueError:
            time = datetime.strftime(datetime.strptime(start[:19], \
                '%Y-%m-%d'), '%B %d - All day')

        day = day_of_week(start[:19])

        if day == None: continue

        print(f"{99*'-'}\n|",end='')

        if 'description' in event.keys():
            print(f"{color.f_cyan}{day}{color.end}".center(25)+'|', end='')
            print(f"{color.f_l_b}{time}{color.end}".center(35)+'|', end='')
            print(f"{event['description']}".center(36)+'|',end='')
            if (event['summary'] == 'Code Clinic' 
                    and len(event['attendees']) == 2):
                print(f"{color.f_l_r}Booked{color.end}".center(27)+'|')
            elif (event['summary'] == 'Code Clinic'):
                print(f"{color.f_b_g}Available{color.end}".center(27)+'|')
            else:
                print(f"{color.f_b_c}Private{color.end}".center(27)+'|')

        else:
            print(f"{color.f_cyan}{day}{color.end}".center(25)+'|', end='')
            print(f"{color.f_l_b}{time}{color.end}".center(35)+'|', end='')
            print(f" ".ljust(36)+'|',end='')
            print(f"{color.f_b_c}Private{color.end}".center(27)+'|')

    print(f"{99*'-'}")


def day_of_week(date):
    """
    a small function that returns what day of the week the date sent
        in is.

    :param date: a string of the day you want converter to
        the day of the week
    :type date: str
    :return: day of the week
    :rtype: str
    """
    try:
        day = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
        f_day = datetime.strftime(day, '%A')


    except ValueError:
        day = datetime.strptime(date, '%Y-%m-%d')
        f_day = datetime.strftime(day, '%A')

    return f_day
