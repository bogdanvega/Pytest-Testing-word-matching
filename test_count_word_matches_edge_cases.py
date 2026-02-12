import pytest
from main import count_word_matches


@pytest.mark.parametrize("a, b, expected", [
    ("", "word", 0),
    ("hello world", "", 0),
    ("", "", 0),
    ("hello  world", "world", 1),
    (" cat ", "cat", 1),
    ("cat,dog cat", "cat", 1),
    ("x y z", "x", 1)
])


def test_count_word_matches_edge_cases(a, b, expected):
    assert count_word_matches(a, b) == expected


pytest.main()
