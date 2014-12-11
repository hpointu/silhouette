from kivy.core.image import Image
from silhouette.uix.sprite import AnimatedSprite
from silhouette.utils import data_path


class Cell(AnimatedSprite):
    def __init__(self):
        sprite_sheet = Image(data_path('circle-02.png')).texture
        super(Cell, self).__init__(
            sprite_sheet,
            nb_row=1,
            nb_col=9,
            delay=0.12
        )