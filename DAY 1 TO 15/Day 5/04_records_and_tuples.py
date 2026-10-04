"""Day 5 - Tuples as small records.

Logic concept: sorting structured rows, filtering records, and grouping.
"""


def make_student(name, score):
    """Return a ``(name, score)`` record."""
    return (name, score)


def sort_by_score(records, reverse=False):
    """Return records ordered by score without breaking name order."""
    ordered = sorted(records, key=lambda record: record[1], reverse=reverse)
    return list(ordered)


def highest_score(records):
    """Return the record with the biggest score, or ``None`` when empty."""
    if not records:
        return None
    best = records[0]
    for record in records[1:]:
        if record[1] > best[1]:
            best = record
    return best


def passing_records(records, cutoff=40):
    """Return only the records that reach ``cutoff``."""
    return [record for record in records if record[1] >= cutoff]


def average_score(records):
    """Return the mean score, or ``0.0`` when there are no records."""
    if not records:
        return 0.0
    total = 0
    for _name, score in records:
        total += score
    return total / len(records)


def names_of(records):
    """Return just the names from ``(name, score)`` records."""
    names = []
    for name, _score in records:
        names.append(name)
    return names


def score_board(records):
    """Return names ranked from the highest score to the lowest."""
    ranked = sort_by_score(records, reverse=True)
    return [name for name, _score in ranked]


def transpose_pairs(records):
    """Swap the two positions inside every record."""
    swapped = []
    for left, right in records:
        swapped.append((right, left))
    return swapped


def best_per_group(records):
    """Return ``group -> top score`` for ``(group, score)`` records."""
    best = {}
    for group, score in records:
        current = best.get(group)
        if current is None or score > current:
            best[group] = score
    return best


def rank_scores(records):
    """Return ``name -> rank`` where rank 1 is the highest score."""
    ranks = {}
    position = 1
    for name, _score in sort_by_score(records, reverse=True):
        ranks[name] = position
        position += 1
    return ranks


if __name__ == "__main__":
    rows = [("Asha", 72), ("Bala", 91), ("Chan", 65)]
    print("make_student('Asha', 72):", make_student("Asha", 72))
    print("sort_by_score(rows):", sort_by_score(rows))
    print("highest_score(rows):", highest_score(rows))
    print("passing_records(rows, 70):", passing_records(rows, 70))
    print("average_score(rows):", average_score(rows))
    print("names_of(rows):", names_of(rows))
    print("score_board(rows):", score_board(rows))
    print("transpose_pairs([(1, 2)]):", transpose_pairs([(1, 2)]))
    teams = [("red", 5), ("blue", 8), ("red", 6)]
    print("best_per_group(teams):", best_per_group(teams))
    print("rank_scores(rows):", rank_scores(rows))
