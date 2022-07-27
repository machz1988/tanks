import constants
from game.scripting.action import Action

class MoveProjectilesAction(Action):
  
    def execute(self, cast, script, callback):
        projectiles = cast.get_actors(constants.PROJECTILES_GROUP)
        for projectile in projectiles:
            projectile.move_next()