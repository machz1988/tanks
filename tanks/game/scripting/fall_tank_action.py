import constants
from game.scripting.action import Action
from game.casting.body import Body
from game.casting.point import Point


class FallTankAction(Action):

    def __init__(self, physics_service):
        self._physics_service = physics_service   
        
    def execute(self, cast, script, callback):
        tanks = cast.get_actors(constants.TANKS_GROUP)
        terrain = cast.get_first_actor(constants.TERRAIN_GROUP)
        surface = terrain.get_surface()
        is_collided = False
        tank = tanks[0]
        body_t = tank.get_body()
        restart_scene = False
        change_scene = False
        for part in surface:
            body_s = Body(part.get_position(), part.get_size())
            if self._physics_service.has_collided_recs(body_s, body_t):
                is_collided = True
                break
        if not is_collided:
            body_t.set_velocity(constants.TANK1_VELOCITY)    
            tank.move_next()
            position = body_t.get_position()
            if position.get_y() >= constants.SCREEN_HEIGHT:
                healths = cast.get_actors(constants.HEALTH_GROUP)
                stats = cast.get_first_actor(constants.STATS_GROUP)
                healths[0].update_value(constants.HEALTH_MIN)
                stats.lose_life()
                #RESTART SCENE
                cast.clear_actors(constants.PROJECTIONS_GROUP)
                restart_scene = True                

        is_collided = False
        tank = tanks[1]
        body_t = tank.get_body()
        for part in surface:
            body_s = Body(part.get_position(), part.get_size())
            if self._physics_service.has_collided_recs(body_s, body_t):
                is_collided = True
                break
        if not is_collided:    
            body_t.set_velocity(constants.TANK2_VELOCITY)    
            tank.move_next()
            position = body_t.get_position()
            if position.get_y() >= constants.SCREEN_HEIGHT:
                healths = cast.get_actors(constants.HEALTH_GROUP)
                stats = cast.get_first_actor(constants.STATS_GROUP)
                healths[1].update_value(constants.HEALTH_MIN)
                #CHANGE SCENE
                stats.add_points(1)
                stats.next_level()
                cast.clear_actors(constants.PROJECTIONS_GROUP)
                change_scene = True
        if change_scene:
            callback.on_next(constants.NEXT_LEVEL)
        if restart_scene:
            callback.on_next(constants.TRY_AGAIN)        
                   
