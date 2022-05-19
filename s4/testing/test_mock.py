import pytest
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app


class TestService4(TestBase):
    def test_bumblebee(self):

        response = self.client.post(url_for('get_transformer'), data='yellow,Mustang')
        self.assertIn(b'Bumblebee', response.data)

    def test_jazz(self):
        response = self.client.post(url_for('get_transformer'), data='yellow,Mercedes')
        self.assertIn(b'Jazz', response.data)
    
    def test_rachet(self):
        response = self.client.post(url_for('get_transformer'), data='yellow,Truck')
        self.assertIn(b'Rachet', response.data)
    
    def test_hotrod(self):
        response = self.client.post(url_for('get_transformer'), data='red,Mercedes')
        self.assertIn(b'Hot rod', response.data)

    def test_longhaul(self):
        response = self.client.post(url_for('get_transformer'), data='red,Mustang')
        self.assertIn(b'Long haul', response.data)
    
    def test_optimusprime(self):
        response = self.client.post(url_for('get_transformer'), data='red,Truck')
        self.assertIn(b'Optimus prime', response.data)

    def test_slingshot(self):
        response = self.client.post(url_for('get_transformer'), data='grey,Mercedes')
        self.assertIn(b'Slingshot', response.data)
    
    def test_barricade(self):
        response = self.client.post(url_for('get_transformer'), data='grey,Mustang')
        self.assertIn(b'Barricade', response.data)

    def test_galvatron(self):
        response = self.client.post(url_for('get_transformer'), data='grey,Truck')
        self.assertIn(b'Galvatron', response.data)

