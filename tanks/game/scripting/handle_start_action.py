from game.scripting.action import Action

class HandleStartAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service 
        
    def execute(self, cast, script, callback):
        pass