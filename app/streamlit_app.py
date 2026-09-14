import streamlit as st

from number_guesser.code_game.code_game import FourDigitCodeGame
from number_guesser.game.game import NumberGuessingGame
from number_guesser.game.hint_generator import GuessResult


# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="Number Guesser",
    page_icon="🎯",
    layout="centered",
)


# ---------------------------------------------------------
# Custom CSS
# ---------------------------------------------------------

st.markdown(
    """
    <style>
        .main {
            padding-top: 2rem;
        }

        .game-title {
            text-align: center;
            font-size: 3rem;
            font-weight: 800;
            margin-bottom: 0.2rem;
        }

        .game-subtitle {
            text-align: center;
            color: #777;
            font-size: 1.1rem;
            margin-bottom: 2rem;
        }

        .stat-card {
            padding: 1rem;
            border-radius: 12px;
            border: 1px solid rgba(128, 128, 128, 0.25);
            text-align: center;
            margin-bottom: 1rem;
        }

        .stat-title {
            font-size: 0.9rem;
            color: #777;
        }

        .stat-value {
            font-size: 1.8rem;
            font-weight: 700;
        }

        .result-box {
            padding: 1.5rem;
            border-radius: 15px;
            text-align: center;
            margin: 1.5rem 0;
            font-size: 1.2rem;
            font-weight: 600;
        }

        .low {
            background-color: rgba(255, 193, 7, 0.15);
            border: 1px solid rgba(255, 193, 7, 0.4);
        }

        .high {
            background-color: rgba(33, 150, 243, 0.15);
            border: 1px solid rgba(33, 150, 243, 0.4);
        }

        .success-box {
            background-color: rgba(76, 175, 80, 0.15);
            border: 1px solid rgba(76, 175, 80, 0.4);
        }

        .game-over {
            background-color: rgba(244, 67, 54, 0.15);
            border: 1px solid rgba(244, 67, 54, 0.4);
        }

        .feedback-digit {
            font-size: 1.5rem;
            font-weight: 700;
            text-align: center;
            padding: 0.8rem;
            border-radius: 12px;
            margin-bottom: 0.5rem;
        }

        .green-digit {
            background-color: rgba(76, 175, 80, 0.2);
            border: 1px solid rgba(76, 175, 80, 0.5);
        }

        .yellow-digit {
            background-color: rgba(255, 193, 7, 0.2);
            border: 1px solid rgba(255, 193, 7, 0.5);
        }

        .red-digit {
            background-color: rgba(244, 67, 54, 0.2);
            border: 1px solid rgba(244, 67, 54, 0.5);
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# Header
# ---------------------------------------------------------

st.markdown(
    '<div class="game-title">🎯 Number Guesser</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="game-subtitle">'
    "Choose a game and test your guessing skills."
    "</div>",
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# Game Selection
# ---------------------------------------------------------

if "selected_game" not in st.session_state:
    st.session_state.selected_game = "Number Guessing"

selected_game = st.radio(
    "Choose your game",
    options=[
        "Number Guessing",
        "Four-Digit Code",
    ],
    horizontal=True,
)

if selected_game != st.session_state.selected_game:
    st.session_state.selected_game = selected_game
    st.session_state.number_game = None
    st.session_state.code_game = None
    st.session_state.last_result = None
    st.session_state.last_code_response = None
    st.rerun()


# ---------------------------------------------------------
# Number Guessing Game
# ---------------------------------------------------------

if selected_game == "Number Guessing":
    if (
        "number_game" not in st.session_state
        or st.session_state.number_game is None
    ):
        st.session_state.number_game = NumberGuessingGame(
            start=1,
            end=100,
            initial_score=100,
            penalty=10,
            max_attempts=10,
        )

    if "last_result" not in st.session_state:
        st.session_state.last_result = None

    game = st.session_state.number_game

    st.subheader("🔢 Number Guessing Game")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Score", game.scorer.score)

    with col2:
        st.metric("Attempts", game.attempts)

    with col3:
        remaining = (
            "∞"
            if game.remaining_attempts is None
            else game.remaining_attempts
        )
        st.metric("Remaining", remaining)

    st.divider()

    if game.guesses:
        st.subheader("📜 Guess History")
        st.write(game.guesses)

    if not game.finished:
        guess = st.number_input(
            "Enter a number",
            min_value=game.start,
            max_value=game.end,
            value=game.start,
            step=1,
        )

        if st.button(
            "🎯 Make Guess",
            use_container_width=True,
            type="primary",
        ):
            response = game.make_guess(int(guess))
            st.session_state.last_result = response.result
            st.rerun()

    if st.session_state.last_result == GuessResult.TOO_LOW:
        st.warning("📉 Too low! Try a higher number.")

    elif st.session_state.last_result == GuessResult.TOO_HIGH:
        st.info("📈 Too high! Try a lower number.")

    elif st.session_state.last_result == GuessResult.CORRECT:
        st.success("🎉 Congratulations! You guessed the number!")
        st.balloons()

    if game.finished and game.lost:
        st.error("💀 Game over!")
        st.write(f"The secret number was: **{game.target}**")

    if game.finished and game.won:
        st.success(
            f"You won with {game.attempts} attempts "
            f"and a score of {game.scorer.score}."
        )

    if st.button(
        "🔄 Restart Number Game",
        use_container_width=True,
    ):
        game.reset()
        st.session_state.last_result = None
        st.rerun()


# ---------------------------------------------------------
# Four-Digit Code Game
# ---------------------------------------------------------

else:
    if (
        "code_game" not in st.session_state
        or st.session_state.code_game is None
    ):
        st.session_state.code_game = FourDigitCodeGame(
            max_attempts=10,
        )

    if "last_code_response" not in st.session_state:
        st.session_state.last_code_response = None

    game = st.session_state.code_game

    st.subheader("🔐 Four-Digit Code Game")

    st.write(
        "Guess a four-digit code without repeated digits or zero."
    )

    st.markdown(
        """
        🟩 **Green:** Correct digit and position

        🟨 **Yellow:** Correct digit, wrong position

        🟥 **Red:** Digit does not exist
        """
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Attempts", game.attempts)

    with col2:
        remaining = (
            "∞"
            if game.remaining_attempts is None
            else game.remaining_attempts
        )
        st.metric("Remaining", remaining)

    st.divider()

    if not game.finished:
        guess = st.text_input(
            "Enter your 4-digit code",
            max_chars=4,
            placeholder="1234",
        )

        if st.button(
            "🔐 Check Code",
            use_container_width=True,
            type="primary",
        ):
            try:
                response = game.make_guess(guess)
                st.session_state.last_code_response = response

            except ValueError as error:
                st.error(str(error))

            st.rerun()

    response = st.session_state.last_code_response

    if response is not None:
        if response.repeated:
            st.warning("You already tried this code.")

        elif response.won:
            st.success("🎉 Congratulations! You guessed the secret code!")
            st.balloons()

        else:
            st.subheader("Feedback")

            feedback_columns = st.columns(4)

            for index, color in enumerate(response.feedback):
                digit = response.guess[index]

                with feedback_columns[index]:
                    if color == "green":
                        css_class = "green-digit"
                        label = "Green"

                    elif color == "yellow":
                        css_class = "yellow-digit"
                        label = "Yellow"

                    else:
                        css_class = "red-digit"
                        label = "Red"

                    st.markdown(
                        f"""
                        <div class="feedback-digit {css_class}">
                            {digit}
                            <br>
                            <small>{label}</small>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

            if game.finished and game.lost:
                st.error("💀 Game over!")
                st.write(
                    f"The correct code was: **{game.correct_code}**"
                )

    if game.guesses:
        st.subheader("📜 Guess History")

        for index, guessed_code in enumerate(game.guesses, start=1):
            st.write(f"{index}. `{guessed_code}`")

    if st.button(
        "🔄 Restart Code Game",
        use_container_width=True,
    ):
        game.reset()
        st.session_state.last_code_response = None
        st.rerun()