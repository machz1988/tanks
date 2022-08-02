import constants
from game.scripting.action import Action

class HandleKeysPressed(Action):
    """
    An input action that handles the keys pressed

    The responsibility of HandleKeysPressed is to manage the keys pressed

    """
    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service 
        
    def execute(self, cast, script, callback):
        """Executes the handle keys pressed.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # increase shooting power
        if self._keyboard_service.is_key_down('w'):
            if callback.who_plays == constants.ID_TANK1:
                meter = cast.get_first_actor(constants.SHOOTING_POWER_GROUP)
                value = meter.get_value() + 10
                max_value = meter.get_max_value()
                if value <= max_value:
                    meter.update_value(value)
                else:
                    meter.update_value(max_value)
            # elif callback.who_plays == constants.ID_TANK2:
            #     meter = cast.get_actors(constants.SHOOTING_POWER_GROUP)[1]
            #     value = meter.get_value() + 10
            #     max_value = meter.get_max_value()
            #     if value <= max_value:
            #         meter.update_value(value)
            #     else:
            #         meter.update_value(max_value)
        # decrease shooting power
        if self._keyboard_service.is_key_down('s'):
            if callback.who_plays == constants.ID_TANK1:
                meter = cast.get_first_actor(constants.SHOOTING_POWER_GROUP)
                value = meter.get_value() - 10
                min_value = meter.get_min_value()
                if value >= min_value:
                    meter.update_value(value)
                else:
                    meter.update_value(min_value)
            # elif callback.who_plays == constants.ID_TANK2:
            #     meter = cast.get_actors(constants.SHOOTING_POWER_GROUP)[1]
            #     value = meter.get_value() - 10
            #     min_value = meter.get_min_value()
            #     if value >= min_value:
            #         meter.update_value(value)
            #     else:
            #         meter.update_value(min_value)
        # increase projectile power
        if self._keyboard_service.is_key_down('d'):
            if callback.who_plays == constants.ID_TANK1:
                meter = cast.get_first_actor(constants.PROJECTILE_POWER_GROUP)
                value = meter.get_value() + 1
                max_value = meter.get_max_value()
                if value <= max_value:
                    meter.update_value(value)
                else:
                    meter.update_value(max_value)
            # elif callback.who_plays == constants.ID_TANK2:
            #     meter = cast.get_actors(constants.PROJECTILE_POWER_GROUP)[1]
            #     value = meter.get_value() + 1
            #     max_value = meter.get_max_value()
            #     if value <= max_value:
            #         meter.update_value(value)
            #     else:
            #         meter.update_value(max_value)
        # decrease projectile power
        if self._keyboard_service.is_key_down('a'):
            if callback.who_plays == constants.ID_TANK1:
                meter = cast.get_first_actor(constants.PROJECTILE_POWER_GROUP)
                value = meter.get_value() - 1
                min_value = meter.get_min_value()
                if value >= min_value:
                    meter.update_value(value)
                else:
                    meter.update_value(min_value)
            # elif callback.who_plays == constants.ID_TANK2:
            #     meter = cast.get_actors(constants.PROJECTILE_POWER_GROUP)[1]
            #     value = meter.get_value() - 1
            #     min_value = meter.get_min_value()
            #     if value >= min_value:
            #         meter.update_value(value)
            #     else:
            #         meter.update_value(min_value)    