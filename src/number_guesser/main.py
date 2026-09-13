from .game.game import NumberGuessingGame
from .game.hint_generator import GuessResult
from .utils.commands import is_exit_command


def display_game_status(game: NumberGuessingGame) -> None:
    """Display the current game status."""

    print(f"Score: {game.scorer.score}")
    print(f"Attempts: {game.attempts}")

    if game.remaining_attempts is not None:
        print(f"Remaining attempts: {game.remaining_attempts}")

    if game.guesses:
        print(f"Previous guesses: {game.guesses}")

    print()


def main() -> None:
    """Run the Number Guesser CLI application."""

    print("=" * 45)
    print("              NUMBER GUESSER")
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
            print("Thanks for playing!")
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

        except RuntimeError as error:
            print(error)
            print()
            break

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

        display_game_status(game)

    if game.won:
        print("🏆 You won the game!")

    elif game.lost:
        print("💀 Game over!")

        if game.scorer.score == 0:
            print("Your score reached zero.")

        elif game.remaining_attempts == 0:
            print("You used all of your attempts.")

        print(f"The secret number was: {game.target}")

    print()
    print("Thanks for playing!")


if __name__ == "__main__":
    main()