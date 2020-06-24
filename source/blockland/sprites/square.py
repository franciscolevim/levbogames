from levbogames.levbo_sprite import LevboSprite
from levbogames.environment.resources import Resources
from cocos.euclid import Vector2


class Square(LevboSprite):
    """[summary]

    Args:
        Sprite ([type]): [description]
    """
    # def __init__(self, image, position=(0,0), rotation=0, scale=1, opacity=255, color=(255,255,255), anchor=None, **kwargs):
    def __init__(self, position = (100, 320)):
        """
        [summary]
        """        
        super().__init__(LevboSprite.resources.get_image(file_name = 'green_circle_small.png'))
        self.position = position
        self.scale = 0.5
        self.speed = Vector2(530, 530)