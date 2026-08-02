# Codebreaker 🔐

A command-line Mastermind-style code-breaking game built in Python. Crack the secret combination hidden in a locked treasure box using logic and the red/white pin clue system — with save and load support so you can pick up a game later.

## Story

While exploring campus, you discover a mysterious locked treasure box. It's protected by a complex password lock — only sharp logic and problem-solving can crack it open.

## Rules

- You get **10 guesses** to break the lock.
- Codes are **4, 5, or 6 digits** long, using only digits **0–5**.
- After each guess, you get clues in the form of red and white pins:
  - **Red pins** = digits that are correct *and* in the right position.
  - **White pins** = digits that are correct but in the wrong position.
  - Each digit in the code/guess is only counted once toward red or white.

## Features

- Randomly generated secret code (variable length: 4–6 digits)
- Guess history board showing all past guesses with red/white pin feedback
- Input validation (length, digit range, numeric-only checks)
- **Save/Load system** — save an in-progress game to one of 3 slots (with player name + timestamp) and resume it later
- Win/lose detection with themed treasure-box flavor text

## How to Play

\`\`\`bash
python codebreaker.py
\`\`\`

From the menu:
1. **Rules** — view the game rules
2. **New Game** — start a fresh game
3. **Load Game** — resume a previously saved game from one of 3 save slots
4. **Quit** — exit the program

During a game, enter your guess when prompted, or:
- `q` to quit without saving
- `s` to save your progress and quit

## Tech

Written in Python 3, using the standard library only (`random`, `os`, `datetime`).
