# Learnings

Running notes from the logic practice repo.

## Current Notes

- Hash maps are useful when a problem asks for quick lookup, like two sum.
- Recursion works well for nested structures when each level has the same shape.
- Binary search needs sorted input and careful left/right pointer updates.
- A frequency dictionary is enough for most "count items" problems.
- Small examples at the bottom of a file make practice code easy to run.
- Reusable functions are easier to test when print code stays under
  `if __name__ == "__main__"`.

## Day 4-7 Notes

- A plain `counts[key] = counts.get(key, 0) + 1` loop is enough for almost every
  counting problem; no imports needed.
- Copying a dict with `dict(record)` before editing keeps functions free of
  surprise side effects on the caller's data.
- Set operators (`&`, `-`, `^`, `|`) express "common", "missing", and "unique"
  far more clearly than nested loops.
- Tuple unpacking such as `first, *middle, last = items` removes a lot of index
  bookkeeping.
- `zip(..., strict=True)` catches mismatched lengths early instead of silently
  dropping items.
- Every recursive function needs a base case that returns without calling itself,
  plus an input that shrinks on each step.
- Backtracking only works when the state is undone after each branch fails;
  without that undo step every branch sees polluted data.
- Comprehensions shine for one simple transform and hurt once the expression
  needs a loop inside it.
- Passing a function as an argument (`sorted(key=...)`, `filter(...)`) removes
  most needs for lambdas.
