from game.scripting.action import Action

class HandleKeysPressed(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service 
        
    def execute(self, cast, script, callback):
        pass