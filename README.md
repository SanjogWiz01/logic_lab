# logic-lab-py
Python practice repo for building problem-solving confidence one small program at a
time.

The goal is simple: write code regularly, keep the solutions easy to read, and use
Git history as proof of daily progress.

## Current Structure
```text
logic_lab/
├── DAY 1 TO 15/              # Day 1-7 practice files, four per day
├── Foundations/              # Early loop, pattern, and sliding-window practice
├── Pratice_1/                # First main practice set and separate Q files
├── tests/                    # Automated checks for reusable solutions
├── LEARNINGS.md              # Notes from practice sessions
└── README.md
```

The folder name `Pratice_1` is kept as-is because that is the current working
folder used in this repo.

## Daily Practice Plan

Each day lives in its own folder inside `DAY 1 TO 15/` and holds four files.

| Day | Topic | Files |
|-----|-------|-------|
| 1 | Truthiness, operators, conditionals, loops | `01_truthy_falsy.py`, `02_operators.py`, `03_conditionals.py`, `04_loops.py` |
| 2 | Strings: reversing, counting, building, slicing | `01_string_reversing.py`, `02_char_counting.py`, `03_string_building.py`, `04_slicing_and_tokens.py` |
| 3 | Lists: searching, reversing, sorting, nesting | `01_list_searching.py`, `02_list_reversing.py`, `03_sorting.py`, `04_nested_lists.py` |
| 4 | Dictionaries and sets | `01_dict_basics.py`, `02_counting_and_grouping.py`, `03_sets.py`, `04_dict_transformations.py` |
| 5 | Tuples and unpacking | `01_tuple_basics.py`, `02_unpacking.py`, `03_zip_and_enumerate.py`, `04_records_and_tuples.py` |
| 6 | Recursion, divide and conquer, backtracking | `01_recursion_basics.py`, `02_tree_recursion.py`, `03_divide_and_conquer.py`, `04_backtracking.py` |
| 7 | Comprehensions and functional pipelines | `01_list_comprehensions.py`, `02_dict_and_set_comprehensions.py`, `03_map_filter_reduce.py`, `04_lambdas_and_sorting.py` |

Run a day file with its full path, since the folder name contains spaces:

```powershell
python "DAY 1 TO 15\Day 4\01_dict_basics.py"
```

## Practice Files

| File | Topic |
|------|-------|
| `Pratice_1/01.py` | Prime number check |
| `Pratice_1/fibo.py` | Fibonacci with memoization |
| `Pratice_1/practice_set_q3_to_q9.py` | Clean reusable solutions for Q3-Q9 |
| `Pratice_1/q3_two_sum.py` | Two sum short practice file |
| `Pratice_1/q4_flatten.py` | Deep list flattening |
| `Pratice_1/q5_anagram.py` | Group anagrams |
| `Pratice_1/q6_bin_search.py` | Binary search |
| `Pratice_1/q7_freq.py` | Most frequent element |

## Run Examples

Run the full reusable practice set:

```powershell
python Pratice_1\practice_set_q3_to_q9.py
```

Run a single short practice file:

```powershell
python Pratice_1\q3_two_sum.py
```

## Run Tests

The test suite uses only Python's standard library.

```powershell
python -m unittest discover -s tests
```

## Commit Style

Use small commits with direct messages:

```text
Add q6 binary search practice
Add tests for practice set
Update repo documentation
```

## Ground Rules

- Write the solution first, then improve it.
- Keep beginner practice files simple and honest.
- Keep reusable files import-safe with `if __name__ == "__main__"`.
- Add tests when a file contains reusable functions.
- Commit each meaningful step.

## Progress

| Area | Status |
|------|--------|
| Foundation practice | Started |
| Practice set Q3-Q9 | Done |
| Separate Q3-Q7 files | Done |
| Basic automated tests | Added |
| Learning log | Added |
| Day 1-3 (basics, strings, lists) | Done |
| Day 4-7 (dicts, tuples, recursion, comprehensions) | Done |
| Day 8-15 | Not started |

## Quick commands

- Run tests: python -m unittest discover -s tests
- Lint locally: pip install ruff black isort && ruff check . && black --check .

