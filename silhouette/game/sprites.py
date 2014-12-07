from kivy.core.image import Image
from silhouette.uix.sprite import AnimatedSprite
from silhouette.utils import data_path


class Cell(AnimatedSprite):
    image = Image(data_path('silou.png'))
    nb_row = 1
    nb_col = 8
    delay = 0.12