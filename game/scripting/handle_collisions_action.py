import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point


class HandleCollisionsAction(Action):


    def __init__(self, keyboard_service):


        self._keyboard_service = keyboard_service

        self._is_game_over = False
        self._who_won = ""

    def execute(self, cast, script):
 
        if not self._is_game_over:
            self._handle_cycles_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)
        else:
            if self._keyboard_service.is_key_down('y'):
                # reset game over variable
                self._is_game_over = False
                # remove game over message
                cast.remove_actor("messages", cast.get_first_actor("messages"))
                # reset cycle bodies
                cycles = cast.get_actors("cycles")
                for cycle in cycles:
                    cycle._reset_body()

    def _return_player_color(self, value, reverse=False):

        color_list = ["Yellow", "Red"]
        if value == "first":
            color = 0
        else:
            color = 1
        if reverse:
            color = 1 - color
        return color_list[color]

    def _handle_cycles_collision(self, cast):

        cycles = cast.get_actors("cycles")

        # for every cycle
        for cycle in cycles:
            head = cycle.get_segments()[0]
            # loop through every other cycle
            for other in cycles:
                # make sure its not ourselves
                if other != cycle:
                    for segment in other.get_segments():
                        # for every segment in this other cycle
                        if head.get_position().equals(segment.get_position()):
                            # if head collides with any, game over
                            self._is_game_over = True
                            # assign winner to the other player
                            self._who_won = self._return_player_color(
                                other.get_player())

    def _handle_segment_collision(self, cast):

        cycles = cast.get_actors("cycles")
        for cycle in cycles:
            head = cycle.get_segments()[0]
            segments = cycle.get_segments()[1:]
            # check each cycles head against it's own segments
            for segment in segments:
                if head.get_position().equals(segment.get_position()):
                    # if cycle hit itself, the other player wins
                    self._who_won = self._return_player_color(
                        cycle.get_player(), True)
                    # end game
                    self._is_game_over = True

    def _handle_game_over(self, cast):

        if self._is_game_over:

            # get reference to cycles
            cycles = cast.get_actors("cycles")

            # find a position in the center of the screen
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)
            # create a game over message there
            message = Actor()
            message.set_text(
                f"Game Over!\n {self._who_won.capitalize()} player won the game.\n\n Press 'Y' to play again! ")
            message.set_position(position)
            cast.add_actor("messages", message)

            # turn all segments of all cycles white
            for cycle in cycles:
                # set cycle is dead to true
                cycle.set_is_dead(True)
                segments = cycle.get_segments()
                for index, segment in enumerate(segments):
                    # leave one colored spot to identify which is which
                    if index != 1:
                        segment.set_color(constants.WHITE)

            # add point to correct score
            scores = cast.get_actors("scores")
            for score in scores:
                if self._who_won == "Green" and score.get_player() == "first":
                    score.add_points(1)
                if self._who_won == "Red" and score.get_player() == "second":
                    score.add_points(1)
