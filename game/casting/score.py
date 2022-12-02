from game.casting.actor import Actor
from game.shared.point import Point
import constants


class Score(Actor):

    # Score's job is to keep track of how many points the player has earned by eating food. It has methods 
    # for adding and subtracting points. To obtain a string representation of the points earned, the client should use get text().


    def __init__(self, player):
        super().__init__()
        self._points = 0
        self._player = player
        self.add_points(0)
        self.init_position(self._player)

    def get_player(self):
        return self._player

    def init_position(self, player):

        if self._player == "first":
            self.set_position(
                Point(2 * constants.CELL_SIZE, constants.CELL_SIZE))

        if self._player == "second":
            self.set_position(
                Point(constants.MAX_X - 8 * constants.CELL_SIZE, constants.CELL_SIZE))

    def add_points(self, points):

        self._points += points

        # CHECK PLAYER SCORES
        if self._player == "first":
            self.set_text(f"Yellow Score: {self._points}")

        if self._player == "second":
            self.set_text(f"Red Score: {self._points}")
