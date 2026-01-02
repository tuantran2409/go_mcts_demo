Monte Carlo Tree Search Demo for 5×5 Go
📌 Overview

This repository contains a simplified demonstration of the Monte Carlo Tree Search (MCTS) algorithm applied to a 5×5 Go board.
The project is developed for academic and educational purposes in an Artificial Intelligence course, focusing on illustrating the relationship between game theory and AI search algorithms.

The implementation does not aim to replicate the full rules or complexity of the standard Go game.

🎯 Objectives

Demonstrate the basic idea of Monte Carlo Tree Search

Illustrate decision-making in a two-player zero-sum game

Compare MCTS against a random-playing opponent

Provide a simple and runnable demo suitable for coursework and reports

🧠 Methodology

Board size: 5×5

Players:

Black: Monte Carlo Tree Search (MCTS)

White: Random move selection

The game model is simplified:

No capture rules

No territory scoring

The winner is determined based on predefined evaluation criteria

Multiple simulations are run to observe the performance of MCTS under different simulation counts.

🖥️ Output

The program prints experimental results directly to the console, including:

Number of simulations

Number of wins for MCTS

Number of wins for the random player

Number of draws

Example output:

Simulations: 100
MCTS wins  : 20
Random wins: 0
Draws     : 0

📂 Project Structure
go_mcts_demo/
├── main.py          # Entry point for running experiments
├── mcts.py          # MCTS-related logic (simplified)
├── game.py          # Go board and game state representation
└── README.md        # Project documentation


(File names may vary depending on implementation details.)

▶️ How to Run

Ensure Python 3 is installed

Clone or download this repository

Navigate to the project directory

Run:

python main.py

⚠️ Notes

This project uses a simplified Go model and does not implement the full rules of the game.

The purpose of this repository is demonstration and learning, not competitive gameplay.

Results such as consistent MCTS victories are expected due to the simplified environment and the use of a random opponent.

📘 Academic Context

This project accompanies a written report on:

Game Theory and Its Applications in Go Using Artificial Intelligence

and serves as a practical illustration of theoretical concepts discussed in the report.

📄 License

This project is intended for educational use only.
