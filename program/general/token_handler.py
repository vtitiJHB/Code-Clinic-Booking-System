import pickle
import os

from dateutil.relativedelta import relativedelta
from datetime import datetime


def token_check(token_name):
    """
    check to see if the token exists

    :param token_name: the token file name to search for
    :type token_name: str
    :return: returns a boolean, True if token is valid false if not
    :rtype: boolean
    """
    token_data = None

    if os.path.exists(f"tokens/{token_name}.pickle"):
        with open(f"tokens/{token_name}.pickle", 'rb') as token:
            token_data = pickle.load(token)

    if not token_data or time_check(token_data):
        return False
    return True


def time_check(data):
    """
    To check if the token was created in the past ten minutes

    :param data: the token file data to unpickle
    :type data: str
    :return: returns a boolean, True if created in the past 10 
        minutes False if not
    :rtype: boolean
    """
    token_time = data.replace("T", " ").replace("Z", "")
    now = datetime.utcnow()
    new_t = datetime.strptime(token_time, '%Y-%m-%d %H:%M:%S.%f') + \
        relativedelta(minutes=10)

    if now > new_t:
        return True
    return False


def clear_tokens():
    """
    removes tokens to force calendar updates
    """
    if os.path.exists("tokens/token_calendar_clinic.pickle"):
        os.remove('tokens/token_calendar_clinic.pickle')
    if os.path.exists("tokens/token_calendar_users.pickle"):
        os.remove('tokens/token_calendar_users.pickle')
