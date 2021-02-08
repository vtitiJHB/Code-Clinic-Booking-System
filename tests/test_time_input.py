import unittest
from program.bookings import user_input
from unittest.mock import patch
from io import StringIO 

class MyTestCase(unittest.TestCase):

    @patch("sys.stdin", StringIO("10:3a\n10:30\n"))
    def test_1(self):
        self.assertEqual('10:30', user_input.time_input())

    @patch("sys.stdin", StringIO("10:99\n10:30\n"))
    def test_2(self):
        self.assertEqual('10:30', user_input.time_input())

    @patch("sys.stdin", StringIO("exit\n"))
    def test_3(self):
        self.assertEqual('exit', user_input.time_input())  

    @patch("sys.stdin", StringIO("quit\n"))
    def test_4(self):
        self.assertEqual('exit', user_input.time_input())    


if __name__ == "__main__":
    unittest.main()