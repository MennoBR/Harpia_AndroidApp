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
            Image(source="Harpialogo.jpeg", size_hint=(None, None), size=(100, 50), pos_hint={'x': 0.01, 'top': 0.95}))

        # Adicionando butões
        self.add_widget(
            Button(text='Selecionar Rota', size_hint=(0.4, 0.1), bold=True, background_color="green", background_normal='',
                   pos_hint={'center_x': 0.5, 'center_y': 0.6}))
        self.add_widget(
            Button(text='Informações da Aeronave', size_hint=(0.4, 0.1), bold=True, background_color="green", background_normal='',
                   pos_hint={'center_x': 0.5, 'center_y': 0.5}))
        self.add_widget(
            Button(text='Aeroportos', size_hint=(0.4, 0.1), bold=True, background_color="green", background_normal='',
                   pos_hint={'center_x': 0.5, 'center_y': 0.4}))
        self.add_widget(
            Button(text='Configurações', size_hint=(0.4, 0.1), bold=True, background_color="green", background_normal='',
                   pos_hint={'center_x': 0.5, 'center_y': 0.3}))
        self.add_widget(
            Button(text='Minha Conta', size_hint=(0.4, 0.1), bold=True, background_color="green", background_normal='',
                   pos_hint={'center_x': 0.5, 'center_y': 0.2}))

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class Harpia(App):
    def build(self):
        return MainMenuScreen()


if __name__ == "__main__":
    Harpia().run()



'''from kivy.app import App
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle

# Travando a janela:
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')

#definindo a função:

class MainMenuScreen(FloatLayout):
    def __init__(self, **kwargs):
        super(MainMenuScreen, self).__init__(**kwargs)

        with self.canvas.before:
            Color(1, 0.980, 0.941, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)

        #Manipulando logo
        self.add_widget(Image(source="Harpialogo.jpeg", size_hint=(None, None), size=(100, 50), pos_hint={'x': 0.01, 'top': 0.95} ))

        # Adicionando butões
        self.add_widget(Button(text='Button 1', size_hint=(0.4, 0.1), bold=True, background_color="green", background_normal='', pos_hint={'center_x': 0.5, 'center_y': 0.6}))
        self.add_widget(Button(text='Button 2', size_hint=(0.4, 0.1), bold=True, background_color="green", background_normal='', pos_hint={'center_x': 0.5, 'center_y': 0.5}))
        self.add_widget(Button(text='Button 3', size_hint=(0.4, 0.1), bold=True, background_color="green", background_normal='', pos_hint={'center_x': 0.5, 'center_y': 0.4}))
        self.add_widget(Button(text='Button 4', size_hint=(0.4, 0.1), bold=True, background_color="green", background_normal='', pos_hint={'center_x': 0.5, 'center_y': 0.3}))
        self.add_widget(Button(text='Button 5', size_hint=(0.4, 0.1), bold=True, background_color="green", background_normal='', pos_hint={'center_x': 0.5, 'center_y': 0.2}))

class Harpia(App):
    def build(self):
        return MainMenuScreen()

if __name__ == "__main__":
    Harpia().run()'''