# 🎯 Number Guesser

A modular number guessing game built with **Python**, featuring both a **Command Line Interface (CLI)** and a modern **Streamlit web interface**.

The project is designed with a separation between the core game logic and the user interface, making the code easier to maintain and extend.

---

## 📸 Overview

**Number Guesser** is a game where the player tries to guess a randomly generated secret number within a defined range.

The player starts with a score and loses points after every incorrect guess.

After each guess, the game provides feedback:

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
* Interactive web UI
* Real-time game feedback
* Responsive layout

### 🧑‍💻 Code Structure

* Modular Python architecture
* Object-Oriented Programming
* Separation of game logic and UI
* Reusable game components
* Python package structure
* Configurable game settings

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

After an incorrect guess:

```text
Wrong Guess
     ↓
Score - 10
     ↓
Score: 90
```

The process continues until the player guesses correctly or the score reaches:

```text
Score: 0
```

---

# 🧠 Architecture

The project separates the core game engine from the user interface.

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

The game engine is independent from Streamlit, allowing the same core logic to be reused with different interfaces in the future.

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
├── .gitignore
├── LICENSE
├── README.md
├── pyproject.toml
└── requirements.txt
```

---

# 🛠️ Technologies

The project currently uses:

* **Python** — Core programming language
* **Streamlit** — Web interface
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

## 4. Install dependencies

Install the required dependencies:

```bash
pip install -r requirements.txt
```

The main dependency is:

```text
streamlit
```

---

# 💻 Running the CLI

After activating the virtual environment, run:

```bash
export PYTHONPATH="$PWD/src:$PYTHONPATH"
```

Then:

```bash
python -m number_guesser.main
```

The game will start in your terminal.

You can enter a number between `1` and `100`.

To exit the game, use:

```text
q
quit
exit
```

---

# 🌐 Running the Streamlit Web App

From the project root, first make sure the package can be imported:

```bash
export PYTHONPATH="$PWD/src:$PYTHONPATH"
```

Then start Streamlit:

```bash
streamlit run app/streamlit_app.py
```

Streamlit will start a local web server.

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

# 📦 Dependencies

Project dependencies are listed in:

```text
requirements.txt
```

Install them with:

```bash
pip install -r requirements.txt
```

Current dependency:

```text
streamlit>=1.40
```

---

# 🔧 Configuration

The game engine is configurable.

For example:

```python
game = NumberGuessingGame(
    start=1,
    end=100,
    initial_score=100,
    penalty=10,
)
```

The configuration controls:

| Parameter       | Description                         |
| --------------- | ----------------------------------- |
| `start`         | Minimum possible number             |
| `end`           | Maximum possible number             |
| `initial_score` | Starting player score               |
| `penalty`       | Score lost after an incorrect guess |

This allows different game configurations to be created without changing the core game logic.

---

# 🧩 Core Components

## 🎲 Number Generator

Responsible for generating the secret number within the configured range.

```text
Minimum ─────────────── Maximum
   │                         │
   └──── Random Number ──────┘
```

---

## 💡 Hint Generator

Compares the player's guess with the secret number.

```text
Guess < Secret Number
        ↓
     TOO LOW

Guess > Secret Number
        ↓
     TOO HIGH

Guess == Secret Number
        ↓
      CORRECT
```

---

## 🏆 Scorer

Responsible for managing the player's score.

It handles:

* Initial score
* Score penalties
* Minimum score
* Score updates
* Score reset

The score cannot become negative.

---

## 🎮 Game Engine

`NumberGuessingGame` coordinates the different components of the game.

It manages:

* Secret number
* Player guesses
* Attempts
* Score
* Game state
* Game reset

---

# 🔮 Future Improvements

The project is designed to be extended over time.

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

### 🌐 Web Interface

* [ ] Improved animations
* [ ] Sound effects
* [ ] Dark / Light themes
* [ ] Advanced responsive design
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
* Exception handling
* Properties

### Software Engineering

* Project organization
* Separation of concerns
* Modular architecture
* Dependency management
* Virtual environments
* Documentation
* Git and GitHub

### Tools

* Git
* GitHub
* Streamlit
* Python packaging

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

If you find a bug or have an idea for a new feature:

1. Open an issue.
2. Describe the problem or proposed feature.
3. Create a new branch.
4. Make your changes.
5. Test your changes locally.
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
