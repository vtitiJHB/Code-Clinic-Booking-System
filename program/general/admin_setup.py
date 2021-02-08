import os.path
import pickle
from sys import argv

from program.general.file_handling import create_folder

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


def call_admin_setup():
    """
    checks to see if the user called the admin_setup call and if not
        loads the creds for the system

    :return: creds the credentials for connecting to the code clinic
        calendar
    :rtype: Credentials
    """
    pathname = os.path.abspath(os.path.dirname(argv[0]))
    p_path = f'{pathname}/program/creds'
    t_path = f'{pathname}/program/tokens'
    create_folder(p_path)
    create_folder(t_path)

    if 'admin_init' in argv:
        creds = account_login()
        with open(f'{p_path}/clinic_credentials.pickle', 'wb') as token:
            pickle.dump(creds, token)

    elif os.path.exists(f'{t_path}/clinic_credentials.pickle'):
        with open(f'{t_path}/clinic_credentials.pickle', 'rb') as token:
            creds = pickle.load(token)

    elif os.path.exists(f'{p_path}/clinic_credentials.pickle'):
        with open(f'{p_path}/clinic_credentials.pickle', 'rb') as token:
            creds = pickle.load(token)

    else:
        creds = account_login()
        with open(f'{t_path}/clinic_credentials.pickle', 'wb') as token:
            pickle.dump(creds, token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            with open(f'{t_path}/clinic_credentials.pickle', 'wb') as token:
                pickle.dump(creds, token)

    return creds


def account_login():
    """
    generates the credentials used for setting up a connection to the
    code clinic calendar

    :return: returns the credentials for the users google's calendar
        for our code clinic's calendar
    :rtype: Credentials
    """
    pathname = os.path.abspath(os.path.dirname(argv[0]))
    scope = ['https://www.googleapis.com/auth/calendar']

    flow = InstalledAppFlow.from_client_secrets_file(
        f'{pathname}/program/creds/credentials.json', scope)

    return flow.run_local_server(port=0)
