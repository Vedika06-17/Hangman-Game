# Hangman Game

## Introduction 🎮

This is a simple Hangman game implemented in Python. The game selects a random word from a predefined list, and the player has to guess the word by suggesting letters. The player has a total of six lives, which decrease each time they guess incorrectly. The game ends when the player either guesses the word correctly or loses all their lives.

---

## How the Code Works 📝

### 1. **Importing Required Modules** 📦

The `random` module is imported to allow the program to select a random word from the given list.

```python
import random
```

### 2. **Defining Word List and Art Assets** 🎨

The game uses a predefined word list and ASCII art for different hangman stages.

```python
word_list = ["aardvark", "baboon", "camel"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
...]  # (Other stages included in the full code)
```

A logo is also provided for better visual appeal.

### 3. **Initializing Game Variables** 🛠️

- `lives = 6` keeps track of the player’s remaining attempts.
- `chosen_word = random.choice(word_list)` selects a random word.
- `placeholder` is initialized with underscores (`_`) representing unguessed letters.

```python
lives = 6
chosen_word = random.choice(word_list)
placeholder = "_" * len(chosen_word)
```

### 4. **Game Loop (While Not Game Over)** 🔄

The game continues as long as the player has lives left and hasn’t guessed the word completely.

```python
while not game_over:
```

- The player is prompted to guess a letter:
  ```python
  guess = input("Letter to guess: ").lower()
  ```
- If the letter has already been guessed, a message is displayed.
- The guessed letter is checked against the word:
  - If correct, the placeholder updates with the letter.
  - If incorrect, the `lives` count decreases by 1.
  ```python
  if guess not in chosen_word:
      lives -= 1
      print(f"You guessed {guess}, that's not in the word. You lose a life.")
  ```

### 5. **Win or Lose Condition** 🏆❌

- If the player guesses all letters, they win:
  ```python
  if "_" not in display:
      game_over = True
      print("YOU WIN!")
  ```
- If `lives == 0`, they lose and the game ends:
  ```python
  if lives == 0:
      game_over = True
      print(f"The word was {chosen_word}. YOU LOSE!")
  ```

### 6. **Displaying Hangman Stages** 🎭

Depending on the number of lives remaining, the corresponding Hangman ASCII art is displayed.

```python
print(stages[lives])
```

---

## Features ✅

- Random word selection 🎲
- Case-insensitive letter guessing 🔠
- Lives tracking system ❤️
- ASCII art representation of Hangman 🎭
- User-friendly interface 🖥️

---

## How to Play 🕹️

1. Run the Python script.
2. The game will randomly choose a word.
3. Enter letters one by one to guess the word.
4. You have 6 lives—each incorrect guess reduces a life.
5. Win by guessing the word before losing all lives!

---

## Example Gameplay 🏁

```
****************************6/6 LIVES LEFT***********************************
Letter to guess: a
_a_a__
****************************6/6 LIVES LEFT***********************************
Letter to guess: e
_a_a_e
...
YOU WIN!
```

---

## Future Improvements 🚀

- Add a difficulty level system 🎚️
- Implement a graphical user interface (GUI) 🖥️
- Allow multiple rounds without restarting the script 🔁

---

## Conclusion 🎯

This project is a fun and interactive way to practice Python programming concepts such as loops, conditionals, lists, and user input handling. Hangman is a classic word-guessing game that enhances vocabulary while providing entertainment!

---

Enjoy playing! 🎉

