import constants
from game.scripting.action import Action


class HandleGrowthAction(Action):


    def __init__(self):

        self._timer = 0
        self._wait_time = constants.GROW_TAIL_WAIT

    def execute(self, cast, script):

        cycles = cast.get_actors("cycles")

        if(cycles[0].get_is_dead() == True):


            self._wait_time = constants.GROW_TAIL_WAIT

        else:

            # counter each step
            self._timer += 1

            # when wait time is reached
            if self._timer > self._wait_time:

                # reset counter
                self._timer = 0

                #  growing tails
                for cycle in cycles:
                    cycle.grow_tail(1)

                if self._wait_time > 20:
                    self._wait_time -= 1
