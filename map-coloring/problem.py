# -*- coding:utf8 -*-

# regions
WA = 'Western Austrailia'
NT = 'Northern Territory'
Q = 'Queensland'
NSW = 'New South Wales'
V = 'Victoria'
SA = 'South Australia'
T = 'Tasmania'

# define problem
Variables = [WA, NT, Q, NSW, V, SA, T]
Domains = ['red', 'green', 'blue']

RegionConnections = [
    (WA, NT),
    (WA, SA),
    (NT, Q),
    (NT, SA),
    (SA, Q),
    (SA, NSW),
    (SA, V),
    (Q, NSW),
    (NSW, V)
]

def initialize_problem():
    # this function returns an initial state of problem
    return {
        WA: None,
        NT: None,
        Q: None,
        NSW: None,
        V: None,
        SA: None,
        T: None
    }

def c_check_adjacent_region(state):
    # check adjacent region's color
    # Constraints : "adjacent regions must have different colors"
    # this function returns true if the state satisfies constraints.

    # + this function does not check the color of a region is a "None".
    for tuple_of_regions in RegionConnections:
        region1, region2 = tuple_of_regions
        if state[region1] is None or state[region2] is None:
            continue
        if state[region1] == state[region2]:
            return False

    return True

def get_possible_colors(state, region):
    # get possible colors from state and selected region.
    # this function returns a list that includes possible colors
    domains = Domains[:]

    for tuple_of_regions in RegionConnections:
        if region in tuple_of_regions:
            another_region = tuple_of_regions[tuple_of_regions.index(region) ^ 1]

            if state[another_region] in domains:
                domains.pop(state[another_region])

    return domains

def goal_test(state):
    # goal test function
    # this function returns True if a state is the goal state.

    # all regions have to be assigned values.
    for region in state:
        if state[region] is None:
            return False

    if not c_check_adjacent_region(state):
        return False

    return True

Constraints = [
    c_check_adjacent_region
]
