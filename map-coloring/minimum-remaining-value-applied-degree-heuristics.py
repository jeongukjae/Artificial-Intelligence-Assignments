# -*- coding: utf8 -*-
from problem import Variables, Domains, Constraints, RegionConnections, get_possible_colors, initialize_problem, goal_test

def get_the_number_of_each_constraints(region1, region2):
    cnt1 = 0
    cnt2 = 0
    for connection in RegionConnections:
        if region1 in connection:
            cnt1 += 1
        
        if region2 in connection:
            cnt2 += 1

    return cnt1, cnt2

def select_variable(state):
    minimum_value_count = len(Domains)
    minimum_value_region = None

    for region in state:
        if state[region] is None:
            if minimum_value_region is None:
                minimum_value_region = region
                minimum_value_count = len(get_possible_colors(state, region))
            else:
                temp_var = len(get_possible_colors(state, region))
                if temp_var < minimum_value_count:
                    minimum_value_region = region
                    minimum_value_count = temp_var
                elif temp_var == minimum_value_count:
                    cnt1, cnt2 = get_the_number_of_each_constraints(minimum_value_region, region)

                    if cnt1 < cnt2:
                        minimum_value_region = region
                        minimum_value_count = temp_var

    return minimum_value_region

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
