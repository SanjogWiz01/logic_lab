import importlib.util
import io
import pathlib
import unittest
from contextlib import redirect_stdout

from Foundations.loop1 import factorial
from Foundations.sliding_window import longest_unique_substring
from Foundations.star_pattern import ascending_stars, descending_stars
from Pratice_1.fibo import fibo
from Pratice_1.practice_set_q3_to_q9 import (
    binary_search,
    flatten_deep,
    group_anagrams,
    most_frequent,
    pascal_triangle,
    rotate_matrix,
    two_sum,
)


def load_prime_module():
    path = pathlib.Path(__file__).parents[1] / "Pratice_1" / "01.py"
    spec = importlib.util.spec_from_file_location("prime_practice", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class SolutionTests(unittest.TestCase):
    def test_factorial_and_prime(self):
        self.assertEqual(factorial(5), 120)
        self.assertFalse(load_prime_module().is_prime(1))
        self.assertTrue(load_prime_module().is_prime(97))

    def test_fibonacci_and_sliding_window(self):
        self.assertEqual([fibo(n) for n in range(7)], [0, 1, 1, 2, 3, 5, 8])
        self.assertEqual(longest_unique_substring("abcabcbb"), 3)
        self.assertEqual(longest_unique_substring(""), 0)

    def test_patterns(self):
        self.assertEqual(ascending_stars(3), ["*", "**", "***"])
        self.assertEqual(descending_stars(3), ["***", "**", "*"])

    def test_q3_to_q7(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(flatten_deep([1, [2, [3]], 4]), [1, 2, 3, 4])
        self.assertEqual(
            group_anagrams(["eat", "tea", "bat"]), [["eat", "tea"], ["bat"]]
        )
        self.assertEqual(binary_search([1, 3, 5, 7], 5), 2)
        self.assertEqual(most_frequent([1, 2, 2, 1, 1]), 1)

    def test_matrix_and_pascal(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(rotate_matrix(matrix), [[7, 4, 1], [8, 5, 2], [9, 6, 3]])
        output = io.StringIO()
        with redirect_stdout(output):
            result = pascal_triangle(3)
        self.assertIsNone(result)
        self.assertEqual(output.getvalue().splitlines(), ["[1]", "[1, 1]", "[1, 2, 1]"])


if __name__ == "__main__":
    unittest.main()
