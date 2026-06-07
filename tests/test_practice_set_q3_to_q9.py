import io
import unittest
from contextlib import redirect_stdout

from Pratice_1.practice_set_q3_to_q9 import (
    binary_search,
    flatten_deep,
    group_anagrams,
    most_frequent,
    pascal_triangle,
    rotate_matrix,
    two_sum,
)


class PracticeSetTests(unittest.TestCase):
    def test_two_sum_finds_pair(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])

    def test_two_sum_returns_empty_when_missing(self):
        self.assertEqual(two_sum([1, 2, 3], 10), [])

    def test_flatten_deep_handles_many_levels(self):
        nested = [[1, [2, 3]], [4, [5, [6]]]]
        self.assertEqual(flatten_deep(nested), [1, 2, 3, 4, 5, 6])

    def test_group_anagrams_groups_words(self):
        words = ["eat", "tea", "tan", "ate", "nat", "bat"]
        got = group_anagrams(words)
        normalized = sorted(sorted(group) for group in got)
        expected = sorted(
            [
                ["ate", "eat", "tea"],
                ["nat", "tan"],
                ["bat"],
            ]
        )
        self.assertEqual(normalized, expected)

    def test_binary_search_found_and_missing(self):
        arr = [1, 3, 5, 7, 9]
        self.assertEqual(binary_search(arr, 7), 3)
        self.assertEqual(binary_search(arr, 4), -1)

    def test_most_frequent(self):
        self.assertEqual(most_frequent([1, 2, 2, 3, 3, 3, 4]), 3)

    def test_most_frequent_empty_list(self):
        self.assertIsNone(most_frequent([]))

    def test_rotate_matrix_changes_matrix_in_place(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        returned = rotate_matrix(matrix)
        expected = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3],
        ]
        self.assertIs(returned, matrix)
        self.assertEqual(matrix, expected)

    def test_pascal_triangle_prints_rows(self):
        out = io.StringIO()

        with redirect_stdout(out):
            pascal_triangle(5)

        self.assertEqual(
            out.getvalue().splitlines(),
            [
                "[1]",
                "[1, 1]",
                "[1, 2, 1]",
                "[1, 3, 3, 1]",
                "[1, 4, 6, 4, 1]",
            ],
        )


if __name__ == "__main__":
    unittest.main()
