# Menu do ap com 5 botões para ser linkado com o main e a 2a tela.

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle

class MainMenuScreen(GridLayout):
    def __init__(self, **kwargs):
        super(MainMenuScreen, self).__init__(**kwargs)
        self.cols = 2


        with self.canvas.before:
            Color(0.270, 0.345, 0.227, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.add_widget(Image(source="Harpialogo.jpeg", size_hint=(1, None), height=150))

        # Add buttons
        self.add_widget(Button(text='Button 1', background_color=(0.423, 0.486, 0.305, 1), background_normal=''))
        self.add_widget(Button(text='Button 2', background_color=(0.423, 0.486, 0.305, 1), background_normal=''))
        self.add_widget(Button(text='Button 3', background_color=(0.423, 0.486, 0.305, 1), background_normal=''))
        self.add_widget(Button(text='Button 4', background_color=(0.423, 0.486, 0.305, 1), background_normal=''))
        self.add_widget(Button(text='Button 5', background_color=(0.423, 0.486, 0.305, 1), background_normal=''))

class Harpia(App):
    def build(self):
        return MainMenuScreen()

if __name__ == "__main__":
    Harpia().run()
