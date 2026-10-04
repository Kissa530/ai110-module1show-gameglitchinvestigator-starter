from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


def test_get_range_for_difficulty():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)


def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"


def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_guess_too_high_with_string_secret():
    outcome, message = check_guess(25, "20")
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_string_secret_is_compared_numerically():
    outcome, _ = check_guess(100, "20")
    assert outcome == "Too High"


def test_too_high_guess_always_loses_points():
    assert update_score(10, "Too High", 2) == 5
    assert update_score(10, "Too High", 3) == 5


def test_too_low_guess_loses_points():
    assert update_score(10, "Too Low", 2) == 5


def test_parse_guess_integer():
    assert parse_guess("42") == (True, 42, None)


def test_parse_guess_decimal():
    assert parse_guess("42.8") == (True, 42, None)


def test_parse_guess_empty_input():
    assert parse_guess("") == (False, None, "Enter a guess.")


def test_parse_guess_invalid_input():
    assert parse_guess("hello") == (False, None, "That is not a number.")
