# 🎯 Number Guesser

A modular number guessing game built with **Python**, featuring both a **Command Line Interface (CLI)** and a modern **Streamlit web interface**.

The project is designed with a separation between the core game logic and the user interface, making the code easier to maintain, test, and extend.

---

## 📸 Overview

**Number Guesser** is a game where the player tries to guess a randomly generated secret number within a defined range.

The player starts with a score and loses points after every incorrect guess.

The game provides feedback after every attempt:

* 📉 **Too Low** — the guessed number is lower than the secret number.
* 📈 **Too High** — the guessed number is higher than the secret number.
* 🎉 **Correct** — the player successfully guessed the secret number.

The game ends when the player guesses the correct number or their score reaches zero.

---

# ✨ Features

### 🎮 Gameplay

* 🎲 Random secret number generation
* 🎯 Guess evaluation
* 📉 Too Low hints
* 📈 Too High hints
* 🎉 Correct guess detection
* 🏆 Score system
* 🔢 Attempt counter
* 🔄 Game reset
* 💀 Game Over state

### 💻 Interfaces

* Command Line Interface (CLI)
* Streamlit Web Interface
* Responsive and simple web UI
* Interactive game controls

### 🧑‍💻 Development

* Modular Python architecture
* Object-Oriented Programming
* Type hints
* Dataclasses
* Enums
* Input validation
* Unit testing with Pytest
* Python package structure
* Git/GitHub ready

---

# 🎮 Game Rules

The default game configuration is:

| Setting                 | Value |
| ----------------------- | ----: |
| Minimum number          |     1 |
| Maximum number          |   100 |
| Initial score           |   100 |
| Penalty per wrong guess |    10 |

### Example

The game starts with:

```text
Score: 100
```

If the player makes an incorrect guess:

```text
Wrong Guess
     ↓
Score - 10
     ↓
Score: 90
```

The process continues until the player guesses correctly or reaches:

```text
Score: 0
```

---

# 🧠 Architecture

The project separates the game logic from the user interface.

```text
                         USER
                           │
                           ▼
                 ┌──────────────────┐
                 │   User Interface │
                 │                  │
                 │ CLI / Streamlit  │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │   Game Engine    │
                 └────────┬─────────┘
                          │
            ┌─────────────┼─────────────┐
            │             │             │
            ▼             ▼             ▼
       Number          Hint          Scoring
      Generator       System         System
            │             │             │
            └─────────────┼─────────────┘
                          │
                          ▼
                     Game Result
```

The core game engine does not depend on Streamlit.

This means the same game logic can later be reused by:

* CLI
* Streamlit
* REST API
* Desktop GUI
* Mobile application
* Other interfaces

---

# 🏗️ Project Structure

```text
Number-Guesser/
│
├── app/
│   └── streamlit_app.py
│
├── assets/
│
├── src/
│   └── number_guesser/
│       ├── __init__.py
│       ├── main.py
│       │
│       ├── game/
│       │   ├── __init__.py
│       │   ├── game.py
│       │   ├── hint_generator.py
│       │   ├── number_generator.py
│       │   └── scorer.py
│       │
│       └── utils/
│           ├── __init__.py
│           ├── commands.py
│           └── input_validator.py
│
├── tests/
│   ├── __init__.py
│   ├── test_game.py
│   ├── test_hint_generator.py
│   ├── test_number_generator.py
│   └── test_scorer.py
│
├── .github/
│   └── workflows/
│
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── pyproject.toml
```

---

# 🛠️ Technologies

The project currently uses:

* **Python** — Core programming language
* **Streamlit** — Web interface
* **Pytest** — Unit testing
* **Git** — Version control
* **GitHub** — Repository and collaboration

---

# 🚀 Installation

## 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd Number-Guesser
```

---

## 2. Create a virtual environment

### Linux / macOS

```bash
python -m venv .venv
```

### Windows

```powershell
python -m venv .venv
```

---

## 3. Activate the virtual environment

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```powershell
.venv\Scripts\activate
```

---

## 4. Install the project

Install the project in editable mode with development dependencies:

```bash
pip install -e ".[dev]"
```

This installs:

* The Number Guesser package
* Streamlit
* Pytest

---

# 💻 Running the CLI

From the project root:

```bash
python -m number_guesser.main
```

You should see:

```text
========================================
        NUMBER GUESSER
========================================
Guess a number between 1 and 100.
Type 'q' to quit.

