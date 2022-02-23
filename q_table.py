
class QTable:
    def __init__(self):
        # use (x, y , Action) as the key to query the utility?
        self.table = {}

    def is_terminal_state(self):
        # given coordinate, return true is that state is a terminal state
        pass

    def initialize_table(self):
        pass

    def update_utility(self):
        pass

    def get_action_highest_utility(self):
        # given current location, find next action with the highest utility
        pass
