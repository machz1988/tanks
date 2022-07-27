import constants
from game.scripting.action import Action

class DrawProjectilesAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service 
        
    def execute(self, cast, script, callback):
        projectiles = cast.get_actors(constants.PROJECTILES_GROUP)
        for projectile in projectiles:
            image = projectile.get_image()
            body = projectile.get_body()
            position = body.get_position()
            self._video_service.draw_image(image, position)