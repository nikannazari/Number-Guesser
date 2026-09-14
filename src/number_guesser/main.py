from .code_game.code_game import FourDigitCodeGame
from .game.game import NumberGuessingGame
from .game.hint_generator import GuessResult
from .utils.commands import is_exit_command


def display_number_game_status(game: NumberGuessingGame) -> None:
    """Display the current number game status."""

    print(f"Score: {game.scorer.score}")
    print(f"Attempts: {game.attempts}")

    if game.remaining_attempts is not None:
        print(f"Remaining attempts: {game.remaining_attempts}")

    if game.guesses:
        print(f"Previous guesses: {game.guesses}")

    print()


def play_number_guessing_game() -> None:
    """Run the classic number guessing game."""

    print("=" * 45)
    print("          NUMBER GUESSING GAME")
    print("=" * 45)
    print("Guess a number between 1 and 100.")
    print("You have 10 attempts.")
    print("Type 'q' to quit.")
    print()

    game = NumberGuessingGame(
        start=1,
        end=100,
        initial_score=100,
        penalty=10,
        max_attempts=10,
    )

    while not game.finished:
        user_input = input("Your guess: ").strip()

        if is_exit_command(user_input):
            print("Returning to the main menu...")
            return

        try:
            guess = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a number.")
            print()
            continue

        try:
            response = game.make_guess(guess)

        except ValueError as error:
            print(error)
            print()
            continue

        if response.repeated:
            print("You already guessed this number.")
            print("Try a different number.")
            print()
            continue

        if response.result == GuessResult.TOO_LOW:
            print("📉 Too low!")

        elif response.result == GuessResult.TOO_HIGH:
            print("📈 Too high!")

        else:
            print("🎉 Congratulations!")
            print("You guessed the secret number!")

        print()
        display_number_game_status(game)

    if game.won:
        print("🏆 You won the number guessing game!")

    elif game.lost:
        print("💀 Game over!")

        if game.scorer.score == 0:
            print("Your score reached zero.")

        elif game.remaining_attempts == 0:
            print("You used all of your attempts.")

        print(f"The secret number was: {game.target}")

    print()


def display_code_feedback(feedback: list[str]) -> None:
    """Display colored feedback for a code guess."""

    symbols = {
        "green": "🟩 Green",
        "yellow": "🟨 Yellow",
        "red": "🟥 Red",
    }

    for color in feedback:
        print(symbols[color])

    print()


def play_four_digit_code_game() -> None:
    """Run the four-digit code guessing game."""

    print("=" * 45)
    print("           FOUR-DIGIT CODE GAME")
    print("=" * 45)
    print("Guess the secret four-digit code.")
    print("Rules:")
    print("- Use exactly 4 digits.")
    print("- Zero is not allowed.")
    print("- Digits must not repeat.")
    print()
    print("🟩 Green  = Correct digit and position")
    print("🟨 Yellow = Correct digit, wrong position")
    print("🟥 Red    = Digit does not exist")
    print()
    print("Type 'q' to return to the main menu.")
    print()

    game = FourDigitCodeGame(max_attempts=10)

    while not game.finished:
        guess = input("Your code: ").strip()

        if is_exit_command(guess):
            print("Returning to the main menu...")
            return

        try:
            response = game.make_guess(guess)

        except ValueError as error:
            print(error)
            print()
            continue

        if response.repeated:
            print("You already tried this code.")
            print("Try another code.")
            print()
            continue

        if response.won:
            print("🎉 Congratulations! You guessed the code!")
            print(f"Attempts: {response.attempts}")
            print()
            break

        print("Feedback:")
        display_code_feedback(response.feedback)

        print(f"Attempts: {response.attempts}")

        if response.remaining_attempts is not None:
            print(f"Remaining attempts: {response.remaining_attempts}")

        print()

    if game.lost:
        print("💀 Game over!")
        print(f"The correct code was: {game.correct_code}")
        print()


def display_main_menu() -> None:
    """Display the game selection menu."""

    print("=" * 45)
    print("              NUMBER GUESSER")
    print("=" * 45)
    print("1. Number Guessing Game")
    print("2. Four-Digit Code Game")
    print("q. Exit")
    print()


def main() -> None:
    """Run the Number Guesser application."""

    while True:
        display_main_menu()

        choice = input("Choose a game: ").strip().lower()

        if is_exit_command(choice):
            print("Thanks for playing!")
            break

        if choice == "1":
            play_number_guessing_game()

        elif choice == "2":
            play_four_digit_code_game()

        else:
            print("Invalid choice. Please select 1, 2, or q.")
            print()


if __name__ == "__main__":
    main()