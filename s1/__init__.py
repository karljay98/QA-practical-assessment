from flask import Flask, render_template, Response
import requests

app = Flask(__name__)

@app.route('/transformer', methods=['GET', 'POST'])
# a get request should be made for service 2 and 4
def show_transformer():
    s2 = request.get('http://service2.com')
    s3 = request.get('http://service3.com')
    transformer = s2+","+s3




    return Response(transformer, mimetype='text/plain')
