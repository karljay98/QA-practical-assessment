from unittest.mock import patch
from flask import url_for, request
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestService3(TestBase):
    def test_mercendes(self):
        with patch('random.randint') as r:
            r.return_value = 0
            response = self.client.get(url_for('cars'))
            self.assertIn(b'Mercedes', response.data)

    def test_mustang(self):
        with patch('random.randint') as r:
            r.return_value = 1
            response = self.client.get(url_for('cars'))
            self.assertIn(b'Mustang', response.data)

    def test_mercendes(self):
        with patch('random.randint') as r:
            r.return_value = 2
            response = self.client.get(url_for('cars'))
            self.assertIn(b'Truck', response.data)

