import constants
from models.sprites import Sprite

class Border():
    def __init__(self) -> None:
        pass

    def create(self, height, width, color, pos_x, pos_y):
        border = Sprite(color, height, width)
        border.rect.x = pos_x
        border.rect.y = pos_y

        return border