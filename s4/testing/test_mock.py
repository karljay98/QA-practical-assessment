from unittest.mock import patch
from flask import url_for, request
from flask_testing import TestCase

from s2 import app

class TestBase(TestCase):
    def create_app(self):
        return app


class TestService4(TestBase):
    def test_bumblebee(self):
        response = self.client.post(url_for('get_transfromer'))

