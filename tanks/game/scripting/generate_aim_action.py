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
        if callback.who_plays == constants.ID_TANK1:
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
            if xp < xc and yp > yc:
                theta = 360 + theta
            elif xp > xc and yp > yc:
                theta = 180 - theta
            elif xp > xc and yp < yc:
                theta = 180 - theta
            else:
                theta = theta
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
        # if callback.who_plays == constants.ID_TANK2:
        #     position_c = self._mouse_service.get_coordinates()
        #     xc = position_c.get_x()
        #     yc = position_c.get_y()
        #     tank2 = cast.get_actors(constants.TANKS_GROUP)[1]
        #     body_t = tank2.get_body()
        #     position_t = body_t.get_position()
        #     size_t = body_t.get_size()
        #     xp = position_t.get_x() + int(size_t.get_x()/2)
        #     yp = position_t.get_y() - int(size_t.get_y()/2)
        #     center = Point(xp,yp)
        #     radius = constants.PROJECTION_RADIUS
        #     h = math.sqrt(math.pow(yc - yp, 2) + math.pow(xc - xp, 2))
        #     theta = int(math.asin((yc - yp) / h) * 180 / math.pi)
        #     if xp < xc and yp > yc:
        #         theta = 360 + theta
        #     elif xp > xc and yp > yc:
        #         theta = 180 - theta
        #     elif xp > xc and yp < yc:
        #         theta = 180 - theta
        #     else:
        #         theta = theta
        #     image = Image(constants.PROJECTILE_IMAGE, constants.PROJECTILE_SCALE, constants.PROJECTILE_ROTATION)
        #     circle = Circle(center, constants.PROJECTION_RADIUS, constants.WHITE)
        #     shooting_power = cast.get_actors(constants.SHOOTING_POWER_GROUP)[1]
        #     projectile_power = cast.get_actors(constants.PROJECTILE_POWER_GROUP)[1]
        #     v0 = shooting_power.get_value()
        #     power = projectile_power.get_value()    
        #     projectile = Projectile(image, circle, v0, theta, power)
        #     time_rate = constants.TIME_RATE
        #     radius = constants.PROJECTION_RADIUS
        #     color = constants.PROJECTION_COLOR
        #     #projection = Circle(position, radius, color)
        #     #cast.add_actor(constants.PROJECTIONS_GROUP, projection)            
        #     for i in range(constants.PROJECTIONS_NUMBER):
        #         new_pos = projectile.calculate_projection_position(time_rate*i)
        #         x = new_pos.get_x()
        #         y = new_pos.get_y()
        #         projection = Circle(Point(x, y), radius, color)
        #         cast.add_actor(constants.PROJECTIONS_GROUP, projection)