from flask import Flask, Response
import requests

app == Flask(__name__)

@app.route('post/transformer', methods =['POST'])
# two get requests are needed for service 2 and 3
# use these in logic for transformers.
def get_transformer():
    colours = requests.get('http://service1:5000/get/colour')
    car_list = requests.get('http://service1:5000/get/car')
    transformer = request.data.decode('utf-8')
    transformer_split = transformer_car.split(",")
    car = transformer_split[0]
    colour = transformer_split[1]

    if colour == "yellow" and car_list == "Mustang":
        transformer = "Bumblebee"
    elif colour == "yellow" and car_list == "Mercendes":
        transfromer = "Jazz"
    elif colour == "yellow" and car_list == "Truck":
        transformer = "Rachet"
    elif colour == "red" and car_list == "Mercendes":
        transformer = "Hot rod"
    elif colour == "red" and car_list == "Mustang":
        transformer = "Long haul"
    elif colour == "red" and car_list == "Truck":
        transfromer = "Optimus prime"
    elif colour == "grey" and car_list == "Mercendes":
        transformer = "Slingshot"
    elif colour == "grey" and car_list == "Mustang":
        transformer = "Barricade"
    else:
        transformer = "Galvatron"

    return Response(transformer, mimetype='text/plain')


# additional response for jenkins testing
# this will tell us if they are autobot or decepticon
#@app.route('post/army', methods=['POST'])

#def get_army():
    
    #if transformer == "Bumblebee":
        #army = "Autobots"

    # add remaining elif statements

    #return Response(army, mimetype='text/plain')



    

