import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle(Actor):
    
    # A cycle leaving a trail behind it.

    # This class is for it to move itself

    # Attributes:
    #     _segments (list): A list of actors forming the body
    #     _player (string): A string that identifies whether the player is "first" or "second"
    #     _is_dead (bool): Keeps track of the state of the cycle
    

    def __init__(self, player):
        super().__init__()
        self._segments = []
        self._player = player
        self._prepare_body(self._player)
        self._is_dead = False

    def get_player(self):
        return self._player

    def get_segments(self):
        return self._segments

    def get_is_dead(self):
        return self._is_dead

    def set_is_dead(self, is_dead):
        self._is_dead = is_dead

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)

            segment = Actor()

            if self._player == "first":
                segment.set_position(position)
                segment.set_velocity(velocity)
                segment.set_text("#")
                segment.set_color(constants.GREEN)
            else:
                segment.set_position(position)
                segment.set_velocity(velocity)
                segment.set_text("%")
                segment.set_color(constants.RED)

            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)

    def _reset_body(self):
        self._is_dead = False
        self._segments.clear()
        self._prepare_body(self._player)

    def _prepare_body(self, player):

        if player == "first":
            x = int(constants.MAX_X / 4)
            y = int(constants.MAX_Y / 2)
            for i in range(constants.CYCLE_LENGTH):
                position = Point(x, y + i * constants.CELL_SIZE)
                velocity = Point(0, -1 * constants.CELL_SIZE)
                text = "8" if i == 0 else "#"
                color = constants.BROWN if i == 0 else constants.GREEN
                segment = Actor()
                segment.set_position(position)
                segment.set_velocity(velocity)
                segment.set_text(text)
                segment.set_color(color)
                self._segments.append(segment)
        else:
            x = int(constants.MAX_X / 4)*3
            y = int(constants.MAX_Y / 2)
            for i in range(constants.CYCLE_LENGTH):
                position = Point(x, y - i * constants.CELL_SIZE)
                velocity = Point(0, 1 * constants.CELL_SIZE)
                #velocity = (0, 30)
                text = "$" if i == 0 else "%"
                color = constants.YELLOW if i == 0 else constants.RED
                segment = Actor()
                segment.set_position(position)
                segment.set_velocity(velocity)
                segment.set_text(text)
                segment.set_color(color)
                self._segments.append(segment)
