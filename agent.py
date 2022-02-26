import random
from q_table import QTable, Action


class Agent:
    def __init__(self, file_name, greedy_epsilon):
        self.q_table = QTable(file_name)
        self.action_map = {Action.up: (-1, 0), Action.down: (1, 0), Action.left: (0, -1), Action.right: (0, 1)}
        self.current_x = 0
        self.current_y = 0
        self.greedy_epsilon = greedy_epsilon

    def move(self, x, y):
        # finally, move the agent to the new place by updateing its current x and y
        self.current_x = x
        self.current_y = y

    def pick_start_location(self):
        # greedily pick the next best next action
        max_x = self.q_table.max_x
        max_y = self.q_table.max_y
        next_x = random.randint(0, max_x)
        next_y = random.randint(0, max_y)

        flag_is_terminal = self.q_table.is_terminal_state(next_x, next_y)
        while flag_is_terminal:
            next_x = random.randint(0, max_x)
            next_y = random.randint(0, max_y)
            flag_is_terminal = self.q_table.is_terminal_state(next_x, next_y)
        self.current_y = next_y
        self.current_x = next_x

    def get_next_action_deviate(self, action):
        # deviate the action depending on the probability
        half_epsilon = (1 - self.greedy_epsilon) / 2
        explore_probability = random.uniform(0, 1)
        if half_epsilon < explore_probability < (1 - half_epsilon):
            return action
        match action:
            case Action.up:
                if explore_probability < half_epsilon:
                    return Action.left
                else:
                    return Action.right
            case Action.right:
                if explore_probability < half_epsilon:
                    return Action.up
                else:
                    return Action.down
            case Action.left:
                if explore_probability < half_epsilon:
                    return Action.down
                else:
                    return Action.up
            case Action.down:
                if explore_probability < half_epsilon:
                    return Action.right
                else:
                    return Action.left
        raise 'cannot identify next action'

    def find_next_best_action(self):
        # find the best action the agent should take
        best_action = None
        best_utility = -9999
        for action in Action:
            if self.q_table.get_utility(self.current_x, self.current_y, action) > best_utility:
                best_action = action
                best_utility = self.q_table.get_utility(self.current_x, self.current_y, best_action)
        return best_action

    def fix_edge_case(self, action):
        # at those edge cases, the agent bounce back
        max_x = self.q_table.max_x
        max_y = self.q_table.max_y
        next_x = self.current_x + self.action_map[action][0]
        next_y = self.current_y + self.action_map[action][1]
        if 0 <= next_x <= max_x and 0 <= next_y <= max_y:  # within boundary
            return next_x, next_y
        if self.current_y == max_y and self.current_x == max_x:  # right bottom corner
            if action is Action.down or action is Action.right:
                return self.current_x, self.current_y
            else:
                return next_x, next_y
        if self.current_y == self.current_x == 0:  # left top corner
            if action is Action.left or action is Action.up:
                return self.current_x, self.current_y
            else:
                return next_x, next_y
        if self.current_y == max_y and self.current_x == 0:  # right top corner
            if action is Action.up or action is Action.right:
                return self.current_x, self.current_y
            else:
                return next_x, next_y
        if self.current_y == 0 and self.current_x == max_x:  # left bottom corner
            if action is Action.left or action is Action.down:
                return self.current_x, self.current_y
            else:
                return next_x, next_y
        if self.current_y == 0:  # most left
            if action is Action.left:
                return self.current_x, self.current_y
            else:
                return next_x, next_y
        if self.current_y == max_y:  # most right
            if action is Action.right:
                return self.current_x, self.current_y
            else:
                return next_x, next_y
        if self.current_x == max_x:  # bottom
            if action is Action.down:
                return self.current_x, self.current_y
            else:
                return next_x, next_y
        if self.current_x == 0:  # top
            if action is Action.up:
                return self.current_x, self.current_y
            else:
                return next_x, next_y
        raise 'fix edge failed'

