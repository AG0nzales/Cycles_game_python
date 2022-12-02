class Script:

    def __init__(self):

        self._actions = {}
        
    def add_action(self, group, action):

        if not group in self._actions.keys():
            self._actions[group] = []
            
        if not action in self._actions[group]:
            self._actions[group].append(action)

    def get_actions(self, group):

        results = []
        if group in self._actions.keys():
            results = self._actions[group].copy()
        return results
    
    def remove_action(self, group, action):

        if group in self._actions:
            self._actions[group].remove(action)