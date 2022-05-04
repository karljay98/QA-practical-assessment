from flask import Flask, Response
import requests

app == Flask(__name__)

@app.route('get/transformer', methods =['POST'])
# two get requests are needed for service 2 and 3
# use these in logic for transformers.
def get_transformer():
    