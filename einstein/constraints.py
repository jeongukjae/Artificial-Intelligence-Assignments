# -*- coding: utf8 -*-

from elements import Constraint

def C1(node):
    for house in node.houses:
        if SC1(house):
            return True

    return False

def C2(node):
    for house in node.houses:
        if SC2(house):
            return True

    return False

def C3(node):
    for house in node.houses:
        if SC3(house):
            return True

    return False

def C4(node):
    for i in range(5):
        house = node.houses[i]

        if house.color == 'green':
            if i is 4:
                break

            if node.houses[i + 1].color == 'white':
                return True
    return False

def C5(node):
    for house in node.houses:
        if SC5(house):
            return True

    return False

def C6(node):
    for house in node.houses:
        if SC6(house):
            return True

    return False

def C7(node):
    for house in node.houses:
        if SC7(house):
            return True

    return False

def C8(node):
    return node.houses[2].drink == 'milk'

def C9(node):
    return node.houses[0].nationality == 'Norwegian'

def C10(node):
    for i in range(5):
        house = node.houses[i]
        if house.cigarette == 'Blend':
            if (i < 4 and node.houses[i + 1].pet == 'cats') or\
                (i > 0  and node.houses[i - 1].pet == 'cats'):
                return True

            break

    return False

def C11(node):
    for i in range(5):
        house = node.houses[i]
        if house.pet == 'horses':
            if (i < 4 and node.houses[i + 1].cigarette == 'Dunhill') or\
                (i > 0  and node.houses[i - 1].cigarette == 'Dunhill'):
                return True

            break

    return False

def C12(node):
    for house in node.houses:
        if SC12(house):
            return True

    return False

def C13(node):
    for house in node.houses:
        if SC13(house):
            return True

    return False

def C14(node):
    for i in range(5):
        house = node.houses[i]
        if house.nationality == 'Norwegian':
            if (i < 4 and node.houses[i + 1].color == 'blue') or\
                (i > 0  and node.houses[i - 1].color == 'blue'):
                return True

            break

    return False

def C15(node):
    for i in range(5):
        house = node.houses[i]
        if house.cigarette == 'Blend':
            if (i < 4 and node.houses[i + 1].drink == 'water') or\
                (i > 0  and node.houses[i - 1].drink == 'water'):
                return True

            break

    return False

F = [
    C1,
    C2,
    C3,
    C4,
    C5,
    C6,
    C7,
    C8,
    C9,
    C10,
    C11,
    C12,
    C13,
    C14,
    C15
]

CONSTRAINTS = []

for f in F:
    CONSTRAINTS.append(Constraint(f))
