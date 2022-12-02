import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):


    def __init__(self, keyboard_service):
 
        self._keyboard_service = keyboard_service
        self._first_player_direction = Point(0, -constants.CELL_SIZE)
        self._second_player_direction = Point(0, constants.CELL_SIZE)

    def execute(self, cast, script):

        # Player 1 controls
        p1_key_pressed = False

        # left
        if self._keyboard_service.is_key_down('a'):
            self._first_player_direction = Point(-constants.CELL_SIZE, 0)
            p1_key_pressed = True

        # right
        if self._keyboard_service.is_key_down('d'):
            self._first_player_direction = Point(constants.CELL_SIZE, 0)
            p1_key_pressed = True

        # up
        if self._keyboard_service.is_key_down('w'):
            self._first_player_direction = Point(0, -constants.CELL_SIZE)
            p1_key_pressed = True

        # down
        if self._keyboard_service.is_key_down('s'):
            self._first_player_direction = Point(0, constants.CELL_SIZE)
            p1_key_pressed = True

        # player 2 controls
        p2_key_pressed = False

        # left
        if self._keyboard_service.is_key_down('j'):
            self._second_player_direction = Point(-constants.CELL_SIZE, 0)
            p2_key_pressed = True

        # right
        if self._keyboard_service.is_key_down('l'):
            self._second_player_direction = Point(constants.CELL_SIZE, 0)
            p2_key_pressed = True

        # up
        if self._keyboard_service.is_key_down('i'):
            self._second_player_direction = Point(0, -constants.CELL_SIZE)
            p2_key_pressed = True

        # down
        if self._keyboard_service.is_key_down('k'):
            self._second_player_direction = Point(0, constants.CELL_SIZE)
            p2_key_pressed = True

        # apply directions
        cycles = cast.get_actors("cycles")

        for cycle in cycles:
            # apply first players movement
            if cycle.get_player() == "first":
                if p1_key_pressed:
                    cycle.turn_head(self._first_player_direction)
            # aply second players movement
            if cycle.get_player() == "second":
                if p2_key_pressed:
                    cycle.turn_head(self._second_player_direction)
