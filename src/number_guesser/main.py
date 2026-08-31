from .game.game import NumberGuessingGame
from .game.hint_generator import GuessResult
from .utils.commands import is_exit_command


def main() -> None:
    print("=" * 40)
    print("        NUMBER GUESSER")
    print("=" * 40)
    print("Guess a number between 1 and 100.")
    print("Type 'q' to quit.")
    print()

    game = NumberGuessingGame()

    while not game.finished:
        user_input = input("Your guess: ").strip()

        if is_exit_command(user_input):
            print("Thanks for playing!")
            return

        try:
            guess = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        try:
            response = game.make_guess(guess)
        except ValueError as error:
            print(error)
            continue

        if response.result == GuessResult.TOO_LOW:
            print("Too low!")
        elif response.result == GuessResult.TOO_HIGH:
            print("Too high!")
        else:
            print("🎉 Congratulations! You guessed the number!")

        print(f"Score: {response.score}")
        print(f"Attempts: {response.attempts}")
        print()

    if game.scorer.score == 0:
        print("Game over! Your score reached zero.")


if __name__ == "__main__":
    main()