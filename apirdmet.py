# API oficial com dados oficiais de aviação da rede Redemet,
# para compilar e fazer o display no App.

import requests
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config

# Travando a janela:
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')

class RedemetApp(App):
    def build(self):
        # create the layout
        layout = FloatLayout()

        # Pegando as informações do clima da API(com tratamento de erros e exceções):
        url = "http://api.redemet.aer.mil.br/api/v1/meteograma/prev/24/prognostico/80568?fields=temperature,relativeHumidity,windDirection,windSpeed,pressure,precipitation&api_key=xzvjAbr90ReXv02lZa8zWV4DPqzoNW1eaIiIopkF"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            # Mostrando os dados:
            temp = data["temperature"][0]["value"]
            temp_label = Label(text=f"Temperatura: {temp}°C", font_size=20, pos_hint={"x": 0.05, "top": 0.9})
            layout.add_widget(temp_label)

            humidity = data["relativeHumidity"][0]["value"]
            humidity_label = Label(text=f"\nHumidade: {humidity}%", font_size=20, pos_hint={"x": 0.05, "top": 0.8})
            layout.add_widget(humidity_label)

            wind_dir = data["windDirection"][0]["value"]
            wind_speed = data["windSpeed"][0]["value"]
            wind_label = Label(text=f"\nVentos: {wind_dir} {wind_speed}km/h", font_size=20,
                               pos_hint={"x": 0.05, "top": 0.7})
            layout.add_widget(wind_label)

            pressure = data["pressure"][0]["value"]
            pressure_label = Label(text=f"\nPressão: {pressure}hPa", font_size=20, pos_hint={"x": 0.05, "top": 0.6})
            layout.add_widget(pressure_label)

            precipitation = data["precipitation"][0]["value"]
            precipitation_label = Label(text=f"\nPrecipitação: {precipitation}mm", font_size=20,
                                        pos_hint={"x": 0.05, "top": 0.5})
            layout.add_widget(precipitation_label)

        except requests.exceptions.RequestException as e:
            error_label = Label(text=f"Erro: {str(e)}", font_size=20, pos_hint={"x": 0.05, "top": 0.9})
            layout.add_widget(error_label)

        return layout


if __name__ == "__main__":
    RedemetApp().run()
