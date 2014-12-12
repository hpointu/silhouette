from silhouette.game.sprites import Cell
import cymunk as pymunk


class Entity(object):
    """
    Test for 2D entity
    """

    _pos = None

    def __init__(self):
        self.sprite = Cell()
        self.body = pymunk.Body(1, 1666)
        self.shape = pymunk.Poly.create_box(self.body)
        self.pos = (0, 0)
        self.body.position = self.pos

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        self._pos = value
        self.sprite.pos = value

    def move(self, dx, dy):
        self.pos = (self.pos[0]+dx, self.pos[1]+dy)

    def tick(self):
        # update position according to physics body
        self.pos = self.body.position.x, self.body.position.y
