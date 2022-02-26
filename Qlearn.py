import agent
from agent import Agent
from time import time


# def run_qlearning():
#     while not_reach_time_limit() or not_terminal_state:
#         next_location = get_next_location() # also handle the deviate
#         agent.move(next_location) # after moving, update the Q_table as well
#         update_Qtable()
#         not_terminal_state = q_table.is_terminal_state(next_location)

class Q_Learning:
    def __init__(self, seconds_to_tun, alpha, gamma, reward, file_name, greedy_epsilon):
        self.agent = Agent(file_name, greedy_epsilon)
        self.seconds_to_tun = seconds_to_tun
        self.start_time = 0
        self.alpha = alpha
        self.gamma = gamma
        self.reward = reward

    def run_Q_learning(self):
        # run Q learning
        self.start_time = time()
        while self.not_reach_time_limit():
            self.agent.pick_start_location()
            while not self.agent.q_table.is_terminal_state(self.agent.current_x, self.agent.current_y):
                next_best_action = self.agent.find_next_best_action()
                deviate_action = self.agent.get_next_action_deviate(next_best_action)
                next_x, next_y = self.agent.fix_edge_case(deviate_action)
                previous_location = (self.agent.current_x, self.agent.current_y)
                next_location = (next_x, next_y)
                self.agent.q_table.update_utility(self.alpha, self.gamma, deviate_action, previous_location,
                                                  next_location, self.reward)
                self.agent.move(next_x, next_y)

    def not_reach_time_limit(self):
        # check if time limit has been reached
        return (time() - self.start_time) < self.seconds_to_tun


if __name__ == '__main__':
    instance = Q_Learning(10, 0.1, 1, -0.05, 'sample.txt', 0.1)
    instance.agent.q_table.initialize_table()
    instance.run_Q_learning()
    instance.agent.q_table.print_training_result()
