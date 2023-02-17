# Rascunho / Testes:

#Rascunho do menu funcional com os botões:
'''from kivy.app import App
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle

# Travando a janela:
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')


# definindo a função:
class MainMenuScreen(FloatLayout):
    def __init__(self, **kwargs):
        super(MainMenuScreen, self).__init__(**kwargs)

        with self.canvas.before:
            Color(1, 0.980, 0.941, 1)
            self.rect = Rectangle(size=self.size)
            self.bind(size=self._update_rect)

        # Manipulando logo
        self.add_widget(
            Image(source="Harpialogo.jpeg", size_hint=(None, None), size=(150, 75), pos_hint={'x': 0.32, 'top': 0.95}))

        # Adicionando butões
        button_height = 0.1
        button_padding = 20
        self.add_widget(
            Button(text='Selecionar Rota', size_hint=(0.4, button_height), bold=True, background_color="green",
                   background_normal='', pos_hint={'center_x': 0.5, 'center_y': 0.6},
                   border=(10, 10, 10, 10), padding=(button_padding, button_padding)))
        self.add_widget(
            Button(text='Ver Mapa', size_hint=(0.4, button_height), bold=True, background_color="green",
                   background_normal='', pos_hint={'center_x': 0.5, 'center_y': 0.5},
                   border=(10, 10, 10, 10), padding=(button_padding, button_padding)))
        self.add_widget(
            Button(text='Aeroportos', size_hint=(0.4, button_height), bold=True, background_color="green",
                   background_normal='', pos_hint={'center_x': 0.5, 'center_y': 0.4},
                   border=(10, 10, 10, 10), padding=(button_padding, button_padding)))
        self.add_widget(
            Button(text='Configurações', size_hint=(0.4, button_height), bold=True, background_color="green",
                   background_normal='', pos_hint={'center_x': 0.5, 'center_y': 0.3},
                   border=(10, 10, 10, 10), padding=(button_padding, button_padding)))
        self.add_widget(
            Button(text='Minha Conta', size_hint=(0.4, button_height), bold=True, background_color="green",
                   background_normal='', pos_hint={'center_x': 0.5, 'center_y': 0.2},
                   border=(10, 10, 10, 10), padding=(button_padding, button_padding)))

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class Harpia(App):
    def build(self):
        return MainMenuScreen()


if __name__ == "__main__":
    Harpia().run()'''


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