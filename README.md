# 🎯 Number Guessing Game

A fun and interactive number guessing game built in Python, showcasing the evolution from procedural to object-oriented programming.

## 🎮 Game Overview

Guess the secret number between 1 and 100 in the minimum number of attempts! The computer will give you hints whether your guess is too high or too low.

```
  ____                       _____ _            _   _                 _               _ 
 / ___|_   _  ___  ___ ___  |_   _| |__   ___  | \ | |_   _ _ __ ___ | |__   ___ _ __| |
| |  _| | | |/ _ \/ __/ __|   | | | '_ \ / _ \ |  \| | | | | '_ ` _ \| '_ \ / _ \ '__| |
| |_| | |_| |  __/\__ \__ \   | | | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |  |_|
 \____|\__,_|\___||___/___/   |_| |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|  (_)   
----------------------------------------------------------------------------------------   
```

## 🚀 Features

- **Interactive Gameplay**: Clean command-line interface with visual feedback
- **Input Validation**: Handles invalid inputs gracefully
- **Attempt Tracking**: Keeps track of your guesses
- **Replay Option**: Play multiple rounds without restarting
- **Customizable Range**: Easy to modify the guessing range
- **ASCII Art**: Cool banner for enhanced user experience

## 📁 Project Structure

```
number-guessing-game/
├── guess.py              # Original procedural version
├── refactored_guess.py   # Object-oriented version
└── README.md            # Project documentation
```

## 🏃‍♂️ How to Run

### Prerequisites
- Python 3.6 or higher

### Running the Game
```bash
# Clone or download the project
cd "number guessing game"

# Run the original version
python guess.py

# Run the refactored OOP version
python refactored_guess.py
```

## 🎯 Gameplay

1. The computer randomly selects a number between 1-100
2. You enter your guess
3. The game tells you if your guess is too high, too low, or correct
4. Keep guessing until you find the secret number!
5. Try to minimize your attempts for a better score

### Example Gameplay
```
Guess: 50
Attempt: 1
Your guess is higher than the number | Try Again
----------------------------------------------------------------------------------------
Guess: 25
Attempt: 2
Your guess is lower than the number | Try Again
----------------------------------------------------------------------------------------
Guess: 37
Number Guessed Correctly! | Attempts: 3
```

## 📚 Learning Journey

This project represents my journey from **procedural programming** to **object-oriented programming (OOP)**. Here's what I learned:

### 🔄 From Procedural to OOP

#### **Original Approach (`guess.py`)**
- Linear, step-by-step execution
- Global variables for game state
- All logic in one main block
- Difficult to extend or maintain

#### **Refactored Approach (`refactored_guess.py`)**
- **Encapsulation**: Game state and logic contained within a class
- **Single Responsibility**: Each method has a specific purpose
- **Reusability**: Easy to create multiple game instances
- **Maintainability**: Clean, organized code structure

### 🧩 OOP Concepts Applied

| Concept | Implementation |
|---------|----------------|
| **Encapsulation** | All game data (secret number, attempts, game state) contained within the `GuessGame` class |
| **Abstraction** | Complex game logic hidden behind simple method calls |
| **Modularity** | Separate methods for different responsibilities |
| **Reusability** | `reset()` method allows multiple game sessions |

### 🏗️ Class Structure

```python
class GuessGame:
    def __init__(self, min_num=1, max_num=100)  # Initialize game state
    def welcome(self)                           # Display game banner
    def user_inp(self)                          # Handle user input & validation
    def check(self, guess)                      # Game logic & feedback
    def play(self)                              # Main game loop
    def reset(self)                             # Reset for new game
```

### 🎓 Key Learnings

1. **Code Organization**: OOP makes code more organized and readable
2. **Error Handling**: Implemented try-catch for input validation
3. **Method Responsibility**: Each method has a single, clear purpose
4. **State Management**: Better control over game state through class attributes
5. **Extensibility**: Easy to add new features like difficulty levels or scoring

## 🔧 Technical Details

### **Technologies Used**
- **Python 3.x**: Core programming language
- **random module**: For generating random numbers
- **Exception handling**: For input validation

### **Design Patterns**
- **Single Responsibility Principle**: Each method handles one aspect
- **Encapsulation**: Data and methods bundled together
- **Clean Code**: Readable method names and clear logic flow

## 🌟 Future Enhancements

- [ ] **Difficulty Levels**: Easy (1-50), Medium (1-100), Hard (1-500)
- [ ] **Score System**: Points based on number of attempts
- [ ] **Leaderboard**: Save and display high scores
- [ ] **Hint System**: Optional hints for struggling players
- [ ] **GUI Version**: Tkinter or PyQt interface
- [ ] **Multiplayer Mode**: Turn-based guessing with friends

**Made by Ayushh** | *Learning Python & OOP concepts one project at a time*

### 🏆 Skills Demonstrated
`Python` `OOP` `Class Design` `Error Handling` `Code Refactoring` `Clean Code` `Problem Solving`
