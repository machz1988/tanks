import math
import constants
from game.casting.body import Body
from game.casting.image import Image
from game.casting.point import Point
from game.casting.projectile import Projectile
from game.scripting.action import Action

class HandleMousePressed(Action):

    def __init__(self, mouse_service):
        self._mouse_service = mouse_service 
        
    def execute(self, cast, script, callback):
        if self._mouse_service.is_button_pressed("left"):
            position_c = self._mouse_service.get_coordinates()
            xc = position_c.get_x()
            yc = position_c.get_y()
            tank1 = cast.get_first_actor(constants.TANKS_GROUP)
            body_t = tank1.get_body()
            position_t = body_t.get_position()
            size_t = body_t.get_size()
            size = constants.PROJECTILE_SIZE
            xp = position_t.get_x() + int(size_t.get_x()/2)
            yp = position_t.get_y() - int(size_t.get_y()/2)
            position = Point(xp,yp)
            h = math.sqrt(math.pow(yc - yp, 2) + math.pow(xc - xp, 2))
            theta = int(math.asin((yc - yp) / h) * 180 / math.pi)
            if xc > xp:
                theta = - theta
            else:
                theta = 180 + theta
            image = Image(constants.PROJECTILE_IMAGE, constants.PROJECTILE_SCALE, constants.PROJECTILE_ROTATION)
            body = Body(position, size)
            projectile = Projectile(image,body,constants.PROJECTILE_EXAMPLE_V0, theta)
            cast.add_actor(constants.PROJECTILES_GROUP, projectile)