#!/datAPI/flask/bin/python

"""
The unittest.

Tests first for proper responses from fibo.py
Tests second for actual HTTP calls to localhost
Optionally could copy HTTP calls and edit target to pub IP
"""


import unittest
from fibo import restfib
import requests


class FibTests(unittest.TestCase):

    def setUp(self):
        self.obj = restfib()

    def testNegative(self):
        self.number = -5
        test = self.obj.san_number(self.number)
        self.failUnless(test is not True)

    def testTooBig(self):
        self.number = 10000
        test = self.obj.san_number(self.number)
        self.failUnless(test is not True)

    def testIsInt(self):
        self.number = 'what'
        test = self.obj.san_number(self.number)
        self.failUnless(test is not True)

    def testTrue(self):
        self.number = 4
        test = self.obj.san_number(self.number)
        self.failUnless(test is True)

    def testAPIstring(self):
        test = requests.post("http://localhost:5000/fibo/api/v1.0/string")
        expected = {"result": {"Error01": "You must submit a whole number!"}}
        self.failUnless(test.json() == expected)

    def testAPIfloat(self):
        test = requests.post(
            "http://localhost:5000/fibo/api/v1.0/10.5")
        expected = {"result": {"Error01": "You must submit a whole number!"}}
        self.failUnless(test.json() == expected)

    def testAPINegative(self):
        test = requests.post("http://localhost:5000/fibo/api/v1.0/-10")
        expected = {"result": {"Error02": "Negative numbers not allowed."}}
        self.failUnless(test.json() == expected)

    def testAPIHugemongous(self):
        test = requests.post("http://localhost:5000/fibo/api/v1.0/1000")
        expected = {
            "result": {"Error03": "Numbers larger than 999 not allowed."}}
        self.failUnless(test.json() == expected)


if __name__ == '__main__':
    unittest.main()
