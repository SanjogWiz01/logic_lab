import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).parents[1]
DAYS = ROOT / "DAY 1 TO 15"


def load_day_module(day, filename):
    path = DAYS / f"Day {day}" / filename
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class DayFourTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.basics = load_day_module(4, "01_dict_basics.py")
        cls.counting = load_day_module(4, "02_counting_and_grouping.py")
        cls.sets = load_day_module(4, "03_sets.py")
        cls.transforms = load_day_module(4, "04_dict_transformations.py")

    def test_dict_basics(self):
        profile = self.basics.make_profile("Asha", 24, "Pune")
        self.assertEqual(profile["name"], "Asha")
        self.assertEqual(self.basics.get_value(profile, "pin", "none"), "none")
        self.assertEqual(self.basics.add_or_update(profile, "age", 25)["age"], 25)
        self.assertEqual(self.basics.increment({}, "views"), {"views": 1})
        self.assertEqual(self.basics.merge_records({"a": 1}, {"a": 9}), {"a": 9})
        self.assertEqual(
            self.basics.rename_key(profile, "city", "town")["town"], "Pune"
        )
        self.assertNotIn("age", self.basics.drop_key(profile, "age"))
        self.assertEqual(self.basics.invert({"a": 1}), {1: "a"})
        self.assertEqual(
            self.basics.sort_by_value({"a": 3, "b": 1}), [("b", 1), ("a", 3)]
        )
        self.assertEqual(self.basics.keys_above({"a": 1, "b": 5}, 2), ["b"])

    def test_counting_and_grouping(self):
        counts = self.counting.char_counts("aab")
        self.assertEqual(counts, {"a": 2, "b": 1})
        self.assertEqual(self.counting.word_counts("a b a")["a"], 2)
        self.assertEqual(self.counting.most_common(counts, 1), [("a", 2)])
        self.assertEqual(self.counting.first_max_key(counts), "a")
        self.assertIsNone(self.counting.first_max_key({}))
        self.assertEqual(self.counting.group_by_length(["hi", "ox"]), {2: ["hi", "ox"]})
        grouped = self.counting.group_anagrams(["eat", "tea", "bat"])
        self.assertEqual(grouped["aet"], ["eat", "tea"])
        self.assertEqual(self.counting.duplicates_found([1, 2, 2, 1]), [1, 2])
        self.assertEqual(self.counting.running_total([1, 2, 3])[3], 6)

    def test_sets(self):
        self.assertEqual(self.sets.common_items([1, 2, 3], [2, 3, 4]), [2, 3])
        self.assertEqual(self.sets.only_in_first([1, 2], [2, 3]), [1])
        self.assertEqual(self.sets.in_either([1, 2], [2, 3]), [1, 3])
        self.assertEqual(self.sets.in_either_or_both([1, 2], [2, 3]), [1, 2, 3])
        self.assertTrue(self.sets.is_subset([1], [1, 2]))
        self.assertTrue(self.sets.is_disjoint([1], [2]))
        self.assertEqual(self.sets.unique_in_order([1, 2, 1]), [1, 2])
        self.assertEqual(self.sets.split_unique([1, 2, 3], [2]), ([2], [1, 3]))
        self.assertEqual(self.sets.rotate_cycle([1, 2, 3], 2), [3, 1, 2])

    def test_dict_transformations(self):
        merged = self.transforms.deep_merge({"a": {"x": 1}}, {"a": {"y": 2}})
        self.assertEqual(merged, {"a": {"x": 1, "y": 2}})
        flat = self.transforms.flatten_record({"u": {"n": "a"}})
        self.assertEqual(flat, {"u.n": "a"})
        rows = [{"d": "eng"}, {"d": "eng"}, {"d": "ops"}]
        self.assertEqual(self.transforms.count_by_key(rows, "d"), {"eng": 2, "ops": 1})
        self.assertEqual(self.transforms.top_values({"a": 1, "b": 5}, 1), [("b", 5)])
        self.assertEqual(self.transforms.values_below({"a": 1, "b": 5}, 5), {"a": 1})
        self.assertEqual(self.transforms.shared_keys({"a": 1}, {"a": 0, "c": 3}), ["a"])


class DayFiveTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.basics = load_day_module(5, "01_tuple_basics.py")
        cls.unpacking = load_day_module(5, "02_unpacking.py")
        cls.zipping = load_day_module(5, "03_zip_and_enumerate.py")
        cls.records = load_day_module(5, "04_records_and_tuples.py")

    def test_tuple_basics(self):
        self.assertEqual(self.basics.first_and_last([4, 5]), (4, 5))
        self.assertEqual(self.basics.first_and_last([]), (None, None))
        self.assertEqual(self.basics.swap_ends([1, 2, 3]), (3, 2, 1))
        self.assertEqual(self.basics.rotate_tuple((1, 2, 3), 1), (2, 3, 1))
        self.assertEqual(self.basics.middle_slice((1, 2, 3)), (2,))
        self.assertEqual(self.basics.clamp_pair((-5, 12), 0, 10), (0, 10))
        self.assertEqual(self.basics.distance_manhattan((0, 0), (3, 4)), 7)
        self.assertTrue(self.basics.is_palindrome_tuple((1, 2, 1)))

    def test_unpacking(self):
        self.assertEqual(self.unpacking.sum_and_product([2, 3]), (5, 6))
        self.assertEqual(self.unpacking.head_and_tail([7, 8]), (7, [8]))
        self.assertEqual(self.unpacking.starred_middle([1, 2, 3]), (1, [2], 3))
        self.assertEqual(self.unpacking.collect_heads([[1, 2], [3]]), [1, 3])
        self.assertEqual(self.unpacking.nested_unpack(((("a", 1)), "p")), ("a", "p"))
        self.assertEqual(self.unpacking.unpack_to_dict(["a"], [1]), {"a": 1})
        self.assertEqual(self.unpacking.swap_in_place([1, 2], 0, 1), [2, 1])
        self.assertEqual(self.unpacking.compare_pairs([1, 2], [1, 3]), -1)

    def test_zip_and_enumerate(self):
        self.assertEqual(self.zipping.index_items(["a"]), [(0, "a")])
        self.assertEqual(self.zipping.index_items_starting_at(["a"]), [(1, "a")])
        self.assertEqual(self.zipping.pair_shortest([1, 2], ["a"]), [(1, "a")])
        self.assertEqual(
            self.zipping.pair_longest([1], ["a", "b"]), [(1, "a"), (None, "b")]
        )
        self.assertEqual(self.zipping.zip_dicts(["a"], [1]), {"a": 1})
        self.assertEqual(self.zipping.unzip_pairs([(1, "a")]), ([1], ["a"]))
        self.assertEqual(self.zipping.positions_of([1, 1, 2], 1), [0, 1])
        self.assertEqual(self.zipping.running_pairs([1, 2, 3]), [(1, 2), (2, 3)])
        with self.assertRaises(ValueError):
            self.zipping.pair_same_length([1], [1, 2])

    def test_records_and_tuples(self):
        rows = [("Asha", 72), ("Bala", 91)]
        self.assertEqual(self.records.sort_by_score(rows), [("Asha", 72), ("Bala", 91)])
        self.assertEqual(self.records.highest_score(rows), ("Bala", 91))
        self.assertIsNone(self.records.highest_score([]))
        self.assertEqual(self.records.passing_records(rows, 80), [("Bala", 91)])
        self.assertEqual(self.records.average_score(rows), 81.5)
        self.assertEqual(self.records.score_board(rows), ["Bala", "Asha"])
        self.assertEqual(self.records.best_per_group([("a", 1), ("a", 4)]), {"a": 4})
        self.assertEqual(self.records.rank_scores(rows), {"Bala": 1, "Asha": 2})


class DaySixTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.basics = load_day_module(6, "01_recursion_basics.py")
        cls.tree = load_day_module(6, "02_tree_recursion.py")
        cls.divide = load_day_module(6, "03_divide_and_conquer.py")
        cls.backtrack = load_day_module(6, "04_backtracking.py")

    def test_recursion_basics(self):
        self.assertEqual(self.basics.factorial(5), 120)
        self.assertEqual(self.basics.sum_to(5), 15)
        self.assertEqual(self.basics.countdown(3), [3, 2, 1])
        self.assertEqual(self.basics.fib(7), 13)
        self.assertEqual(self.basics.power(2, 5), 32)
        self.assertEqual(self.basics.digit_sum(9182), 20)
        self.assertTrue(self.basics.is_palindrome_number(121))
        self.assertFalse(self.basics.is_palindrome_number(123))
        self.assertEqual(self.basics.greatest_common_divisor(48, 18), 6)
        with self.assertRaises(ValueError):
            self.basics.power(2, -1)

    def test_tree_recursion(self):
        nested = [1, [2, [3, 4]], 5]
        self.assertEqual(self.tree.flatten(nested), [1, 2, 3, 4, 5])
        self.assertEqual(self.tree.nested_total(nested), 15)
        self.assertEqual(self.tree.nested_depth(nested), 2)
        self.assertEqual(self.tree.count_leaves(nested), 5)
        self.assertEqual(self.tree.nested_max(nested), 5)
        self.assertIn("1.1.0=3", self.tree.tree_paths(nested))
        self.assertTrue(self.tree.contains(nested, 4))
        self.assertFalse(self.tree.contains(nested, 9))

    def test_divide_and_conquer(self):
        self.assertEqual(self.divide.recursive_binary_search([1, 3, 5, 7], 7), 3)
        self.assertEqual(self.divide.recursive_binary_search([1, 3, 5, 7], 4), -1)
        self.assertEqual(self.divide.merge([1, 4], [2, 3]), [1, 2, 3, 4])
        self.assertEqual(self.divide.merge_sort([5, 3, 9, 1]), [1, 3, 5, 9])
        self.assertEqual(self.divide.sum_range(1, 10), 55)
        self.assertEqual(self.divide.count_divisors(28), 6)
        self.assertEqual(self.divide.count_pairs_with_sum([1, 2, 3, 4], 5), 2)
        self.assertEqual(self.divide.count_pairs_with_sum([1, 2, 3, 4], 99), 0)

    def test_backtracking(self):
        self.assertEqual(
            sorted(map(len, self.backtrack.all_subsets([1, 2]))), [0, 1, 1, 2]
        )
        self.assertEqual(len(self.backtrack.all_permutations([1, 2, 3])), 6)
        self.assertEqual(len(self.backtrack.permutations_of_size([1, 2, 3], 2)), 6)
        self.assertEqual(
            self.backtrack.combinations([1, 2, 3], 2), [[1, 2], [1, 3], [2, 3]]
        )
        grid = [["A", "B"], ["C", "D"]]
        self.assertTrue(self.backtrack.word_exists(grid, "AB"))
        self.assertTrue(self.backtrack.word_exists(grid, "AC"))
        self.assertFalse(self.backtrack.word_exists(grid, "AD"))
        self.assertFalse(self.backtrack.word_exists(grid, "AA"))


class DaySevenTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lists = load_day_module(7, "01_list_comprehensions.py")
        cls.dicts = load_day_module(7, "02_dict_and_set_comprehensions.py")
        cls.pipelines = load_day_module(7, "03_map_filter_reduce.py")
        cls.lambdas = load_day_module(7, "04_lambdas_and_sorting.py")

    def test_list_comprehensions(self):
        self.assertEqual(self.lists.square_each([1, 2, 3]), [1, 4, 9])
        self.assertEqual(self.lists.keep_positive([-2, 0, 5]), [5])
        self.assertEqual(self.lists.squares_of_range(3), [0, 1, 4])
        self.assertEqual(self.lists.flatten([[1, 2], [3]]), [1, 2, 3])
        self.assertEqual(self.lists.scale_pairs([1, 2], [10, 20]), [10, 40])
        self.assertEqual(self.lists.pair_with_index(["a"]), [(0, "a")])
        self.assertEqual(self.lists.running_totals([1, 2, 3]), [1, 3, 6])
        self.assertEqual(self.lists.rotate_list([1, 2, 3], 2), [3, 1, 2])

    def test_dict_and_set_comprehensions(self):
        self.assertEqual(self.dicts.index_of_each(["a", "b"]), {"a": 0, "b": 1})
        self.assertEqual(self.dicts.counts_of([1, 1, 2]), {1: 2, 2: 1})
        self.assertEqual(self.dicts.unique_items([1, 1, 2]), {1, 2})
        self.assertEqual(self.dicts.lengths_of(["hi"]), {"hi": 2})
        self.assertEqual(self.dicts.invert({"a": 1}), {1: "a"})
        self.assertEqual(self.dicts.keep_big_values({"a": 1, "b": 5}, 5), {"b": 5})
        self.assertEqual(self.dicts.characters_in("a b"), {"a", "b"})
        self.assertEqual(self.dicts.squares_to_dict(3), {0: 0, 1: 1, 2: 4})
        self.assertEqual(self.dicts.duplicates([1, 2, 2]), {2})

    def test_map_filter_reduce(self):
        self.assertEqual(self.pipelines.double_each([1, 2]), [2, 4])
        self.assertEqual(self.pipelines.absolute_values([-3, 4]), [3, 4])
        self.assertEqual(self.pipelines.keep_even([1, 2, 3, 4]), [2, 4])
        self.assertEqual(self.pipelines.total_of([1, 2, 3]), 6)
        self.assertEqual(self.pipelines.product_of([2, 3]), 6)
        self.assertEqual(self.pipelines.longest_word(["a", "logic"]), "logic")
        self.assertIsNone(self.pipelines.longest_word([]))
        self.assertEqual(self.pipelines.apply_pipeline([1, 2, 3, 4]), [4, 8])
        self.assertEqual(self.pipelines.average_of([2, 4]), 3.0)
        self.assertEqual(self.pipelines.average_of([]), 0.0)
        self.assertTrue(self.pipelines.any_negative([1, -1]))
        self.assertTrue(self.pipelines.all_even([2, 4]))
        self.assertFalse(self.pipelines.all_even([2, 5]))

    def test_lambdas_and_sorting(self):
        self.assertEqual(self.lambdas.apply_twice(abs, -3), 3)
        self.assertEqual(self.lambdas.make_adder(10)(5), 15)
        self.assertEqual(self.lambdas.sort_numbers_by([3, 1]), [1, 3])
        self.assertEqual(self.lambdas.sort_by_length(["ccc", "a"]), ["a", "ccc"])
        self.assertEqual(
            self.lambdas.sort_records_by([("a", 2), ("b", 1)]), [("b", 1), ("a", 2)]
        )
        self.assertEqual(self.lambdas.sort_by_second_letter(["ab", "ba"]), ["ba", "ab"])
        self.assertEqual(self.lambdas.pick([1, 2, 3], lambda n: n > 1), [2, 3])
        self.assertEqual(self.lambdas.transform([1, 2], lambda n: n + 1), [2, 3])
        self.assertEqual(self.lambdas.compose_functions(abs, lambda n: -n)(-4), 4)
        self.assertEqual(self.lambdas.top_n([4, 9, 1], 2), [9, 4])


if __name__ == "__main__":
    unittest.main()
