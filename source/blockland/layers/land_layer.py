from blockland.sprites.square import Square
from levbogames.levbo_layer import LevboLayer
from levbogames.levbo_sprite import LevboSprite
from levbogames.environment.paths import levbopaths
from cocos.euclid import Vector2
from pyglet.window import key


class LandLayer(LevboLayer):
    """
    [summary]

    Args:
        LevboLayer ([type]): [description]
    """
    is_event_handler = True


    def __init__(self):
        super().__init__()
        LevboSprite.resources.append_sprites_path(path = levbopaths.RESOURCES_PATH, directory = 'blockland/sprites')
        self.__square = Square()
        self.add(self.__square)
        self.schedule(self.update)


    def update(self, delta_t):
        """
        [summary]

        Args:
            delta_t ([type]): [description]
        """
        mov_x = LevboLayer.keys_pressed[key.RIGHT] - LevboLayer.keys_pressed[key.LEFT]
        mov_y = LevboLayer.keys_pressed[key.UP] - LevboLayer.keys_pressed[key.DOWN]                
        if mov_x != 0 or mov_y != 0:
            movement = Vector2(mov_x * delta_t, mov_y * delta_t)
            self.__square.move(movement)