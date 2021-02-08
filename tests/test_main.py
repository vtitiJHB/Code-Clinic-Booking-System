# made by henry as a file to run all unittests in the tests/ folder
import unittest
from io import StringIO
import sys
from tests.test_base import captured_io
from tests.test_base import run_unittests
import unittest
from unittest.mock import patch
from io import StringIO
from program.general import *
from program.bookings import *
from program.viewing import *
from dateutil.relativedelta import relativedelta
from datetime import datetime

class MyTestCase(unittest.TestCase):

    def test_userinput(self):
        import tests.test_user_input
        test_result = run_unittests("tests.test_user_input")
        self.assertTrue(test_result.wasSuccessful(), 
            "unit tests should succeed")

    def test_timeinput(self):
        import tests.test_time_input
        test_result = run_unittests("tests.test_time_input")
        self.assertTrue(test_result.wasSuccessful(), 
            "unit tests should succeed")

    def test_two_digit_input(self):
        with captured_io(StringIO('12\n\n')) as (out, err):
            user_input.two_digit_input()
        
        output = out.getvalue().strip()

        self.assertEqual("""Enter the day's date as a numerical value (eg. 12):""", output)
    

    def test_viewing(self):
        with captured_io(StringIO('08:30\n\n')) as (out, err):
            user_input.time_input()

        output = out.getvalue().strip()

        self.assertEqual("""Enter the time as 24-hour digits (eg. 'nine thirty PM' = 21:30):""", output)    


    def test_general_get_new_login(self):
        with captured_io(StringIO('msibiya@student.wethinkcode.co.za\n7\n')) as (out, err):
            calendar=None
            create_init.get_new_login(calendar)

        output = out.getvalue().strip()

        self.assertEqual("""Enter your WeThinkCode email address : Enter the number of calendar days to download (min=2; max=10) :""",output)
    

    def test_event_creation(self):
        date_time_str = '20/12/11 08:30:00'
        start_t = datetime. strptime(date_time_str, '%y/%m/%d %H:%M:%S')
        
        self.assertEqual(event_creation.create_events('Code Clinic',
        'jhbcodingclinicteam6@gmail.com',
        'msibiya@student.wethinkcode.co.za',start_t),[
            {
            'summary': 'Code Clinic',
            'description': 'Volunteer Available',
            'maxAttendee': 2,
            'start': {
                'dateTime': '2020-12-11T08:30:00+02:00',
                'timeZone': 'Africa/Johannesburg',
                },
            'end': {
                'dateTime': '2020-12-11T09:00:00+02:00',
                'timeZone': 'Africa/Johannesburg',
                },
            'organizer': {
                'email': 'jhbcodingclinicteam6@gmail.com',
                },
            'attendees': [
                {
                'email': 'msibiya@student.wethinkcode.co.za',
                'optional': False,
                'comment': 'volunteer',
                'responseStatus': 'accepted',
                }
            ]
        },
        {
            'summary': 'Code Clinic',
            'description': 'Volunteer Available',
            'maxAttendee': 2,
            'start': {
                'dateTime': '2020-12-11T09:00:00+02:00',
                'timeZone': 'Africa/Johannesburg',
                },
            'end': {
                'dateTime': '2020-12-11T09:30:00+02:00',
                'timeZone': 'Africa/Johannesburg',
                },
            'organizer': {
                'email': 'jhbcodingclinicteam6@gmail.com',
                },
            'attendees': [
                {
                'email': 'msibiya@student.wethinkcode.co.za',
                'optional': False,
                'comment': 'volunteer',
                'responseStatus': 'accepted',
                }
            ]
        },{
            'summary': 'Code Clinic',
            'description': 'Volunteer Available',
            'maxAttendee': 2,
            'start': {
                'dateTime': '2020-12-11T09:30:00+02:00',
                'timeZone': 'Africa/Johannesburg',
                },
            'end': {
                'dateTime': '2020-12-11T10:00:00+02:00',
                'timeZone': 'Africa/Johannesburg',
                },
            'organizer': {
                'email': 'jhbcodingclinicteam6@gmail.com',
                },
            'attendees': [
                {
                'email': 'msibiya@student.wethinkcode.co.za',
                'optional': False,
                'comment': 'volunteer',
                'responseStatus': 'accepted',
                }
            ]
        }
        ])
        

    def test_event_creation_invalid_dateTime(self):

        date_time_str = '20/12/11 08:30:00'
        start_t = datetime. strptime(date_time_str, '%y/%m/%d %H:%M:%S')
        
        self.assertNotEqual(event_creation.create_events('Code Clinic',
        'jhbcodingclinicteam6@gmail.com',
        'msibiya@student.wethinkcode.co.za',start_t),[
            {
            'summary': 'Code Clinic',
            'description': 'Volunteer Available',
            'maxAttendee': 2,
            'start': {
                'dateTime': '2020-12-11Z08:30:00+02:00',
                'timeZone': 'Africa/Johannesburg',
                },
            'end': {
                'dateTime': '2020-12-11Z09:00:00+02:00',
                'timeZone': 'Africa/Johannesburg',
                },
            'organizer': {
                'email': 'jhbcodingclinicteam6@gmail.com',
                },
            'attendees': [
                {
                'email': 'msibiya@student.wethinkcode.co.za',
                'optional': False,
                'comment': 'volunteer',
                'responseStatus': 'accepted',
                }
            ]
        },
        {
            'summary': 'Code Clinic',
            'description': 'Volunteer Available',
            'maxAttendee': 2,
            'start': {
                'dateTime': '2020-12-11Z09:00:00+02:00',
                'timeZone': 'Africa/Johannesburg',
                },
            'end': {
                'dateTime': '2020-12-11Z09:30:00+02:00',
                'timeZone': 'Africa/Johannesburg',
                },
            'organizer': {
                'email': 'jhbcodingclinicteam6@gmail.com',
                },
            'attendees': [
                {
                'email': 'msibiya@student.wethinkcode.co.za',
                'optional': False,
                'comment': 'volunteer',
                'responseStatus': 'accepted',
                }
            ]
        },{
            'summary': 'Code Clinic',
            'description': 'Volunteer Available',
            'maxAttendee': 2,
            'start': {
                'dateTime': '2020-12-11Z09:30:00+02:00',
                'timeZone': 'Africa/Johannesburg',
                },
            'end': {
                'dateTime': '2020-12-11Z10:00:00+02:00',
                'timeZone': 'Africa/Johannesburg',
                },
            'organizer': {
                'email': 'jhbcodingclinicteam6@gmail.com',
                },
            'attendees': [
                {
                'email': 'msibiya@student.wethinkcode.co.za',
                'optional': False,
                'comment': 'volunteer',
                'responseStatus': 'accepted',
                }
            ]
        }
        ])


    def test_day_of_week(self):
        
        self.assertEqual(event_printout.day_of_week(
            '2020-12-11'), 'Friday')
    

    def test_day_of_week_invalid_string(self):

        self.assertNotEqual(event_printout.day_of_week(
            '2020-12-11'), '2020')


if __name__ == "__main__":
    unittest.main()