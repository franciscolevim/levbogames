from levbogames.environment.resources import Resources
from cocos.sprite import Sprite
from cocos.euclid import Vector2


class LevboSprite(Sprite):
    """[summary]

    Args:
        Sprite ([type]): [description]
    """
    resources = Resources()


    def __init__(self, image, position = (0,0), rotation = 0, scale = 1, opacity = 255, color = (255,255,255), 
                anchor = None, **kwargs):
        """
        [summary]

        Args:
            image ([type]): [description]
            position (tuple, optional): [description]. Defaults to (0,0).
            rotation (int, optional): [description]. Defaults to 0.
            scale (int, optional): [description]. Defaults to 1.
            opacity (int, optional): [description]. Defaults to 255.
            color (tuple, optional): [description]. Defaults to (255,255,255).
            anchor ([type], optional): [description]. Defaults to None.
        """
        super().__init__(image, position = position, rotation = rotation, scale = scale, opacity = opacity, 
                        color = color, anchor=anchor, **kwargs)
        self.speed = Vector2(0, 0)        


    def move(self, offset:Vector2):
        """
        [summary]

        Args:
            offset ([type]): [description]
        """
        mov_x = self.position[0] + offset.x * self.speed.x
        mov_y = self.position[1] + offset.y * self.speed.y 
        self.position = Vector2(mov_x, mov_y)

