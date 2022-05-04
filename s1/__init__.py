from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/transformer', methods=['GET', 'POST'])
# a get request should be made for service 2 and 4
