from flask import Flask, render_template, Response
import requests

app = Flask(__name__)

@app.route('/transformer', methods=['GET', 'POST'])
# a get request should be made for service 2 and 4
def show_transformer():
    s2 = requests.get('http://service2:5001/get/colour')
    s3 = requests.get('http://service3:5002/get/car')
    transformer = s2+","+s3
    result = requests.post('http://service4:5003/post/transformer', data=transformer)




    return Response(transformer, mimetype='text/plain')

if __name__ == '__main__':
    app.run(port=5000, debug = True, host='0.0.0.0')
