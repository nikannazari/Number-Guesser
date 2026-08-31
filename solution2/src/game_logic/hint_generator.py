def provide_hint(number, guess):
    '''
    Provides a hint to the user based on the guess.
    Args:
        number: int
        guess: int
    Returns:
        str: A hint to the user.
    '''
    if guess < number:
        return "Too low! Try again."
    elif guess > number:
        return "Too high! Try again."
    else:
        return "Congratulations! You guessed the number."
        