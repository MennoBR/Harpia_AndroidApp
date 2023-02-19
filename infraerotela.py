#Tela para mostrar ao usuário informações dos aeroportos.

from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.config import Config


# Travando a janela:
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')

#Começando build:
class infrap(FloatLayout):

    def __init__(self, **kwargs):
        super(infrap, self).__init__(**kwargs)

        with self.canvas.before:
            Color(0.960784, 0.921569, 0.803922)
            self.rect = Rectangle(size=self.size)
            self.bind(size=self._update_rect)

        #Add e maniplando as imagens:
        self.add_widget(
                Image(source="Harpialogo.jpeg", size_hint=(None, None), size=(150, 75),
                      pos_hint={'x': 0.32, 'top': 0.95}))
        self.add_widget(
            Image(source="infraero1.png", size_hint=(None, None), size=(300, 150),
                  pos_hint={'center': 1, 'top': 0}))



if __name__ == "__main__":
    infrap().run()
