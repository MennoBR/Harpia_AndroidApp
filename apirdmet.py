# API oficial com dados oficiais de aviação da rede Redemet,
# para compilar e fazer o display no App.


import requests
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

API_KEY = 'xzvjAbr90ReXv02lZa8zWV4DPqzoNW1eaIiIopkF'

class Redemet(App):

    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Add a label to display the weather data
        self.weather_label = Label(text="")

        # Add the label to the layout
        layout.add_widget(self.weather_label)

        return layout

    def on_start(self):
        # Retrieve the weather data
        icao_code = "SBSP"
        url = 'https://api-redemet.decea.gov.br/mg/{}'.format(icao_code)
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


            self.weather_label.text = f"Código ICAO : {clima['icao_code']}\nTemperatura: {clima['temperature']}°C" \
                                      f"\nPonto orvalho: {clima['dew_point']}°C\nDireção vento: {clima['wind_direction']}°" \
                                      f"\nVelocidade vento: {clima['wind_speed']} kts\nPressão: {clima['pressure']}" \
                                      f" hPa\nHumidade: {clima['humidity']}%"
        else:
            self.weather_label.text = 'Erro: Não foi possível acessar os dados'

if __name__ == '__main__':
    Redemet().run()
