# Menu do ap com 5 botões para ser linkado com o main e a 2a tela.

from kivy.app import App
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

        # Adicionando botões
        button_height = 0.1
        button_padding = 20
        self.add_widget(
            Button(text='<- Voltar', size_hint=(0.15, button_height), color="green", bold=True, background_color=(0, 0, 0, 0), background_normal='',
                   pos_hint={'x': 0.03, 'top': 1}, border=(8, 8, 8, 8), padding=(button_padding, button_padding)))
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
    Harpia().run()












