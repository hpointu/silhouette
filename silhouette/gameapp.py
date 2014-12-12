import cymunk as pymunk
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from silhouette.game.entity import Entity

FRAME_RATE = 1.0/50.0


class MainWindow(BoxLayout):
    pass


class GameTest(Widget):
    def __init__(self, **kwargs):
        super(GameTest, self).__init__(**kwargs)

        self.entity = Entity()
        self.space = pymunk.Space()
        self.init_scene()

        Clock.schedule_interval(self.update, FRAME_RATE)

    def init_scene(self):

        self.space.gravity = 0, -10

        self.entity.pos = (10, 10)
        self.add_widget(self.entity.sprite)

        self.space.add(self.entity.body, self.entity.shape)

    def update(self, dt):
        """
        Uptade state of the game
        """
        speed_factor = dt/FRAME_RATE

        self.space.step(dt)

        # update entity
        self.entity.tick()


class GameApp(App):
    def build(self):
        return GameTest()
