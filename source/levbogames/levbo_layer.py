from cocos.layer import Layer
from pyglet.window import key
from collections import defaultdict


class LevboLayer(Layer):
    """[summary]

    Args:
        Layer ([type]): [description]
    """
    keys_pressed = defaultdict(int)


    def __init__(self):
        super(LevboLayer, self).__init__()


    def on_key_press(self, symbol, _):
        LevboLayer.keys_pressed[symbol] = 1


    def on_key_release(self, symbol, _):
        LevboLayer.keys_pressed[symbol] = 0