import os
from kivy.app import App
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.properties import ListProperty, ReferenceListProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.utils import get_color_from_hex
from silhouette.uix.sprite import AnimatedSprite
from kivy.uix.colorpicker import ColorPicker

class Window(BoxLayout):
    pass
    # def __init__(self, **kwargs):
    #     super(Window, self).__init__(**kwargs)
    #
    #     self.orientation = 'vertical'
    #
    #     self.add_widget(
    #         AnimatedSprite(
    #             'silhouette/data/silou.png',
    #             nb_col=8, nb_row=1,
    #             delay=.1
    #         )
    #     )
    #
    #     with self.canvas.before:
    #         Color(1, 1, 1)
    #         self.bg = Rectangle(pos=self.pos, size=self.size)
    #
    #     self.bind(size=self.update_draw)
    #     self.bind(pos=self.update_draw)
    #
    # def update_draw(self, *args):
    #     self.bg.size = self.size
    #     self.bg.pos = self.pos


class SelectorScreen(Screen):
    bg_color = ListProperty([])


class MyFileChooser(FileChooserIconView):
    def __init__(self, **kwargs):
        super(MyFileChooser, self).__init__(**kwargs)
        _root = os.path.dirname(os.path.dirname(__file__))
        self.rootpath = os.path.join(_root, 'silhouette', 'data')


class LoadImageScreen(Screen):
    def on_submit(self):
        # dirty text change
        self.manager.get_screen(
            'selector'
        ).ids.image_filename.text = str(self.ids.filename.selection[0])
        self.manager.current = 'selector'


class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)

    def show_view(self):
        sv = self.get_screen('view')
        ss = self.get_screen('selector')
        sc = self.get_screen('color')

        sv.init_view(
            ss.ids.image_filename.text,
            nb_col=ss.ids.nb_col.value, nb_row=ss.ids.nb_row.value,
            delay=ss.ids.delay.value, bg_color=ss.bg_color
        )

        self.current = 'view'


class ViewScreen(Screen):
    bg_color = ListProperty(None)

    def init_view(self, filename, nb_row, nb_col, delay, bg_color):
        # self.bg_color = get_color_from_hex(bg_color)
        self.bg_color = bg_color

        self.ids.layout.clear_widgets()
        self.ids.layout.add_widget(
            AnimatedSprite(
                filename,
                nb_col=nb_col, nb_row=nb_row,
                delay=delay
            )
        )
        b = Button(size_hint_y=.2, text='return')
        self.ids.layout.add_widget(b)
        b.bind(on_press=self.return_to_home)

    def return_to_home(self, *args):
        self.manager.current = 'selector'


class ColorScreen(Screen):
    def on_submit(self):
        self.manager.get_screen(
            'selector'
        ).bg_color = self.ids.bg_color.color
        self.manager.current = 'selector'


class SpriteViewerApp(App):
    def build(self):
        sm = MyScreenManager()
        sm.add_widget(SelectorScreen(name='selector'))
        sm.add_widget(LoadImageScreen(name='load_image'))
        sm.add_widget(ViewScreen(name='view'))
        sm.add_widget(ColorScreen(name='color'))
        return sm


if __name__ == "__main__":
    SpriteViewerApp().run()