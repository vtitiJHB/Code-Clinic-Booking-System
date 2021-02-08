from sys import argv
import os


def create_folder(path):
    """
    checks to see if the folder at the given path exists if not it
        makes it

    :param path: a string of the path to a folder to be checked
    :type path: str
    """
    if not os.path.exists(path):
        os.mkdir(path)


def remove_folder():
    """
    removes save data from both the user and the clinics calendars
    """
    pathname = os.path.abspath(os.path.dirname(argv[0])) + '/program'

    if os.path.exists(f'{pathname}/saves'):
        for save_file in os.listdir(f'{pathname}/saves'):
            os.remove(f'{pathname}/saves/{save_file}')
        os.rmdir(f'{pathname}/saves')
