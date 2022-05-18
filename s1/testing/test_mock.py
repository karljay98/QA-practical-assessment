from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestService1(TestBase):
    def test_bumblebee(self):
        with requests_mock.Mocker() as m:
            m.get('http://service2:5001/get/colour', text ='yellow')
            m.get('http://service3:5002/get/car', text='Mustang')
            m.post('http://service4:5003/post/transformer',text='yellow,Mustang')
            response = self.client.get(url_for('show_transformer'))
            self.assertIn(b'yellow,Mustang', response.data)
    
    def test_jazz(self):
        with requests_mock.Mocker() as m:
            m.get('http://service2:5001/get/colour', text ='yellow')
            m.get('http://service3:5002/get/car', text='Mercedes')
            m.post('http://service4:5003/post/transformer',text='yellow,Mercedes')
            response = self.client.get(url_for('show_transformer'))
            self.assertIn(b'yellow,Mercedes', response.data)
    
    def test_rachet(self):
        with requests_mock.Mocker() as m:
            m.get('http://service2:5001/get/colour', text ='yellow')
            m.get('http://service3:5002/get/car', text='Truck')
            m.post('http://service4:5003/post/transformer',text='yellow,Truck')
            response = self.client.get(url_for('show_transformer'))
            self.assertIn(b'yellow,Truck', response.data)

    def test_hotrod(self):
        with requests_mock.Mocker() as m:
            m.get('http://service2:5001/get/colour', text ='red')
            m.get('http://service3:5002/get/car', text='Mercedes')
            m.post('http://service4:5003/post/transformer',text='red,Mercedes')
            response = self.client.get(url_for('show_transformer'))
            self.assertIn(b'red,Mercedes', response.data)

    def test_longhaul(self):
        with requests_mock.Mocker() as m:
            m.get('http://service2:5001/get/colour', text ='red')
            m.get('http://service3:5002/get/car', text='Mustang')
            m.post('http://service4:5003/post/transformer',text='red,Mustang')
            response = self.client.get(url_for('show_transformer'))
            self.assertIn(b'red,Mustang', response.data)

    def test_optimusprime(self):
        with requests_mock.Mocker() as m:
            m.get('http://service2:5001/get/colour', text ='red')
            m.get('http://service3:5002/get/car', text='Truck')
            m.post('http://service4:5003/post/transformer',text='red,Truck')
            response = self.client.get(url_for('show_transformer'))
            self.assertIn(b'red,Truck', response.data)

    def test_slingshot(self):
        with requests_mock.Mocker() as m:
            m.get('http://service2:5001/get/colour', text ='grey')
            m.get('http://service3:5002/get/car', text='Mercedes')
            m.post('http://service4:5003/post/transformer',text='grey,Mercedes')
            response = self.client.get(url_for('show_transformer'))
            self.assertIn(b'grey,Mercedes', response.data)

    def test_barricade(self):
        with requests_mock.Mocker() as m:
            m.get('http://service2:5001/get/colour', text ='grey')
            m.get('http://service3:5002/get/car', text='Mustang')
            m.post('http://service4:5003/post/transformer',text='grey,Mustang')
            response = self.client.get(url_for('show_transformer'))
            self.assertIn(b'grey,Barricade', response.data)

    def test_galvatron(self):
        with requests_mock.Mocker() as m:
            m.get('http://service2:5001/get/colour', text ='grey')
            m.get('http://service3:5002/get/car', text='Truck')
            m.post('http://service4:5003/post/transformer',text='grey,Truck')
            response = self.client.get(url_for('show_transformer'))
            self.assertIn(b'grey,Truck', response.data)