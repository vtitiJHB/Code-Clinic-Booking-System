from pathlib import Path
from time import sleep
from sys import argv
import pickle
import os

from program.general.file_handling import create_folder
from program.general.admin_setup import account_login


def init_setup_call(calendar):
    """
    Check the user made an init_setup_call.
    If the call was not made, load the required data.

    :param calendar: google calendar
    :type calendar: resource object
    :return: days - number of calendar days to download, 
            user_email - user's email address, 
            user_creds - credentials for linking to the user's calendar
            days - int
            user_email - string, 
            user_creds - credentials object
    """
    pathname = os.path.abspath(os.path.dirname(argv[0])) + '/program'
    create_folder(f'{pathname}/tokens')
    p_home = str(Path.home())

    if 'init' in argv:
        days, user_email = get_new_login(calendar)
        user_creds = account_login()
        check_terminal_setup()

    elif os.path.exists(f'{p_home}/.user_creds.pickle'):
        with open(f'{p_home}/.user_creds.pickle', 'rb') as creds_file:
            user_creds = pickle.load(creds_file)

    else:
        user_creds = account_login()

    if (os.path.exists(f'{pathname}/tokens/token_user_setup.pickle')
            and not 'init' in argv):
        with open(f'{pathname}/tokens/token_user_setup.pickle', 'rb') as token:
            days = pickle.load(token)
            user_email = pickle.load(token)

    elif not 'init' in argv:
        days, user_email = get_new_login(calendar)
        check_terminal_setup()

    with open(f'{pathname}/tokens/token_user_setup.pickle', 'wb') as token:
        pickle.dump(days, token)
        pickle.dump(user_email, token)
        pickle.dump(user_creds, token)

    with open(f'{p_home}/.user_creds.pickle', 'wb') as creds_file:
        pickle.dump(user_creds, creds_file)

    os.system('clear')

    return days, user_email, user_creds


def get_new_login(calendar):
    """
    Get the user's WeThinkCode email address. 
    Get the number of viewable days for the user's WeThinkCode Calendar.

    :param calendar: google calendar
    :type calendar: resource object
    :return: credentials, days_to_download data
    :rtype: int, str
    """
    user_email = input("Enter your WeThinkCode email address : ")
    while not ('@student.wethinkcode.co.za' in user_email):
        user_email = input('You may only use your WeThinkCode email address: ')

    text_1 = "Enter the number of calendar days to download (min=2; max=10) : "
    days = input(text_1)

    while (not days.isdigit() or (int(days) < 2 or int(days) > 10)):
        text_1 = "Enter the number of calendar days to"
        text_1 = text_1 + " download (min=2; max=10) : "
        days = input(text_1)

    if days == "":
        return 7, user_email.lower()

    return int(days), user_email.lower()


def check_terminal_setup():
    """
    Check the terminal script has a setup command to make
        the file executable
    """
    pathname = os.path.abspath(os.path.dirname(argv[0]))
    p_home = str(Path.home())

    if os.path.exists(f"{p_home}/.zshrc"):
        with open(f"{p_home}/.zshrc", 'r+') as open_file:
            the_lines = open_file.readlines()

            if (not f'export PATH="$PATH:{pathname}"' in the_lines
                    and not f'export PATH="$PATH:{pathname}"\n' in the_lines):

                open_file.write(f'\nexport PATH="$PATH:{pathname}"')

    if os.path.exists(f"{p_home}/.bashrc"):
        with open(f"{p_home}/.bashrc", 'r+') as open_file:
            the_lines = open_file.readlines()

            if (not f'PATH=$PATH:{pathname}' in the_lines
                    and not f'PATH=$PATH:{pathname}\n' in the_lines):

                open_file.write(f'\nPATH=$PATH:{pathname}')
