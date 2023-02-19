# Segunda tela do APP: Mostrará informações metereológicas ao usuário da cidade escolhida.
# Será acoplada com as informações da Api já criada "ClimaNOW"

import APIClimaNOW
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config


Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '400')
Config.set('graphics', 'minimum_width', '400')
Config.set('graphics', 'minimum_height', '300')
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'window_state', 'maximized')

#Definindo a base.
class SegundaTela(GridLayout):
    def __init__(self, **kwargs):
        super(SegundaTela, self).__init__(**kwargs)
        self.cols = 1
        profpic = Image(source="fotobranca.jpg", size_hint=(None, None), size=(100, 50),
                        pos_hint={'x': 0, 'top': 1})
        self.add_widget(profpic)
        harpia_logo = Image(source="Harpialogo.jpeg", size_hint=(None, None), size=(250, 100),
                            pos_hint={'center_x': 0.5, 'top': 1})
        self.add_widget(harpia_logo)



        self.add_widget(Label(text="Informações do Clima na Rota:", font_size=20, color='green'))
        atual = APIClimaNOW.get_atual("São Paulo")
        info_box = GridLayout(cols=2, padding=[20, 20, 20, 20], size_hint_y=None, height=400)
        info_box.add_widget(Label(text=f"Cidade:", color='green'))
        info_box.add_widget(Label(text=f"{atual['city']}", color='green'))
        info_box.add_widget(Label(text=f"Temperatura:", color='green'))
        info_box.add_widget(Label(text=f"{atual['temperature']:.2f} °C", color='green'))
        info_box.add_widget(Label(text=f"Umidade:", color='green'))
        info_box.add_widget(Label(text=f"{atual['humidity']}%", color='green'))
        info_box.add_widget(Label(text=f"Descrição:", color='green'))
        info_box.add_widget(Label(text=f"{atual['description']}", color='green'))
        info_box.add_widget(Label(text=f"Velocidade do vento:", color='green'))
        info_box.add_widget(Label(text=f"{atual['wind_speed']}", color='green'))
        self.add_widget(info_box)


class RootWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)


        with self.canvas:
            Color(0, 1, 0, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(pos=self.update_rect, size=self.update_rect)

        segunda_tela = SegundaTela(pos_hint={'x': 0, 'y': 0}, size_hint=(1, 1))
        self.add_widget(segunda_tela)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size




