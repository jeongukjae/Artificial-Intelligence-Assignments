# -*- coding: utf8 -*-
 
class House:
    def __init__(self, color, nationality, drink, cigarette, pet):
        self.color = color
        self.nationality = nationality
        self.drink = drink
        self.cigarette = cigarette
        self.pet = pet

    def __repr__(self):
        return "<House [{0}, {1}, {2}, {3}, {4}]>".format(
            self.color, self.nationality, self.drink, self.cigarette, self.pet)

class Node:
    def __init__(self, houses):
        self.houses = houses

    def __repr__(self):
        return "<Node {0}>".format(self.houses)

class Constraint:
    def __init__(self, func):
        self.func = func

    def act(self, node):
        return self.func(node)
