# Segunda tela do APP: Mostrará informações metereológicas ao usuário da cidade escolhida.
# Será acoplada com as informações da Api já criada "ClimaNOW"

import APIClimaNOW
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window


Window.size = (800, 600)


Window.minimum_width, Window.minimum_height = Window.size

class SegundaTela(GridLayout):
    def __init__(self, **kwargs):
        super(SegundaTela, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text="Informações do Clima na Rota:", font_size=20, color='green'))
        atual = APIClimaNOW.get_atual("São Paulo")
        info_box = GridLayout(cols=2, padding=[20, 20, 20, 20], size_hint_y=None, height=400)
        info_box.add_widget(Label(text=f"Cidade:"))
        info_box.add_widget(Label(text=f"{atual['city']}", color='green'))
        info_box.add_widget(Label(text=f"Temperatura:"))
        info_box.add_widget(Label(text=f"{atual['temperature']:.2f} °C", color='green'))
        info_box.add_widget(Label(text=f"Umidade:"))
        info_box.add_widget(Label(text=f"{atual['humidity']}%", color='green'))
        info_box.add_widget(Label(text=f"Descrição:"))
        info_box.add_widget(Label(text=f"{atual['description']}", color='green'))
        info_box.add_widget(Label(text=f"Velocidade do vento:"))
        info_box.add_widget(Label(text=f"{atual['wind_speed']}", color='green'))
        self.add_widget(info_box)


class RootWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)

        harpia_logo = Image(source="Harpialogo.jpeg", size_hint=(50, 50), pos_hint={'x': 10, 'top': 0})
        self.add_widget(harpia_logo)

        with self.canvas:
            Color(0, 1, 0, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(pos=self.update_rect, size=self.update_rect)

        segunda_tela = SegundaTela(pos_hint={'x': 0, 'y': 0}, size_hint=(1, 1))
        self.add_widget(segunda_tela)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size




#código antigo:

'''class SegundaTela(GridLayout):
    def __init__(self, **kwargs):
        super(SegundaTela, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text="Informações do Clima na Rota:", font_size=20, color='green'))
        atual = APIClimaNOW.get_atual("São Paulo")
        info_box = BoxLayout(orientation='vertical', padding=[20, 20, 20, 20], size_hint_y=None, height=400)
        info_box.add_widget(Label(text=f"Cidade: {atual['city']}", font_size=15, color='green'))
        info_box.add_widget(Label(text=f"Temperatura: {atual['temperature']:.2f} °C", font_size=15, color='green'))
        info_box.add_widget(Label(text=f"Umidade: {atual['humidity']}%", font_size=15, color='green'))
        info_box.add_widget(Label(text=f"Descrição: {atual['description']}", font_size=15, color='green'))
        info_box.add_widget(Label(text=f"Velocidade do vento: {atual['wind_speed']}", font_size=15, color='green'))
        self.add_widget(info_box)


        harpia_logo = Image(source="Harpialogo.jpeg", size_hint=(20, 20), pos=(0, self.height))
        self.add_widget(harpia_logo)


        self.bind(pos=self.update_rect, size=self.update_rect)


        with self.canvas:
            Color(1, 1, 1, 1)
            Rectangle(pos=self.pos, size=self.size)

    def update_rect(self, *args):
        # clear the canvas and redraw it with a white rectangle
        self.canvas.before.clear()
        with self.canvas.before:
            Color(1, 1, 1, 1)
            Rectangle(pos=self.pos, size=self.size)'''


