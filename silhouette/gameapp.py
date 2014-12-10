from kivy.app import App
from kivy.core.image import Image as CoreImage
from kivy.metrics import dp
from kivy.properties import ObjectProperty, ListProperty, AliasProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from silhouette.game import level
from silhouette.game.sprites import Cell


class MainWindow(BoxLayout):
    pass


class LevelIcon(ButtonBehavior, Label):
    level = ObjectProperty(None)
    icon_image = ObjectProperty(None, allownone=True)

    def __init__(self, **kwargs):
        super(LevelIcon, self).__init__(**kwargs)
        self.icon_image = CoreImage(kwargs.get('icon_texture').icon)

    def get_icon_texture(self):
        return self.icon_image.texture

    def set_icon_texture(self, x):
        pass

    icon_texture = AliasProperty(get_icon_texture, set_icon_texture,
                                 bind=['level', 'icon_image'])


class LevelSelect(BoxLayout):
    available_levels = [
        level.Cellular(),
        level.Cellular(),
        level.Cellular(),
        level.Cellular(),
        level.Cellular(),
        level.Cellular(),
        level.Cellular(),
        level.Cellular()
    ]

    def __init__(self, **kwargs):
        super(LevelSelect, self).__init__(**kwargs)
        self.orientation = 'vertical'
        # setup widgets
        self.grid = GridLayout(cols=4, rows=2,
                               spacing=dp(10), padding=dp(10),
                               size_hint_y=9)


        # add widgets
        self.add_widget(Label(text='Choose your level', font_size=20))
        self.add_widget(self.grid)


        self.populate_levels()

    def populate_levels(self):
        for l in self.available_levels:
            self.grid.add_widget(LevelIcon(level=l))


class GameApp(App):
    def build(self):
        return LevelSelect()
