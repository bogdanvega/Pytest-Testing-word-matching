import pytest
from main import count_word_matches


@pytest.mark.parametrize("a, b, expected", [
    ("The cat sat on the mat", "cat", 1),
    ("Dog dog DOG dOg", "dog", 4),
    ("Hello world", "world", 1),
    ("hello hello HELLO", "hello", 3),
    ("No matches here", "yes", 0),
    ("catcat cat catdog", "cat", 1),
    ("a a a", "a", 3)
])


def test_count_word_matches_basic(a, b, expected):
    assert count_word_matches(a, b) == expected


pytest.main()
