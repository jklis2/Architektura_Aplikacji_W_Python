# -*- coding: utf-8 -*-
import unittest
from wsei_email import WseiEmails

class TestWseiEmails(unittest.TestCase):
    def test_validate_valid_email(self):
        email = "jan.kowalski@wsei.edu.pl"
        wsei_email = WseiEmails(email)
        self.assertTrue(wsei_email.validate())

    def test_validate_invalid_email(self):
        email = "jan.kowalski@example.com"
        wsei_email = WseiEmails(email)
        self.assertFalse(wsei_email.validate())

if __name__ == '__main__':
    unittest.main()    