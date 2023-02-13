
# Segunda tela do APP: Mostrará informações metereológicas ao usuário da cidade escolhida.
# Será acoplada com as informações da Api já criada "ClimaNOW"

import APIClimaNOW
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class SegundaTela(GridLayout):
    def __init__(self, **kwargs):
        super(SegundaTela, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text="Informações do Clima:", font_size=20, color=[1, 1, 1, 1]))
        self.add_widget(Label(text="", size_hint_y=None, height=100, color=[1, 1, 1, 1]))


        atual = APIClimaNOW.get_atual("São Paulo")
        self.add_widget(Label(text=f"Cidade: {atual['city']}", font_size=15))
        self.add_widget(Label(text=f"Temperatura: {atual['temperature']} °C", font_size=15))
        self.add_widget(Label(text=f"Umidade: {atual['humidity']}%", font_size=15))
        self.add_widget(Label(text=f"Descrição: {atual['description']}", font_size=15))