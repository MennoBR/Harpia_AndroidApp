# API oficial com dados oficiais de aviação da rede Redemet,
# para compilar e fazer o display no App.

from flask import Flask, jsonify
import requests

app = Flask(__name__)

API_KEY = 'xzvjAbr90ReXv02lZa8zWV4DPqzoNW1eaIiIopkF'

@app.route('/weather/<icao_code>')
def get_weather(icao_code):
    url = f'https://api-redemet.decea.gov.br/mg/{icao_code}'
    headers = {'X-Api-Key': API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        clima = {
            'icao_code': data['local'],
            'temperature': data['temperatura'],
            'dew_point': data['temperatura_ponto_orvalho'],
            'wind_direction': data['direcao_vento'],
            'wind_speed': data['velocidade_vento'],
            'pressure': data['pressao_atm'],
            'humidity': data['umidade_rel']
        }
        return jsonify(clima)
    else:
        return jsonify({'error': 'Sem contato com a central, tente de novo.'}), 500

#mostrando informação ao usuário:



if __name__ == '__main__':
    app.run(debug=True)
