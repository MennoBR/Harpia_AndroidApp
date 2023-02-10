
import APIClimaNOW
import Aviator2ndTela
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.clock import Clock


class Harpia(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {'center_x':0.5, "center_y":0.5}


        with self.window.canvas.before:
             Color(0.960784, 0.921569, 0.803922)
             self.rect = Rectangle(size=Window.size, pos=self.window.pos)


        self.window.add_widget(Image(source="Harpialogo.jpeg"))
        self.greeting = Label(text="Quem é você?", font_size = 18, color='green')
        self.window.add_widget(self.greeting)
        self.user = TextInput(multiline=False, padding_y=(20, 20), size_hint=(1, 0.5),
                              background_color='white')
        self.window.add_widget(self.user)
        self.button = Button(text='ENTRAR', size_hint=(1, 0.5), bold=True,
                             background_color='green', background_normal='',)
        self.button.bind(on_press=self.pressiona)
        self.window.add_widget(self.button)

        return self.window

    def pressiona(self, evento):
        self.greeting.text = "Olá Comandante " + self.user.text + '!'

        Clock.schedule_once(self.mostre_segunda, 2)

    def mostre_segunda(self, dt):
        self.window.clear_widgets()
        self.window.add_widget(Aviator2ndTela.SegundaTela())



if __name__ == "__main__":
    Harpia().run()