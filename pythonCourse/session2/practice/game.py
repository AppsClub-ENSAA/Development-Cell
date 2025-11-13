#!/usr/bin/env python3
"""
🔁 Session 2 Challenge
🎮 Rock, Paper, Scissors

📚 Topics:
- Loops (for, while)
- Conditionals
- Random numbers
- Variables

🎯 Tasks:

1️⃣ **Play One Round**
   - Your goal is to make the game work for **a single round**.
   
   - Implement the code **after** `move_number = random.randint(1, 3)`.
   
   - Based on `move_number`, create a 'computer_move' variable to store the random choice :
     - If it's 1 → computer chooses Rock.
     - If it's 2 → computer chooses Paper.
     - If it's 3 → computer chooses Scissors.
     
   - Compare `player_move` and `computer_move`:
     - If they are the same → it's a tie.
     - Otherwise, decide who wins following these rules:
       - Rock beats Scissors
       - Scissors beat Paper
       - Paper beats Rock
   - 💬 Print clear results:
     - Example if it's a tie → `"It's a tie!"`
     - Example if you win → `"You win! "`
     - Example if you lose → `"You lose! "`

2️⃣ **Play 5 Rounds**
   - Make the player play **exactly 5 rounds**.
     ```

3️⃣ **Track Total Results**
   - Add three variables: `wins`, `losses`, and `ties` (start at 0).
   - Update them after each round.
 

"""

import random
import sys

print('ROCK, PAPER, SCISSORS')





while True:
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    player_move = input('> ').strip().lower()
    if player_move == 'q':
        sys.exit()
    if player_move in ['r', 'p', 's']:
        break
    print('Invalid Option!!. ')
    
    
if player_move == 'r':
    print('ROCK versus...')
elif player_move == 'p':
    print('PAPER versus...')
else:
    print('SCISSORS versus...')

move_number = random.randint(1, 3) 

# 🧠 TODO: Implement from here (Task 1)



