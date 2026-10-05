from logic_utils import check_guess, get_hint_message, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_too_high_hint_directs_lower():
    outcome = check_guess(60, 50)
    assert get_hint_message(outcome) == "📉 Go LOWER!"

def test_too_low_hint_directs_higher():
    outcome = check_guess(40, 50)
    assert get_hint_message(outcome) == "📈 Go HIGHER!"

def test_empty_guess_returns_prompt():
    assert parse_guess("") == (False, None, "Enter a guess.")

def test_non_numeric_guess_returns_error():
    assert parse_guess("abc") == (False, None, "That is not a number.")

def test_decimal_guess_is_not_silently_truncated():
    assert parse_guess("12.7") == (False, None, "That is not a number.")

def test_negative_guess_compares_as_too_low():
    ok, guess, error = parse_guess("-4")
    assert ok and error is None and guess == -4
    assert check_guess(guess, 10) == "Too Low"

def test_extremely_large_guess_compares_as_too_high():
    ok, guess, error = parse_guess("9" * 100)
    assert ok and error is None and guess is not None
    assert check_guess(guess, 10) == "Too High"
