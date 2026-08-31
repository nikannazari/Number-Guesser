import streamlit as st

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
    "Guess the secret number and try to keep your score!"
    "</div>",
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# Game State
# ---------------------------------------------------------

if "game" not in st.session_state:
    st.session_state.game = NumberGuessingGame(
        start=1,
        end=100,
        initial_score=100,
        penalty=10,
    )

if "last_result" not in st.session_state:
    st.session_state.last_result = None


game = st.session_state.game


# ---------------------------------------------------------
# Statistics
# ---------------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        f"""
        <div class="stat-card">
            <div class="stat-title">🏆 SCORE</div>
            <div class="stat-value">{game.scorer.score}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        f"""
        <div class="stat-card">
            <div class="stat-title">🎲 ATTEMPTS</div>
            <div class="stat-value">{game.attempts}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


st.divider()


# ---------------------------------------------------------
# Game Area
# ---------------------------------------------------------

if not game.finished:

    st.subheader("Make your guess")

    guess = st.number_input(
        "Enter a number",
        min_value=game.start,
        max_value=game.end,
        value=50,
        step=1,
    )

    if st.button(
        "🎯 Make Guess",
        use_container_width=True,
        type="primary",
    ):

        response = game.make_guess(guess)

        st.session_state.last_result = response.result

        st.rerun()


# ---------------------------------------------------------
# Result Message
# ---------------------------------------------------------

if st.session_state.last_result == GuessResult.TOO_LOW:

    st.markdown(
        """
        <div class="result-box low">
            📉 Your guess is <strong>TOO LOW</strong>!
            <br>
            Try a higher number.
        </div>
        """,
        unsafe_allow_html=True,
    )

elif st.session_state.last_result == GuessResult.TOO_HIGH:

    st.markdown(
        """
        <div class="result-box high">
            📈 Your guess is <strong>TOO HIGH</strong>!
            <br>
            Try a lower number.
        </div>
        """,
        unsafe_allow_html=True,
    )

elif st.session_state.last_result == GuessResult.CORRECT:

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

    st.balloons()


# ---------------------------------------------------------
# Game Over
# ---------------------------------------------------------

if game.finished and game.scorer.score == 0:

    st.markdown(
        """
        <div class="result-box game-over">
            💀 <strong>Game Over!</strong>
            <br>
            Your score reached zero.
        </div>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------
# Restart
# ---------------------------------------------------------

if game.finished:

    st.divider()

    if st.button(
        "🔄 Play Again",
        use_container_width=True,
    ):

        game.reset()
        st.session_state.last_result = None

        st.rerun()