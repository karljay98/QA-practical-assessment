from flask import Flask, render_template, Response
import requests

app = Flask(__name__)

@app.route('/transformer', methods=['GET', 'POST'])
# a get request should be made for service 2 and 4
def show_transformer():
    s2 = request.get('http://service2:5001/get/colour')
    s3 = request.get('http://service3:5002/get/car')
    transformer = s2+","+s3




    return Response(transformer, mimetype='text/plain')
