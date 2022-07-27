import constants
from game.scripting.action import Action

class DrawTanksAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service 
        
    def execute(self, cast, script, callback):
        tanks = cast.get_actors(constants.TANKS_GROUP)
        tank1 = tanks[0]
        tank2 = tanks[1]
        body_t1 = tank1.get_body()
        image_t1 = tank1.get_image()
        body_t2 = tank2.get_body()
        image_t2 = tank2.get_image()
        pos_t1 = body_t1.get_position()
        pos_t2 = body_t2.get_position()
        self._video_service.draw_image(image_t1, pos_t1)
        self._video_service.draw_image(image_t2, pos_t2)