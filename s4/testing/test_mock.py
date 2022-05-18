import pytest
from unittest.mock import patch
from flask import url_for, request
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app


class TestService4(TestBase):
    def test_bumblebee(self):

        response = self.client.post(url_for('get_transfromer'), data='yellow,Mustang')
        self.assertIN(b'Bumblebee', response.data)

        response = self.client.post(url_for('get_transfromer'), data='yellow,Merdedes')
        self.assertIN(b'Jazz', response.data)

        response = self.client.post(url_for('get_transfromer'), data='yellow,Truck')
        self.assertIN(b'Rachet', response.data)

        response = self.client.post(url_for('get_transfromer'), data='red,Mercedes')
        self.assertIN(b'Hot rod', response.data)

        response = self.client.post(url_for('get_transfromer'), data='red,Mustang')
        self.assertIN(b'Long haul', response.data)

        response = self.client.post(url_for('get_transfromer'), data='red,Mercedes')
        self.assertIN(b'Hot rod', response.data)

        response = self.client.post(url_for('get_transfromer'), data='red,Truck')
        self.assertIN(b'Optimus prime', response.data)

        response = self.client.post(url_for('get_transfromer'), data='grey,Mercedes')
        self.assertIN(b'Slingshot', response.data)

        response = self.client.post(url_for('get_transfromer'), data='grey,Mustang')
        self.assertIN(b'Barricade', response.data)

        response = self.client.post(url_for('get_transfromer'), data='grey,Truck')
        self.assertIN(b'Galvatron', response.data)


