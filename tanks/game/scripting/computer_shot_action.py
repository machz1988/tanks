import math
import random
import constants
from game.casting.circle import Circle
from game.casting.image import Image
from game.casting.point import Point
from game.casting.projectile import Projectile
from game.scripting.action import Action

class ComputerShotAction(Action):

    def __init__(self, attepmts, dead_shots, v0, theta, power):
        self._attempts = attepmts
        self._v0 = v0
        self._theta = theta
        self._dead_shots = dead_shots
        self._attempt  = 0
        self._power = power
        
    def execute(self, cast, script, callback):
        if callback.who_plays == constants.ID_TANK2:
            tanks = cast.get_actors(constants.TANKS_GROUP)
            # calculating v0 and power
            if self._attempt < self._attempts:
                shooting_power = cast.get_actors(constants.SHOOTING_POWER_GROUP)[1]
                min_value_sp = shooting_power.get_min_value()
                max_value_sp = shooting_power.get_max_value()
                v0 = random.randint(min_value_sp, max_value_sp)
                shooting_power.update_value(v0)

                projectile_power = cast.get_actors(constants.PROJECTILE_POWER_GROUP)[1]
                min_value_pp = projectile_power.get_min_value()
                max_value_pp = projectile_power.get_max_value()
                power = random.randint(min_value_pp, max_value_pp)
                projectile_power.update_value(power)
                self._attempt += 1
            else:
                v0 = self._v0
                power = self._power
            # Getting tank2's position
            tank2 = tanks[1]
            body_t2 = tank2.get_body()
            position_t2 = body_t2.get_position()
            size_t2 = body_t2.get_size()
            xt2 = position_t2.get_x() + int(size_t2.get_x()/2)
            yt2 = position_t2.get_y() - int(size_t2.get_y()/2)
            # Calculating theta
            theta = self._theta
            # creating projectile
            center = Point(xt2,yt2)
            radius = constants.PROJECTILE_RADIUS
            image = Image(constants.PROJECTILE_IMAGE, constants.PROJECTILE_SCALE, constants.PROJECTILE_ROTATION)
            circle = Circle(center, radius, constants.WHITE)
            projectile = Projectile(image, circle, v0, theta, power)
            cast.add_actor(constants.PROJECTILES_GROUP, projectile)
            callback.who_plays = constants.ID_TANK1

    #def _optimize_theta(self, theta, step):
