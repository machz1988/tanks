import constants
from game.casting.circle import Circle
from game.scripting.action import Action

class CollideTerrainAction(Action):
    """
    An update action that checks the collision between the projectile and the terrain

    The responsibility of CollideTerrainAction is to check the collisions between the projectile and the terrain.
    """
    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        """Executes the projectile collide terrain action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        projectiles = cast.get_actors(constants.PROJECTILES_GROUP)
        terrain = cast.get_first_actor(constants.TERRAIN_GROUP)
        remove_projectile = False
        for projectile in projectiles:
            circle = projectile.get_circle()
            surface = terrain.get_surface()
            # checking if the projectile collides with the terrain
            for rectangle in surface:
                if self._physics_service.has_collided_circle_rec(rectangle, circle):
                    #sound = Sound(constants.HIT_TERRAIN)
                    #scene_manager.AUDIO_SERVICE.play_sound(sound)
                    surface.remove(rectangle)
                    remove_projectile = True
                    break        
            if remove_projectile:
                power = projectile.get_power()
                if power > constants.CELL_SIZE:
                    # removing terrain according the projectile's power
                    for rectangle in surface:
                        center = circle.get_center()
                        radius = int(power / 2)
                        new_circle = Circle(center, radius, constants.WHITE)
                        if self._physics_service.has_collided_circle_rec(rectangle, new_circle):
                            surface.remove(rectangle)    
                cast.remove_actor(constants.PROJECTILES_GROUP, projectile)
                remove_projectile = False