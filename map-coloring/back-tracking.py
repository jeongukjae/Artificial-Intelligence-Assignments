# -*- coding: utf8 -*-
from problem import Variables ,Domains, Constraints, get_possible_colors, initialize_problem, goal_test

def select_variable(state):
    for vars in Variables:
        if state[vars] is None:
            return vars

def check_constraints(state):
    for constraint in Constraints:
        if not constraint(state):
            return False

    return True

def recursive_backtracking(state):
    # if the state passes goal test, returns state
    if goal_test(state):
        return state

    # select a region to be assigned value
    region = select_variable(state)

    for value in Domains:
        copied_state = state.copy()
        copied_state[region] = value

        if check_constraints(copied_state):
            result = recursive_backtracking(copied_state)

            if result:
                return result

    # if fail
    return False

def backtracking_search():
    return recursive_backtracking(initialize_problem())

if __name__ == "__main__":
    result = backtracking_search()
    print(result)
