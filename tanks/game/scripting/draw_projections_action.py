import constants
from game.scripting.action import Action

class DrawProjectionsAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service 
        
    def execute(self, cast, script, callback):
        projections = cast.get_actors(constants.PROJECTIONS_GROUP)
        for projection in projections:
            center = projection.get_center()
            radius = projection.get_radius()
            color = projection.get_color()
            self._video_service.draw_circle(center, radius, color)