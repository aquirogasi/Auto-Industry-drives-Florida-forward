from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import requests
import pandas as pd
import json
import folium

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    key = 'fFQ4L2pmBt9NT77Q4fQmPrdjQLmtMHLN'
    url = 'https://dev.tollguru.com/v1/calc/here'
    headers = {'Content-type': 'application/json', 'x-api-key': key}

    params = {'from': {'address': '1001 Whitehead St, Key West, FL'}, 'to': {'address': '1555 Delaney Dr, Tallahassee, FL 32309'}, 'vehicleType': '2AxlesAuto'}

    response = requests.post(url, json=params, headers=headers)

    data = response.json()

    routes = data['routes']

    costs = routes[0]['costs']

    latitud = []
    longitud = []
    sunpass = []
    plate = []

    fuel = costs['fuel']
    plate = round(costs['licensePlate'], 2)
    sunpass = costs['tag']

    tolls = routes[0]['tolls']

    for toll in tolls:
        for t in toll:
            if t == 'lat':
                latitud.append(toll[t])


    for toll in tolls:
        for t in toll:
            if t == 'lng':
                longitud.append(toll[t])

    m = folium.Map(location= [25.7617, -80.1918], tiles= 'Stamen Terrain', zoom_start=10)

    def map_location(latitud, longitud):
        for i in range(len(latitud)):
            folium.Marker(location= [latitud[i], longitud[i]]).add_to(m)

        return m

    mapping = map_location(latitud, longitud)

    m.save("map.html")

    return mapping._repr_html_()

if __name__ == '__main__':
    app.run(debug=True, port=5002)
