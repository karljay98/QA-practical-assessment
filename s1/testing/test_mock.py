from flask import url_for
from flask_testing import TestCase
import requests_mock

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestService1(TestBase):
    def test_bumblebee(self):
        with requests_mock.Mocker as m:
            m.get('http://service2:5001/get/colour', text ='yellow')
            m.get('http://service3:5002/get/car', text='Mustang')
            response = self.client.get(url_for('show_transformer'))
            self.assertIn(b'Bumblebee', response.data)
    
    def test_jazz(self):
        with requests_mock.Mocker as m:
            m.get('http://service2:5001/get/colour', text ='yellow')
            m.get('http://service3:5002/get/car', text='Mercendes')
            response = self.client.get(url_for('show_transformer'))
            self.assertIn(b'Jazz', response.data)
    
    def test_rachet(self):
        with requests_mock.Mocker as m:
            m.get('http://service2:5001/get/colour', text ='yellow')
            m.get('http://service3:5002/get/car', text='Truck')
            response = self.client.get(url_for('show_transformer'))
            self.assertIn(b'Rachet', response.data)

    def test_hotrod(self):
        with requests_mock.Mocker as m:
            m.get('http://service2:5001/get/colour', text ='red')
            m.get('http://service3:5002/get/car', text='Mercendes')
            response = self.client.get(url_for('show_transformer'))
            self.assertIn(b'Hot rod', response.data)

    def test_longhaul(self):
        with requests_mock.Mocker as m:
            m.get('http://service2:5001/get/colour', text ='red')
            m.get('http://service3:5002/get/car', text='Mustang')
            response = self.client.get(url_for('show_transformer'))
            self.assertIn(b'Long haul', response.data)

    def test_optimusprime(self):
        with requests_mock.Mocker as m:
            m.get('http://service2:5001/get/colour', text ='red')
            m.get('http://service3:5002/get/car', text='Truck')
            response = self.client.get(url_for('show_transformer'))
            self.assertIn(b'Optimus prime', response.data)

    def test_slingshot(self):
        with requests_mock.Mocker as m:
            m.get('http://service2:5001/get/colour', text ='grey')
            m.get('http://service3:5002/get/car', text='Mercendes')
            response = self.client.get(url_for('show_transformer'))
            self.assertIn(b'Slingshot', response.data)

    def test_barricade(self):
        with requests_mock.Mocker as m:
            m.get('http://service2:5001/get/colour', text ='grey')
            m.get('http://service3:5002/get/car', text='Mustang')
            response = self.client.get(url_for('show_transformer'))
            self.assertIn(b'Barricade', response.data)

    def test_galvatron(self):
        with requests_mock.Mocker as m:
            m.get('http://service2:5001/get/colour', text ='grey')
            m.get('http://service3:5002/get/car', text='Truck')
            response = self.client.get(url_for('show_transformer'))
            self.assertIn(b'Galvatron', response.data)