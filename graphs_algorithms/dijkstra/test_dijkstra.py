import unittest
from shortest_path import Dijkstra


class TestDijkstra(unittest.TestCase):

    def test_finds_the_shortest_path(self):
        lines = self.get_file_lines("input/can_find_path.txt")
        dijkstra = Dijkstra(lines)

        expected_result = 9
        actual_result = dijkstra.compute()

        self.assertEqual(actual_result, expected_result)

    def test_doesnt_find_the_shortest_path(self):
        lines = self.get_file_lines("input/cannot_find_path.txt")
        dijkstra = Dijkstra(lines)

        expected_result = -1
        actual_result = dijkstra.compute()

        self.assertEqual(actual_result, expected_result)


    def get_file_lines(self, file_name):
        with open(file_name) as f:
            lines = f.readlines()
        lines = [x.strip() for x in lines]

        return lines


if __name__ == '__main__':
    unittest.main()
