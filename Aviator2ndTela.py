
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class SegundaTela(GridLayout):
    def __init__(self, **kwargs):
        super(SegundaTela, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text="Informações do Clima:"))