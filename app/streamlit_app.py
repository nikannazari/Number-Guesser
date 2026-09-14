from __future__ import annotations

import streamlit as st

from number_guesser.code_game import FourDigitCodeGame
from number_guesser.game.game import NumberGuessingGame
from number_guesser.game.hint_generator import GuessResult


# =========================================================
# Page Configuration
# =========================================================

st.set_page_config(
    page_title="Number Guesser",
    page_icon="🎯",
    layout="centered",
    initial_sidebar_state="expanded",
)


# =========================================================
# Custom CSS
# =========================================================

st.markdown(
    """
    <style>
        .main {
            padding-top: 1.5rem;
        }

        .game-title {
            text-align: center;
            font-size: 3rem;
            font-weight: 800;
            margin-bottom: 0.25rem;
        }

        .game-subtitle {
            text-align: center;
            color: #888;
            font-size: 1.05rem;
            margin-bottom: 2rem;
        }

        .stat-card {
            border: 1px solid rgba(128, 128, 128, 0.3);
            border-radius: 14px;
            padding: 1rem;
            text-align: center;
            margin-bottom: 1rem;
        }

        .stat-title {
            color: #888;
            font-size: 0.85rem;
            margin-bottom: 0.3rem;
        }

        .stat-value {
            font-size: 1.8rem;
            font-weight: 800;
        }

        .result-box {
            border-radius: 14px;
            padding: 1.2rem;
            text-align: center;
            margin: 1rem 0;
            font-size: 1.1rem;
            font-weight: 600;
        }

        .low-box {
            background: rgba(255, 193, 7, 0.14);
            border: 1px solid rgba(255, 193, 7, 0.5);
        }

        .high-box {
            background: rgba(33, 150, 243, 0.14);
            border: 1px solid rgba(33, 150, 243, 0.5);
        }

        .success-box {
            background: rgba(76, 175, 80, 0.14);
            border: 1px solid rgba(76, 175, 80, 0.5);
        }

        .danger-box {
            background: rgba(244, 67, 54, 0.14);
            border: 1px solid rgba(244, 67, 54, 0.5);
        }

        .history-item {
            border: 1px solid rgba(128, 128, 128, 0.25);
            border-radius: 10px;
            padding: 0.8rem;
            margin-bottom: 0.5rem;
        }

        .code-digit {
            display: inline-block;
            width: 48px;
            height: 48px;
            line-height: 48px;
            text-align: center;
            border-radius: 10px;
            margin: 4px;
            color: white;
            font-size: 1.4rem;
            font-weight: 800;
        }

        .green-digit {
            background: #2e9d55;
        }

        .yellow-digit {
            background: #d6a500;
        }

        .red-digit {
            background: #d64545;
        }

        .section-title {
            font-size: 1.35rem;
            font-weight: 750;
            margin-top: 1rem;
            margin-bottom: 0.75rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# Session State Initialization
# =========================================================

if "selected_game" not in st.session_state:
    st.session_state.selected_game = "Number Guessing"

if "number_game" not in st.session_state:
    st.session_state.number_game = NumberGuessingGame(
        start=1,
        end=100,
        initial_score=100,
        penalty=10,
    )

if "code_game" not in st.session_state:
    st.session_state.code_game = FourDigitCodeGame()

if "number_history" not in st.session_state:
    st.session_state.number_history = []

if "code_history" not in st.session_state:
    st.session_state.code_history = []

if "last_number_result" not in st.session_state:
    st.session_state.last_number_result = None

if "last_code_response" not in st.session_state:
    st.session_state.last_code_response = None


# =========================================================
# Helper Functions
# =========================================================

def reset_number_game() -> None:
    st.session_state.number_game.reset()
    st.session_state.number_history = []
    st.session_state.last_number_result = None


def reset_code_game() -> None:
    st.session_state.code_game.reset()
    st.session_state.code_history = []
    st.session_state.last_code_response = None


def show_stat_card(title: str, value: str | int) -> None:
    st.markdown(
        f"""
        <div class="stat-card">
            <div class="stat-title">{title}</div>
            <div class="stat-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def show_number_result(result: GuessResult | None) -> None:
    if result == GuessResult.TOO_LOW:
        st.markdown(
            """
            <div class="result-box low-box">
                📉 Your guess is <strong>TOO LOW</strong>!
                <br>
                Try a higher number.
            </div>
            """,
            unsafe_allow_html=True,
        )

    elif result == GuessResult.TOO_HIGH:
        st.markdown(
            """
            <div class="result-box high-box">
                📈 Your guess is <strong>TOO HIGH</strong>!
                <br>
                Try a lower number.
            </div>
            """,
            unsafe_allow_html=True,
        )

    elif result == GuessResult.CORRECT:
        st.markdown(
            """
            <div class="result-box success-box">
                🎉 <strong>Congratulations!</strong>
                <br>
                You guessed the secret number!
            </div>
            """,
            unsafe_allow_html=True,
        )


def show_code_feedback(
    guess: str,
    feedback: list[str],
) -> None:
    if not feedback:
        return

    html_parts = []

    for digit, color in zip(guess, feedback):
        if color == "green":
            css_class = "green-digit"
        elif color == "yellow":
            css_class = "yellow-digit"
        else:
            css_class = "red-digit"

        html_parts.append(
            f'<span class="code-digit {css_class}">{digit}</span>'
        )

    st.markdown(
        "".join(html_parts),
        unsafe_allow_html=True,
    )


def show_code_legend() -> None:
    st.markdown(
        """
        **Feedback Legend:**

        🟩 Green: correct digit and correct position

        🟨 Yellow: correct digit but wrong position

        🟥 Red: digit does not exist in the secret code
        """
    )


# =========================================================
# Header
# =========================================================

st.markdown(
    '<div class="game-title">🎯 Number Guesser</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="game-subtitle">
        Choose a game and test your guessing skills.
    </div>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# Sidebar - Game Selection
# =========================================================

with st.sidebar:
    st.header("🎮 Game Selection")

    selected_game = st.radio(
        "Choose your game:",
        options=[
            "Number Guessing",
            "Four-Digit Code",
        ],
        index=(
            0
            if st.session_state.selected_game == "Number Guessing"
            else 1
        ),
    )

    if selected_game != st.session_state.selected_game:
        st.session_state.selected_game = selected_game
        st.rerun()

    st.divider()

    st.markdown("### About the games")

    if selected_game == "Number Guessing":
        st.info(
            """
            Guess a number between 1 and 100.

            Every wrong guess decreases your score.
            """
        )
    else:
        st.info(
            """
            Guess a 4-digit code.

            Digits cannot repeat.

            Green, Yellow and Red feedback will help you.
            """
        )


# =========================================================
# Number Guessing Game
# =========================================================

if selected_game == "Number Guessing":
    game: NumberGuessingGame = st.session_state.number_game

    st.subheader("🔢 Number Guessing Game")

    col1, col2, col3 = st.columns(3)

    with col1:
        show_stat_card("🏆 SCORE", game.scorer.score)

    with col2:
        show_stat_card("🎲 ATTEMPTS", game.attempts)

    with col3:
        show_stat_card("🎯 RANGE", f"{game.start} - {game.end}")

    st.divider()

    if not game.finished:
        st.markdown(
            '<div class="section-title">Make your guess</div>',
            unsafe_allow_html=True,
        )

        with st.form("number_guess_form"):
            guess = st.number_input(
                "Enter a number",
                min_value=game.start,
                max_value=game.end,
                value=50,
                step=1,
            )

            submitted = st.form_submit_button(
                "🎯 Make Guess",
                use_container_width=True,
                type="primary",
            )

        if submitted:
            try:
                response = game.make_guess(int(guess))

                st.session_state.last_number_result = response.result

                st.session_state.number_history.append(
                    {
                        "guess": int(guess),
                        "result": response.result.value,
                        "score": response.score,
                        "attempt": response.attempts,
                    }
                )

                st.rerun()

            except ValueError as error:
                st.error(str(error))

    show_number_result(st.session_state.last_number_result)

    if game.finished and game.scorer.score == 0:
        st.markdown(
            """
            <div class="result-box danger-box">
                💀 <strong>Game Over!</strong>
                <br>
                Your score reached zero.
            </div>
            """,
            unsafe_allow_html=True,
        )

    # -----------------------------------------------------
    # Number Guess History
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-title">📜 Guess History</div>',
        unsafe_allow_html=True,
    )

    if not st.session_state.number_history:
        st.caption("No guesses yet. Your guesses will appear here.")

    else:
        for item in reversed(st.session_state.number_history):
            result = item["result"]

            if result == "too_low":
                result_text = "📉 Too Low"
            elif result == "too_high":
                result_text = "📈 Too High"
            else:
                result_text = "🎉 Correct"

            st.markdown(
                f"""
                <div class="history-item">
                    <strong>Attempt {item["attempt"]}</strong>
                    &nbsp; | &nbsp;
                    Guess: <strong>{item["guess"]}</strong>
                    &nbsp; | &nbsp;
                    {result_text}
                    <br>
                    Score after guess: <strong>{item["score"]}</strong>
                </div>
                """,
                unsafe_allow_html=True,
            )

    if game.finished:
        st.divider()

        if st.button(
            "🔄 Play Number Guessing Again",
            use_container_width=True,
        ):
            reset_number_game()
            st.rerun()


# =========================================================
# Four-Digit Code Game
# =========================================================

elif selected_game == "Four-Digit Code":
    game: FourDigitCodeGame = st.session_state.code_game

    st.subheader("🔐 Four-Digit Code Game")

    st.write(
        "Guess a 4-digit code. Each digit must be unique and cannot be zero."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        show_stat_card("🔢 ATTEMPTS", game.attempts)

    with col2:
        show_stat_card("📏 CODE LENGTH", game.CODE_LENGTH)

    with col3:
        remaining = game.remaining_attempts

        if remaining is None:
            remaining_text = "∞"
        else:
            remaining_text = remaining

        show_stat_card("⏳ REMAINING", remaining_text)

    st.divider()

    show_code_legend()

    st.divider()

    if not game.finished:
        st.markdown(
            '<div class="section-title">Enter your code</div>',
            unsafe_allow_html=True,
        )

        with st.form("code_guess_form"):
            code_guess = st.text_input(
                "4-digit code",
                max_chars=4,
                placeholder="Example: 5821",
            )

            submitted = st.form_submit_button(
                "🔐 Check Code",
                use_container_width=True,
                type="primary",
            )

        if submitted:
            try:
                response = game.make_guess(code_guess)

                if response.repeated:
                    st.warning("You already tried this code.")
                else:
                    st.session_state.last_code_response = response

                    st.session_state.code_history.append(
                        {
                            "guess": response.guess,
                            "feedback": response.feedback,
                            "attempt": response.attempts,
                        }
                    )

                    st.rerun()

            except ValueError as error:
                st.error(str(error))

    # -----------------------------------------------------
    # Latest Code Feedback
    # -----------------------------------------------------

    last_response = st.session_state.last_code_response

    if last_response is not None:
        st.markdown(
            '<div class="section-title">Latest Feedback</div>',
            unsafe_allow_html=True,
        )

        st.write(f"Your guess: `{last_response.guess}`")

        show_code_feedback(
            last_response.guess,
            last_response.feedback,
        )

        if last_response.won:
            st.markdown(
                """
                <div class="result-box success-box">
                    🎉 <strong>You cracked the code!</strong>
                    <br>
                    Excellent work!
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.balloons()

        elif last_response.repeated:
            st.warning("This code was already guessed.")

    # -----------------------------------------------------
    # Code Game Over
    # -----------------------------------------------------

    if game.finished and game.won:
        st.markdown(
            """
            <div class="result-box success-box">
                🏆 You won the Four-Digit Code Game!
            </div>
            """,
            unsafe_allow_html=True,
        )

    elif game.finished and game.lost:
        st.markdown(
            f"""
            <div class="result-box danger-box">
                💀 <strong>Game Over!</strong>
                <br>
                The correct code was:
                <strong>{game.correct_code}</strong>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # -----------------------------------------------------
    # Code Guess History
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-title">📜 Code Guess History</div>',
        unsafe_allow_html=True,
    )

    if not st.session_state.code_history:
        st.caption("No code guesses yet.")

    else:
        for item in reversed(st.session_state.code_history):
            st.markdown(
                f"""
                <div class="history-item">
                    <strong>Attempt {item["attempt"]}</strong>
                    <br>
                    Code:
                    <strong>{item["guess"]}</strong>
                </div>
                """,
                unsafe_allow_html=True,
            )

            show_code_feedback(
                item["guess"],
                item["feedback"],
            )

    if game.finished:
        st.divider()

        if st.button(
            "🔄 Play Four-Digit Code Again",
            use_container_width=True,
        ):
            reset_code_game()
            st.rerun()