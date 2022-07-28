import constants
from game.scripting.action import Action

class CollideTankAction(Action):
    """
    An update action that handles the collision of the projectiles with the tanks

    The responsibility of CollideTankAction is to handle the collision of the projectiles with the tanks
    """

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        """Executes the projectile collide tank action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        healths = cast.get_actors(constants.HEALTH_GROUP)
        stats = cast.get_first_actor(constants.STATS_GROUP)
        tanks = cast.get_actors(constants.TANKS_GROUP)
        projectiles = cast.get_actors(constants.PROJECTILES_GROUP)
        change_scene = False
        restart_scene = False
        for projectile in projectiles:
            circle = projectile.get_circle()
            destroy_projectile = False
            for tank in tanks:
                rect = tank.get_body().get_rectangle()
                if self._physics_service.has_collided_circle_rec(rect, circle):
                    #sound = Sound(constants.HIT_TANK)
                    #scene_manager.AUDIO_SERVICE.play_sound(sound)
                    if tank == tanks[0]:
                        value = healths[0].get_value()
                        value -= projectile.get_power()
                        healths[0].update_value(value)
                        if value <= 0:
                            #self._winner = constants.ID_PLAYER2
                            stats.lose_life()
                            healths[0].update_value(0)
                            #RESTART SCENE
                            restart_scene = True
                    else:
                        value = healths[1].get_value()
                        value -= projectile.get_power()
                        healths[1].update_value(value)
                        if value <= 0:
                            #self._winner = constants.ID_PLAYER1
                            healths[1].update_value(0)
                            #CHANGE SCENE
                            stats.add_points(1)
                            stats.next_level()
                            change_scene = True
                    destroy_projectile = True
                    break
            if destroy_projectile:
                cast.remove_actor(constants.PROJECTILES_GROUP, projectile)
            if change_scene or restart_scene:
                break
        if change_scene:
            callback.on_next(constants.NEXT_LEVEL)
        if restart_scene:
            callback.on_next(constants.TRY_AGAIN)