from game.scripting.action import Action


class DrawActorsAction(Action):

    def __init__(self, video_service):

        self._video_service = video_service

    def execute(self, cast, script):


        # get cycle segments
        cycles = cast.get_actors("cycles")
        segments = []
        for cycle in cycles:
            segments += cycle.get_segments()
        # get score and messages
        score = cast.get_actors("scores")
        messages = cast.get_actors("messages")
        # draw actors
        self._video_service.clear_buffer()
        self._video_service.draw_actors(segments)
        self._video_service.draw_actors(score)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()
