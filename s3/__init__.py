from flask import Flask, Response
import random

app == Flask(__name__)

@app.route('/get/car')
def cars():
    car_list = ["Audi", "Mercedes", "Mustang", "Truck", "BMW" ]
    n = random.randint(0,4)
    return Response (car_list[n], mimetype='text/plain')

if __name__ == ' main ':
    app.run(port=5002, debug=True, host='0.0.0.0')