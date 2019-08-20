from flask import Flask
from flask import jsonify
import os
import random

app = Flask(__name__)

@app.route('/api/artpiece/<token_id>')
def artpiece(token_id):
    token_id = int(token_id)
    artpiece_name = ""
    graphical_information_content = ""
    #for file in os.listdir(os.getcwd() + "/images"):
    for file in os.listdir("images"):
        if file.startswith("%i_"%token_id):
            artpiece_name = file[:-4].replace("_", " ")
            image_url_local = file
            graphical_information_content = int((os.path.getsize('images/%s'%file))/1000)

    #catch missing artpiece
    if artpiece_name == "":
        artpiece_name = "default missing artpiece number"
        image_url_local = ('default.png')
        graphical_information_content = 0

    #Attribute Opensea
    attributes = []
    _add_attribute(attributes, 'graphical information content', graphical_information_content, token_id, display_type="boost_number")

    #Attribute Rarebits
    attributes_rarebits = []
    _add_attribute_rarebits(attributes_rarebits, 'graphical information content', graphical_information_content)

    #Change to www.aicryptoart.org!!!
    image_url_online_storage = "http://www.aicryptoart.org/artpieces/" + image_url_local

    json_description = jsonify({
        'name': artpiece_name,
        'description': "AI generated artpiece",
        'image': image_url_online_storage, #Opensea format
        'image_url': image_url_online_storage, #Rarebits format
        'external_url': "http://www.aicryptoart.org", #Opensea format
        'home_url': "http://www.aicryptoart.org", #Rarebits format
        'attributes': attributes, #Opensea format
        'properties': attributes_rarebits
        #'properties': [{"key": "graphical information content", "value": graphical_information_content, type: "integer"}] #Rarebits format
    })
    return json_description

def _add_attribute(existing, attribute_name, options, token_id, display_type=None):
    trait = {
        'trait_type': attribute_name,
        'value': options
    }
    if display_type:
        trait['display_type'] = display_type
    existing.append(trait)

def _add_attribute_rarebits(existing, attribute_name, attribute_value):
    trait = {
        'key': attribute_name,
        'value': attribute_value
    }
    existing.append(trait)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)