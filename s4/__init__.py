from flask import Flask, Response
import requests

app == Flask(__name__)

@app.route('post/transformer', methods =['POST'])
# two get requests are needed for service 2 and 3
# use these in logic for transformers.
def get_transformer():
    colours = requests.get()
    car_list = requests.get()

    if colours == "yellow" and car_list == "Mustang":
        transformer = "Bumblebee"
    # add rest of elif statements


    return Response(transformer, mimetype='text/plain')


# additional response for jenkins testing
# this will tell us if they are autobot or decepticon
@app.route('post/army', methods=['POST'])

def get_army():
    
    if transformer == "Bumblebee":
        army = "Autobots"

    # add remaining elif statements

    return Response(army, mimetype='text/plain')



    

