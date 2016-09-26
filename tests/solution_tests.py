import unittest
from solution import Solution, InvalidNodesException


test_data = [
    "A",
    "B A",
    "C A",
    "D A",
    "I B",
    "N B",
    "E D",
    "F D",
    "J I",
    "K I",
    "O N",
    "G F",
    "H F",
    "L K",
    "M K",
    "P",
    "Q P",
    "R P"
]

sln = Solution(test_data)

class solution_test(unittest.TestCase):
    def test_no_common_ancestor(self):
        self.assertEqual(sln.solve("Q", "M"), "No common ancestor")

    def test_invalid_nodes(self):
        with self.assertRaises(InvalidNodesException):
            sln.solve("Z", "2")

        with self.assertRaises(InvalidNodesException):
            sln.solve("A", "2")

        with self.assertRaises(InvalidNodesException):
            sln.solve("2", "B")

        with self.assertRaises(InvalidNodesException):
            sln.solve("B", "B")

    def test_correct_answer(self):
        self.assertEqual(sln.solve("B", "C"), "A")
        self.assertEqual(sln.solve("J", "C"), "A")
        self.assertEqual(sln.solve("M", "J"), "I")
        self.assertEqual(sln.solve("G", "E"), "D")

