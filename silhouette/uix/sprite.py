from kivy.clock import Clock
from kivy.graphics.vertex_instructions import Rectangle
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.widget import Widget
from kivy.core.image import Image as CoreImage


class AnimatedSprite(Widget):
    texture = ObjectProperty(None, allownone=True)
    current_col = NumericProperty(0)
    current_row = NumericProperty(0)

    def __init__(self, filename, nb_row, nb_col, width=None, height=None,
                 delay=0.2, row=0, **kwargs):
        super(AnimatedSprite, self).__init__(**kwargs)

        self.image = CoreImage(filename)

        self.nb_row = nb_row
        self.nb_col = nb_col
        self.current_row = row
        self._width = width or (self.image.texture.width/nb_col)
        self._height = height or (self.image.texture.height/nb_row)

        self.bind(texture=self.update)
        self.bind(current_row=self.update_texture)
        self.bind(current_col=self.update_texture)
        self.bind(pos=self.update)
        self.bind(size=self.update)

        Clock.schedule_interval(self.update_current_action, delay)

        with self.canvas.after:
            self.rect = Rectangle(
                texture=self.texture,
                pos=self.pos,
                size=self.size
            )

    def get_region(self, index):
        return self.image.texture.get_region(
            index * self._width, self.current_row*self._height,
            self._width, self._height
        )

    def update_texture(self, *args):
        self.texture = self.get_region(self.current_col)

    def update_current_action(self, dt):
        # update index
        self.current_col += 1
        if self.current_col > self.nb_col-1:
            self.current_col = 0

    def update(self, *args):
        self.rect.texture = self.texture
        self.rect.size = (self._width, self._height)
        self.rect.pos = (
            self.center_x - (self._width/2),
            self.center_y - (self._height/2)
        )