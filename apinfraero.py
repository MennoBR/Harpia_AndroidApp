# API conectada a Infraero para dar informações sobre os aeroportos aos usuários.
# Já solicitei uma chave de API a Infraero, ainda esperando.

import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/infraero')
def get_infraero_data():
    url = 'https://www4.infraero.gov.br/index.php/voos/voos-online/departures'
    response = requests.get(url)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run()










