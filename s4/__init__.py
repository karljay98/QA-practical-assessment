from flask import Flask, Response

app == Flask(__name__)

@app.route('get/transformer', methods =['GET', 'POST'])
def get_transformer():
    