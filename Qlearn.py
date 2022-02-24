def run_qlearning():
    while not_reach_time_limit() or not_terminal_state:
        next_location = get_next_location() # also handle the deviate
        agent.move(next_location) # after moving, update the Q_table as well
        update_Qtable()
        not_terminal_state = q_table.is_terminal_state(next_location)
