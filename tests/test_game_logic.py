from logic_utils import check_guess, get_hint_message

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
