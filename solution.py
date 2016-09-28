#!/usr/bin/env python
from __future__ import print_function
import sys


class InvalidNodesException(Exception):
    pass


class Tree(object):
    """ Tree/Node object. Very simple, takes a parent and a value.
    """
    def __init__(self, value=None, parent=None):
        self.value = value
        self.parent = parent


class Solution(object):
    def __init__(self, input_lines):
        self.input_lines = input_lines        
        self.build_tree_from_input()

    def build_tree_from_input(self):
        self.forest = {}
        for line in self.input_lines:
            nodes = line.split()
            if len(nodes) == 2:
                # Not a root node
                node_name, parent_name = nodes
            elif len(nodes) == 1:
                # Node is a root node, no parent specified
                if nodes:
                    node_name, parent_name = nodes[0], None
            else:
                # Deal with blank/invalid lines in input file
                continue

            parent = self.forest.get(parent_name)
            self.forest[node_name] = Tree(parent=parent, value=node_name)

    def get_parents(self, node):
        """ Function to get all parents in order from a node.
        """
        while node and node.parent:
            yield node.parent.value
            node = node.parent


    def solve(self, first_node, second_node):
        first_node = self.forest.get(first_node)
        second_node = self.forest.get(second_node)

        if not first_node or not second_node:
            raise InvalidNodesException("Invalid nodes given.")
        elif first_node == second_node:
            raise InvalidNodesException("Nodes are the same.")

        path1 = list(self.get_parents(first_node))
        path2 = list(self.get_parents(second_node))
        nca = self.nearest_common_ancestor(path1, path2)

        if nca:
            return nca
        else:
            return "No common ancestor"

    @staticmethod
    def nearest_common_ancestor(first_path, second_path):
        """ This function begins iterating over the shortest path until it finds 
            the first ancestor the two lists have in common. It will be the 
            nearest because the paths are represented as nodes in order back to 
            their root.
        """
        if len(first_path) < len(second_path):
            for node in first_path:
                if node in second_path:
                    return node
        else:
            for node in second_path:
                if node in first_path:
                    return node


if __name__ == "__main__":
    try:
        input_file, first_node, second_node = sys.argv[1:]
    except:
        print("Check parameters and try again.\n"
              "Usage: python solution.py <input_file> <node 1> <node 2>")
        sys.exit(1)

    with open(input_file) as f:
        input_lines = f.readlines()

    solution = Solution(input_lines)
    print(solution.solve(first_node, second_node))

