
# Rock, Paper, Scissors Game

## Overview
This project is a command-line implementation of the classic game **Rock, Paper, Scissors**. The game allows a user to play against the computer, where both the user and the computer make random choices, and the winner is determined based on the standard rules of the game. The game continues until either the user or the computer scores 5 points. The results are stored in a file called `result.txt` for reference.

---

## How to Play
1. **Start the Game**: When you run the script, it will read and display the results of previous games from `result.txt` (if it exists).
2. **User Input**: Enter your choice of `Rock`, `Paper`, or `Scissors` by typing `r`, `p`, or `s` respectively.
   - Input validation ensures that you can only provide valid options.
3. **Computer's Turn**: The computer will randomly choose one of the three options.
4. **Scoring**:
   - The user gains a point if their choice beats the computer's choice.
   - The computer gains a point if its choice beats the user's choice.
   - A tie results in no points for either side.
5. **Winning Condition**: The first to reach 5 points wins the game.
6. **Results**: The final scores are displayed and recorded in the `result.txt` file.

---

## Game Rules
- Rock beats Scissors.
- Scissors beat Paper.
- Paper beats Rock.

---

## File Structure
- **`game.py`**: The main Python script that runs the game.
- **`result.txt`**: A text file where the results of each game are saved.

---

## Installation
### Prerequisites
- Python 3.x installed on your system.

### Steps
1. Clone this repository or download the script.
2. Open a terminal and navigate to the directory containing `game.py`.
3. Run the script using the command:
   ```bash
   python game.py
   ```

---

## Code Explanation
The game is implemented using Python and follows a modular approach. Here's an overview of the key functions:

### **`intro()`**
Displays a welcome message introducing the game.

### **`begin_user()`**
Handles user input with validation to ensure valid choices (`r`, `p`, or `s`). Custom exceptions are used for invalid inputs.

### **`begin_ai()`**
Generates a random choice for the computer.

### **`process()`**
Implements the core game logic, including:
- Comparing user and computer choices.
- Updating scores.
- Looping until either the user or the computer scores 5 points.

### **`winner_and_loser()`**
Determines and announces the winner. Calls a nested function `results()` to save the scores in `result.txt`.

---

## Example Gameplay
```text
Previous Results:
User's Score: 5
Computer's Score: 3

Welcome to our game.
This is one of the most well-known games in the world.
---Rock, Paper, Scissors---
--------------------
Select between Rock, Paper, Scissors:(r/p/s) r
Your choice is Rock, Your rival's choice is Scissors.
You gained a score.
--------------------
User's score: 1
Computer's score: 0
...
Good job, you won the game!
```

---

## Contributions
Feel free to contribute to this project by submitting issues or pull requests. Suggestions for improvements, such as adding more features or refining the code, are always welcome.

---

## Future Enhancements
- Add support for multiplayer mode.
- Introduce graphical user interface (GUI).
- Implement advanced AI strategies for more challenging gameplay.
- Add difficulty levels (easy, medium, hard).
