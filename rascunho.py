# Rascunho / Testes:

#Aviator2ndTela.py funcional VR 1:

'''# Segunda tela do APP: Mostrará informações metereológicas ao usuário da cidade escolhida.
# Será acoplada com as informações da Api já criada "ClimaNOW"

import APIClimaNOW
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle


class SegundaTela(GridLayout):
    def __init__(self, **kwargs):
        super(SegundaTela, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text="Informações do Clima na Rota:", font_size=20, color='green'))
        self.add_widget(Label(text="", size_hint_y=None, height=100, color=[1, 1, 1, 1]))


        atual = APIClimaNOW.get_atual("São Paulo")

        info_box = BoxLayout(orientation='vertical', padding=[20, 20, 20, 20], size_hint_y=None, height=400,
                             pos_hint={"center_x": 0.5, "center_y": 0.5})
        with info_box.canvas:
            Color(1, 1, 1, 1)
            Rectangle(pos=info_box.pos, size=info_box.size, )
        info_box.add_widget(Label(text=f"Cidade: {atual['city']}", font_size=15, color='green'))
        info_box.add_widget(Label(text=f"Temperatura: {atual['temperature']:.2f} °C", font_size=15, color='green'))
        info_box.add_widget(Label(text=f"Umidade: {atual['humidity']}%", font_size=15, color='green'))
        info_box.add_widget(Label(text=f"Descrição: {atual['description']}", font_size=15, color='green'))
        info_box.add_widget(Label(text=f"Velocidade do vento: {atual['wind_speed']}", font_size=15, color='green'))
        self.add_widget(info_box)'''