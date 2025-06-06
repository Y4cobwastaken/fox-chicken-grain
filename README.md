# Fox, Chicken, and Grain River Crossing Puzzle

## Overview

This program simulates the classic fox, chicken, and grain river crossing puzzle.  
A farmer needs to carry a fox, a chicken, and a bag of grain across a river using a rowboat.  
The boat can only carry the farmer and one item at a time. The challenge is to transport all safely without the fox eating the chicken or the chicken eating the grain.

---

## How the Program Works

- Four variables represent the position of the fox, chicken, grain, and farmer:
  - `0` means the item is on the starting side (near side) of the river.
  - `1` means the item is on the far side of the river.

- The user inputs which item they want to take across the river each turn:  
  `fox`, `chicken`, `grain`, or `farmer`.

- The program updates the positions if the move is valid (the farmer and item are on the same side).

- It then prints the current state of both sides of the river, showing who is where.

- The program checks if a wrong move has happened (fox eats chicken or chicken eats grain) on either side and ends if so.

- The game continues until the user successfully moves all three items across safely.

---

## Explanation of Key Functions

### Grouping()

This function uses the Python built-in `enumerate` function to check the positions of each item (`fox`, `chicken`, `grain`, `farmer`):

- `enumerate` lets you loop over a list while keeping track of each item's index and value.

- It creates two lists:
  - `positions1` for items on the far side (`value == 1`)
  - `positions0` for items on the near side (`value == 0`)

These lists are used to display which items are on each side of the river.

---

### puzzle_solved()

Checks if the puzzle is solved by verifying that all three items (`fox`, `chicken`, and `grain`) are on the far side (`value == 1`). Returns `True` if solved, otherwise `False`.

---

### wrong_move()

Checks whether the current state is losing by seeing if:

- The fox and chicken are alone on the same side without the farmer.
- The chicken and grain are alone on the same side without the farmer.

It checks both sides of the river. Returns `(True, message)` if lost, or `(False, "")` if safe.

---

### Output()

Displays the current situation, printing what items are on each side of the river. If the game is lost, it also prints the reason why (e.g., "The fox ate the chicken.").

---

### Understanding `enumerate`

The Python built-in function `enumerate` is used to loop over a list **while keeping track of both the index and the value** of each item.

Normally, when you loop over a list like this:

```python
for item in some_list:
    print(item)
```

You only get the item itself, but not its position in the list.

Using enumerate, you get both the index (position) and the value like this:

```python
for index, value in enumerate(some_list):
    print(f"Index: {index}, Value: {value}")
```

In the program, enumerate is used in the Grouping() function to check the positions of the fox, chicken, grain, and farmer. It loops through their position values (0 or 1) and collects the indexes of items on each side of the river.

For example:

```python
for index, value in enumerate([fox, chicken, grain, farmer]):
    if value == 1:
        positions1.append(index)  # Item on the far side
    elif value == 0:
        positions0.append(index)  # Item on the near side
```

This way, the program keeps track of which items are on each side by their indexes, which can then be matched to their names for displaying the current state of the game.


---

## How to Solve the Puzzle

The key challenge is to avoid leaving the fox alone with the chicken, or the chicken alone with the grain, on either side without the farmer.

A common solution pattern is:

1. Take the **chicken** across first.
2. Return alone to the original side.
3. Take the **fox** across next.
4. Bring the **chicken** back to the original side.
5. Take the **grain** across.
6. Return alone to the original side.
7. Finally, take the **chicken** across again.

This way, you never leave incompatible pairs alone without the farmer.

---

## Running the Program

Run the program and follow the prompts:

A fox, chicken and a bag of grain wait by the side of a river.

Which item will you take in your rowboat to the other side?

fox, chicken, grain or farmer?

Choose:


Type the name of the item you want to move (or `farmer` to move alone), and press Enter.

The program will show the state of the river after each move and notify you if you lose or when you solve the puzzle.

---

Good luck and enjoy solving the puzzle!