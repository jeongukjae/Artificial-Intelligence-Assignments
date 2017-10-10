# -*- coding: utf8 -*-
import itertools

from elements import Node, House, Constraint
from constraints import CONSTRAINTS

COLORS          = ['blue', 'green', 'red', 'white', 'yellow']
NATIONALITIES   = ['Dane', 'Englishman', 'German', 'Swede', 'Norwegian']
DRINKS          = ['bier', 'coffee', 'milk', 'tea', 'water']
CIGARETTES      = ['Blend', 'BlueMaster', 'Dunhill', 'PallMall', 'Prince']
PETS            = ['birds', 'cats', 'dogs', 'fish', 'horses']

def check(node, constraints):
    for constraint in constraints:
        if not constraint.act(node):
            return False
    return True

def get_all_houses():
    houses = []
    for color in COLORS:
        for nationality in NATIONALITIES:
            for drink in DRINKS:
                for cigarette in CIGARETTES:
                    for pet in PETS:
                        houses.append(House(color, nationality, drink, cigarette, pet))

    return houses

def get_possible_node(houses, constraints):
    cnt = 0

    for houses in itertools.combinations(houses, 5):
        node = Node(houses)
        cnt += 1
        if check(node, constraints):
            print('valid node {0}'.format(node))
            return node

        if cnt % 100000 == 0:
            print("Step {0}".format(cnt))

if __name__ == "__main__":
    print(get_possible_node(get_all_houses(), CONSTRAINTS))