Your guess:
```

Enter a number between `1` and `100`.

You can exit the game using:

```text
q
quit
exit
```

---

# 🌐 Running the Streamlit Web App

From the project root:

```bash
streamlit run app/streamlit_app.py
```

Streamlit will start a local server.

Open the displayed address in your browser, usually:

```text
http://localhost:8501
```

The Streamlit interface provides:

* 🎯 Number input
* 🏆 Score display
* 🎲 Attempt counter
* 📉 Too Low feedback
* 📈 Too High feedback
* 🎉 Winning notification
* 💀 Game Over state
* 🔄 Play Again button

---

# 🧪 Running Tests

Run all tests:

```bash
pytest -v
```

Or:

```bash
pytest
```

The test suite covers the main game components:

```text
Number Generator
       │
       ├── Range validation
       └── Random number generation

Hint Generator
       │
       ├── Too Low
       ├── Too High
       └── Correct

Scorer
       │
       ├── Initial score
       ├── Penalties
       ├── Score limit
       └── Reset

Game Engine
       │
       ├── Initialization
       ├── Guess processing
       ├── Winning
       ├── Game Over
       └── Reset
```

---

# 📦 Dependencies

The project uses the following main dependencies:

```text
streamlit
pytest
```

Dependencies are listed in:

```text
requirements.txt
```

and development configuration is defined in:

```text
pyproject.toml
```

---

# 🔧 Configuration

The default game configuration is defined when creating the game:

```python
game = NumberGuessingGame(
    start=1,
    end=100,
    initial_score=100,
    penalty=10,
)
```

This makes the game engine configurable.

For example, a different game could use:

```python
game = NumberGuessingGame(
    start=1,
    end=1000,
    initial_score=500,
    penalty=25,
)
```

---

# 🧩 Core Components

## Number Generator

Responsible for generating the secret number.

```python
generate_number(1, 100)
```

---

## Hint Generator

Evaluates the player's guess:

```text
Guess < Secret Number
        ↓
     TOO_LOW

Guess > Secret Number
        ↓
     TOO_HIGH

Guess == Secret Number
        ↓
     CORRECT
```

---

## Scorer

Controls:

* Initial score
* Penalties
* Minimum score
* Score reset

The score can never become negative.

---

## Game Engine

`NumberGuessingGame` connects the main components together.

It manages:

* Secret number
* Player guesses
* Attempts
* Score
* Game state
* Game reset

---

# 🔮 Future Improvements

The project is intentionally designed to be extensible.

Possible future features include:

### 🎮 Gameplay

* [ ] Difficulty levels
* [ ] Easy / Medium / Hard modes
* [ ] Custom number ranges
* [ ] Custom scoring
* [ ] Maximum attempts
* [ ] Limited lives
* [ ] Streak system
* [ ] Combo system

### 🏆 Statistics

* [ ] High score
* [ ] Game history
* [ ] Win rate
* [ ] Average attempts
* [ ] Best performance
* [ ] Leaderboard

### 🌐 Web Application

* [ ] Improved animations
* [ ] Sound effects
* [ ] Dark / Light themes
* [ ] Better responsive design
* [ ] Game statistics dashboard
* [ ] Player profiles

### 🔌 Backend

* [ ] REST API
* [ ] Database support
* [ ] User authentication
* [ ] Online leaderboard
* [ ] Multiplayer mode

### 🚀 Deployment

* [ ] Docker support
* [ ] Docker Compose
* [ ] CI/CD
* [ ] Cloud deployment
* [ ] Automated releases

### 🧪 Testing

* [ ] Higher test coverage
* [ ] Integration tests
* [ ] Streamlit testing
* [ ] Property-based testing
* [ ] Automated code quality checks

---

# 📚 Learning Goals

This project is also a practical Python learning project.

The main concepts practiced include:

### Python

* Variables
* Functions
* Classes
* Object-Oriented Programming
* Modules
* Packages
* Type hints
* Dataclasses
* Enums
* Exceptions
* Properties

### Software Engineering

* Project structure
* Separation of concerns
* Modular architecture
* Testing
* Dependency management
* Virtual environments
* Documentation

### Tools

* Git
* GitHub
* Streamlit
* Pytest
* Python packaging

---

# 🤝 Contributing

Contributions and suggestions are welcome.

If you find a bug or have an idea for a new feature:

1. Open an issue.
2. Describe the problem or feature.
3. Create a branch.
4. Make your changes.
5. Add or update tests.
6. Submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.

See the `LICENSE` file for more information.

---

# 👨‍💻 Author

**Nikan Nazari**

---

⭐ If you find this project useful, consider giving it a star on GitHub.
