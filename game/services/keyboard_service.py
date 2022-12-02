import pyray
from game.shared.point import Point


class KeyboardService:
# THIS CLASS WILL DETECT PLAYER INPUTS

    def __init__(self):
        # THE CONSTRUCTOR USING PYRAY
        self._keys = {}

        self._keys['w'] = pyray.KEY_W
        self._keys['a'] = pyray.KEY_A
        self._keys['s'] = pyray.KEY_S
        self._keys['d'] = pyray.KEY_D

        self._keys['i'] = pyray.KEY_I
        self._keys['j'] = pyray.KEY_J
        self._keys['k'] = pyray.KEY_K
        self._keys['l'] = pyray.KEY_L

        self._keys['y'] = pyray.KEY_Y

    def is_key_up(self, key):

        pyray_key = self._keys[key.lower()]
        return pyray.is_key_up(pyray_key)

    def is_key_down(self, key):

        pyray_key = self._keys[key.lower()]
        return pyray.is_key_down(pyray_key)
