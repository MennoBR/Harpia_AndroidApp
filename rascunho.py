# Rascunho / Testes:

'''with info_box.canvas:
    Color(1, 1, 1, 1)
    self.rect = Rectangle(pos=self.pos, size=self.size)
    self.bind(pos=self.update_rect, size=self.update_rect)

def update_rect(self, *args):
    self.rect.pos = self.pos
    self.rect.size = self.size

self.add_widget(info_box)
self.add_widget(Label(text="", size_hint_y=None, height=100))
self.add_widget(Label(text="", size_hint_y=None, height=100))

def on_size(self, *args):
    self.rect.size = self.size
    self.rect.pos = (self.width / 2 - self.rect.size[0] / 2, self.height / 2 - self.rect.size[1] / 2)'''