# -*- coding: utf8 -*-
# 걍 EightPuzzle 클래스 감싸는 Node 클래스

class Node:
    def __init__(self, depth, data):
        self.children = []
        self.depth = depth
        self.data = data

    def get_depth(self):
        return self.depth

    def get_data(self):
        return self.data

    def set_parent(self, parent):
        self.parent = parent

    def append_child(self, child):
        self.children.append(child)

    def get_parent(self):
        return self.parent

    def get_children(self):
        return self.children