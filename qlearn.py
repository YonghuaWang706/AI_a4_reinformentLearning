import sys
from agent import Agent
from time import time


class Q_Learning:
    def __init__(self, seconds_to_tun, constant_reward, file_name, greedy_epsilon, alpha=0.1, gamma=0.9):
        self.agent = Agent(file_name, greedy_epsilon)
        self.seconds_to_tun = seconds_to_tun
        self.start_time = 0
        self.alpha = alpha
        self.gamma = gamma
        self.reward = constant_reward

    def run_Q_learning(self):
        # run Q learning
        self.start_time = time()
        self.agent.pick_start_location()
        while self.not_reach_time_limit():
            self.agent.pick_start_location()
            while not self.agent.q_table.is_terminal_state(self.agent.current_x, self.agent.current_y):
                if not self.not_reach_time_limit():
                    break
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
    if len(sys.argv) < 4:
        sys.exit("invalid argument, try python3 qlearn.py <file> <seconds to run> <probability to move in desired "
                 "direction> <reward>")
    temp, filename, runtime, prob, reward = sys.argv
    runtime = float(runtime)
    prob = float(prob)
    reward = float(reward)
    instance = Q_Learning(runtime, reward, filename, prob)
    instance.agent.q_table.initialize_table()
    instance.run_Q_learning()
    instance.agent.q_table.print_training_result()

