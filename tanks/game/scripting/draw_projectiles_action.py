import constants
from game.casting.point import Point
from game.scripting.action import Action

class DrawProjectilesAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service 
        
    def execute(self, cast, script, callback):
        projectiles = cast.get_actors(constants.PROJECTILES_GROUP)
        for projectile in projectiles:
            image = projectile.get_image()
            circle = projectile.get_circle()
            center = circle.get_center()
            radius = circle.get_radius()
            x = center.get_x() - radius
            y = center.get_y() - radius
            position = Point(x, y)
            self._video_service.draw_image(image, position)