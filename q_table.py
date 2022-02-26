from enum import Enum


class Action(Enum):
    up = 1
    down = 2
    left = 3
    right = 4


class QTable:
    def __init__(self, file_name):
        self.q_table = {}
        self.input_file_name = file_name
        self.max_x = 0
        self.max_y = 0
        # use (x, y , Action) as the key to query the utility?
        # [(x.y)][action]
        # {(1,1) : { isTerminal : true, utility: 0.5  }}
        # (1,1) -> (1,2)
        # Utility((1,1), action) <- Utility((1,1), action) + alpha * (reward +  gamma * Max(Utility((1,2), one_of_actions) - Utility((1,1), action) )
        # self.table = {}

    def is_terminal_state(self, x, y):
        # given coordinate, return true is that state is a terminal state
        return self.q_table[(x, y)]['is_terminal_state']

    def initialize_table(self):
        # initialize the q_table from the input file
        i_index = 0
        j_index = 0
        with open(self.input_file_name, 'r') as file:
            for line in file:
                numbers = line.split(sep='\t')
                j_index = 0
                for number in numbers:
                    key = (i_index, j_index)
                    score = int(number)
                    self.q_table[key] = {}
                    self.q_table[key]["score"] = score
                    self.q_table[key]["is_terminal_state"] = score != 0
                    for action in Action:
                        self.q_table[key][action] = score
                    j_index += 1
                i_index += 1
        self.max_x = i_index - 1
        self.max_y = j_index - 1

    def update_utility(self, alpha, gamma, action, previous_location, next_location, reward):
        # update the Q_table according to the formula
        previous_utility = self.q_table[previous_location][action]
        next_location_max_utility = self.get_action_highest_utility(next_location)
        self.q_table[previous_location][action] = previous_utility + alpha * (
                reward + gamma * (next_location_max_utility - previous_utility))

    def get_action_highest_utility(self, next_location):
        # given current location, find next action with the highest utility
        next_location_max_utility = -9999
        for action in Action:
            current_utility = self.q_table[next_location][action]
            if current_utility > next_location_max_utility:
                next_location_max_utility = current_utility
        return next_location_max_utility

    def get_utility(self, x, y, action):
        # helper function to query the utility associated with the action
        return self.q_table[(x, y)][action]

    def print_training_result(self):
        # print the training result, the best action to take on each location
        action_figure = {Action.up: '^', Action.down: 'v', Action.left: '<', Action.right: '>'}
        for i in range(self.max_x + 1):
            for j in range(self.max_y + 1):
                best_action = None
                best_utility_sofar = -9999
                action_dict = self.q_table[(i, j)]
                for action in Action:
                    if action_dict[action] > best_utility_sofar:
                        best_utility_sofar = action_dict[action]
                        best_action = action
                if self.is_terminal_state(i, j):
                    print(self.q_table[(i,j)]['score'], end='\t')
                else:
                    print(action_figure[best_action], end='\t')
            print("\n")


if __name__ == '__main__':
    q_table_instance = QTable('sample.txt')
    q_table_instance.initialize_table()
    print(q_table_instance.q_table)
