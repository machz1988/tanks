from hashlib import new
import math
import constants
from game.casting.circle import Circle
from game.casting.point import Point
from game.casting.image import Image
from game.casting.body import Body
from game.casting.projectile import Projectile
from game.scripting.action import Action

class GenerateAimAction(Action):

    def __init__(self, mouse_service):
        self._mouse_service = mouse_service 
        
    def execute(self, cast, script, callback):
        cast.clear_actors(constants.PROJECTIONS_GROUP)
        position_c = self._mouse_service.get_coordinates()
        xc = position_c.get_x()
        yc = position_c.get_y()
        tank1 = cast.get_first_actor(constants.TANKS_GROUP)
        body_t = tank1.get_body()
        position_t = body_t.get_position()
        size_t = body_t.get_size()
        xp = position_t.get_x() + int(size_t.get_x()/2)
        yp = position_t.get_y() - int(size_t.get_y()/2)
        center = Point(xp,yp)
        radius = constants.PROJECTION_RADIUS
        h = math.sqrt(math.pow(yc - yp, 2) + math.pow(xc - xp, 2))
        theta = int(math.asin((yc - yp) / h) * 180 / math.pi)
        if xc > xp:
            theta = - theta
        else:
            theta = 180 + theta
        image = Image(constants.PROJECTILE_IMAGE, constants.PROJECTILE_SCALE, constants.PROJECTILE_ROTATION)
        circle = Circle(center, constants.PROJECTION_RADIUS, constants.WHITE)
        shooting_power = cast.get_first_actor(constants.SHOOTING_POWER_GROUP)
        projectile_power = cast.get_first_actor(constants.PROJECTILE_POWER_GROUP)
        v0 = shooting_power.get_value()
        power = projectile_power.get_value()    
        projectile = Projectile(image, circle, v0, theta, power)
        time_rate = constants.TIME_RATE
        radius = constants.PROJECTION_RADIUS
        color = constants.PROJECTION_COLOR
        #projection = Circle(position, radius, color)
        #cast.add_actor(constants.PROJECTIONS_GROUP, projection)            
        for i in range(constants.PROJECTIONS_NUMBER):
            new_pos = projectile.calculate_projection_position(time_rate*i)
            x = new_pos.get_x()
            y = new_pos.get_y()
            projection = Circle(Point(x, y), radius, color)
            cast.add_actor(constants.PROJECTIONS_GROUP, projection)