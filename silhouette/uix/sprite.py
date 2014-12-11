from kivy.clock import Clock
from kivy.graphics.vertex_instructions import Rectangle
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.widget import Widget
from kivy.core.image import Image as CoreImage


class AnimatedSprite(Widget):
    texture = ObjectProperty(None, allownone=True)
    current_col = NumericProperty(0)
    current_row = NumericProperty(0)

    def __init__(self, sprite_sheet, nb_row, nb_col,
                 row=0, delay=0.2,
                 width=None, height=None,
                 **kwargs):
        super(AnimatedSprite, self).__init__(**kwargs)

        self.sprite_sheet = sprite_sheet

        self.delay = delay
        self.nb_row = nb_row
        self.nb_col = nb_col
        self.current_row = row
        self.width = width or (self.sprite_sheet.width/self.nb_col)
        self.height = height or (self.sprite_sheet.height/self.nb_row)

        self.bind(texture=self.update)
        self.bind(current_row=self.update_texture)
        self.bind(current_col=self.update_texture)
        self.bind(pos=self.update)
        self.bind(size=self.update)

        Clock.schedule_interval(self.update_current_action, self.delay)

        with self.canvas.after:
            self.rect = Rectangle(
                texture=self.texture,
                pos=self.pos,
                size=self.size
            )

        self.update_texture()

    def get_region(self, index):
        return self.sprite_sheet.get_region(
            index * self.width, self.current_row*self.height,
            self.width, self.height
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
        self.rect.size = (self.width, self.height)
        self.rect.pos = (
            self.center_x - (self.width/2),
            self.center_y - (self.height/2)
        )