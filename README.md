# logic-lab-py

Python practice repo for building problem-solving confidence one small program at a
time.

The goal is simple: write code regularly, keep the solutions easy to read, and use
Git history as proof of daily progress.

## Current Structure

```text
logic_lab/
├── Foundations/              # Early loop, pattern, and sliding-window practice
├── Pratice_1/                # First main practice set and separate Q files
├── tests/                    # Automated checks for reusable solutions
├── LEARNINGS.md              # Notes from practice sessions
└── README.md
```

The folder name `Pratice_1` is kept as-is because that is the current working
folder used in this repo.

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
