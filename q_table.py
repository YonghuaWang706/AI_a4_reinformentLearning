from agent import Action


class QTable:
    def __init__(self, file_name):
        self.q_table = {{}}
        self.input_file_name = file_name
        # use (x, y , Action) as the key to query the utility?
        # [(x.y)][action]
        # {(1,1) : { isTerminal : true, utility: 0.5  }}
        # (1,1) -> (1,2)
        # Utility((1,1), action) <- Utility((1,1), action) + alpha * (reward +  gamma * Max(Utility((1,2), one_of_actions) - Utility((1,1), action) )
        # self.table = {}

    def is_terminal_state(self):
        # given coordinate, return true is that state is a terminal state
        pass

    def initialize_table(self):

        with open(self.input_file_name, 'r') as file:
            x_index = 0
            for line in file:
                numbers = line.split(sep='\t')
                j_index = 0
                for number in numbers:
                    key = (x_index, j_index)
                    self.q_table[key]["score"] = int(number)
                    for action in Action:
                        self.q_table[key][action] = 0
                    j_index += 1
                x_index += 1

    def __getitem__(self):
        pass

    def update_utility(self):
        pass

    def get_action_highest_utility(self):
        # given current location, find next action with the highest utility
        pass
