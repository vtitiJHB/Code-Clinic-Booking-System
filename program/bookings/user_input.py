from dateutil.relativedelta import relativedelta
from datetime import datetime

from program.viewing.custom_color import color


def user_booking_input(the_map):
    """
    We ask the user to enter a day, month and time.
    We also check if the input is an available slot
    We convert it to the format of a datetime object

    :param the_map: The list full of open events & days
    :type the_map: list
    :return: the datetime for the start of a new event
    :rtype: datetime
    """

    u_day = two_digit_input()
    if (u_day == 'exit'): return None

    e_date = datetime.now()
    d_day = int(datetime.strftime(datetime.now(), '%d'))

    if u_day < d_day:
        e_date = e_date + relativedelta(months=1)
        e_date = e_date + relativedelta(day=u_day )

    elif u_day > d_day:
        e_date = e_date + relativedelta(day=u_day)

    s_date = datetime.strftime(e_date, '%Y-%h-%d')
    the_date = f"{color.f_b_u_c}{s_date}{color.end}"
    while True:
        replay = input(f'Is this the correct date {the_date} [y/n]: ')
        if replay.lower() == 'exit' or replay.lower() == 'quit': return None

        if replay.lower() == 'y' or replay.lower() == 'yes':
            break

        elif replay.lower() == 'n' or replay.lower() == 'no':
            return user_booking_input(the_map)

    time = time_input()
    if (time == 'exit'): return None

    month = datetime.strftime(e_date, '%m')
    
    if f'{int(month)}-{int(u_day)}' in the_map:
        
        if time in the_map[f'{int(month)}-{int(u_day)}']:
            final_date = datetime.strftime(e_date, '%Y/%m/%d')
            start_date = final_date + " " + time + ":00"
            start_t = datetime.strptime(start_date, '%Y/%m/%d %H:%M:%S')
            return start_t

    print('Pick a date and time from an available slot')

    return user_booking_input(the_map)


def patient_booking_input(the_map):
    """
    gets the users description for the event and other date input

    :param the_map: open events
    :type the_map: list
    :return: date and time, event description
    :rtype: datetime object, string
    """
    date_obj = user_booking_input(the_map)

    if date_obj == None:
        return None

    description = ''

    while not description:
        description = input("Enter the topic you need help with: ")

    return date_obj, description


def two_digit_input():
    """
    We ask the user to enter a day/month/year
    We check if the format is correct

    :return: the day/month/year/None
    :rtype: int/None
    """

    x = input("Enter the day's date as a numerical value (eg. 12): ")
    try:
        if ('quit' in x.lower() or 'exit' in x.lower()):
            return 'exit'
        x_int = int(x)
        if (1 <= x_int <= 31):
            return x_int
    except:
        pass
    print("You may only use the digit format for the day eg. '2020-Dec-07' Monday = 7")
    return two_digit_input()


def time_input():
    """
    Get the time as user input.

    :return: 12 hour digital format
    :rtype: string
    """
    while True:
        x = input("Enter the time as 24-hour digits (eg. 'nine thirty PM' = 21:30): ")
        try:
            if ('quit' in x.lower() or 'exit' in x.lower()):
                return 'exit'
            if not((':' in x) and (len(x) == 5) and (x[0:2].isdigit())
            and (0 <= int(x[0:2]) <= 24) and (x[3:5].isdigit()) 
            and (0 <= int(x[3:5])<= 59)):
                pass
            else:
                return x
        except:
            pass
        print("You may only use the 24-hour format for the time eg. 'nine thirty AM' = 09:30")
