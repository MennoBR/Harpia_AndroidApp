#Tela para mostrar ao usuário informações dos aeroportos da API apinfraero.py

from kivy.app import App
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button
from kivy.uix.label import Label


# Configurando a janela:
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')


class MainMenuScreen(FloatLayout):
    def __init__(self, **kwargs):
        super(MainMenuScreen, self).__init__(**kwargs)

        with self.canvas.before:
            Color(0.960784, 0.921569, 0.803922)
            self.rect = Rectangle(size=self.size)
            self.bind(size=self._update_rect)

        # Adicionando o logo e a imagem
        self.add_widget(
            Image(source="Harpialogo.jpeg", size_hint=(None, None), size=(200, 100), pos_hint={'x': 0.25, 'top': 0.9}))
        self.add_widget(
            Image(source="fotobranca.jpg", size_hint=(None, None), size=(90, 40), pos_hint={'x': 0.79, 'top': 1}))
        self.add_widget(Image(source="infraero1.png", size_hint_y=None, height=200, pos_hint={'x': 0, 'top': 0.6}))

        button_height = 0.07
        button_padding = 10
        self.add_widget(
            Button(text='Voltar', size_hint=(0.3, button_height), bold=True, background_color="green",
                   background_normal='', pos_hint={'x': 0.35, 'y': 0.15},
                   border=(9, 9, 9, 9), padding=(button_padding, button_padding)))

        self.add_widget(Label(text='Selecione o Aeroporto e espere carregar:', font_size='18sp', color='green',
                              pos_hint={'x': 0, 'y': 0.15}, font_name='Roboto-Bold.ttf'))


    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class Harpia(App):
    def build(self):
        return MainMenuScreen()


if __name__ == "__main__":
    Harpia().run()
















