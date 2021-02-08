import unittest
from program.bookings import user_input
from unittest.mock import patch
from io import StringIO 

class MyTestCase(unittest.TestCase):

    @patch("sys.stdin", StringIO("av\nbd\n124\n12\n"))
    def test_1(self):
        self.assertTrue(1<=user_input.two_digit_input()<=31)

    @patch("sys.stdin", StringIO("av\nbd\n32\n12\n"))
    def test_2(self):
        self.assertTrue(1<=user_input.two_digit_input()<=31)

    @patch("sys.stdin", StringIO("exit\n"))
    def test_3(self):
        self.assertEqual('exit', user_input.two_digit_input())   

    @patch("sys.stdin", StringIO("quit\n"))
    def test_4(self):
        self.assertEqual('exit', user_input.two_digit_input())    


if __name__ == "__main__":
    unittest.main()