import pytest
from main import count_word_matches


@pytest.mark.parametrize("a, b, expected", [
    (None, "word", TypeError),
    ("hello world", None, TypeError),
    (123, "word", TypeError),
    ("hello world", 456, TypeError),
    (["hello", "world"], "world", TypeError),
    ("hello world", ["world"], TypeError),
])


def test_count_word_matches_negative(a, b, expected):
    if not isinstance(a, str) or not isinstance(b, str):
        with pytest.raises(TypeError):
            count_word_matches(a, b)
    else:
        assert count_word_matches(a, b) == expected


pytest.main()
