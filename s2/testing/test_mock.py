from flask import url_for
from flask_testing import TestCase
import requests_mock

from s2 import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestService2(TestBase):
    def test_yellow(self):
        with patch('random.randint') as r:
            r.return_value = 0
            response = self.client.get(url_for('colour'))
            self.assertIn(b'yellow', response.data)

    def test_red(self):
        with patch('random.randint') as r:
            r.return_value = 1
            response = self.client.get(url_for('colour'))
            self.assertIn(b'red', response.data)

    def test_grey(self):
        with patch('random.randint') as r:
            r.return_value = 2
            response = self.client.get(url_for('colour'))
            self.assertIn(b'grey', response.data)

    
