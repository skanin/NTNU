# TDT4136 Assignment 4 - Solving Constraint Satisfaction Problems

## Sudoku Solutions

### Easy

```
############## Sudoku easy ##############
7 8 4 | 9 3 2 | 1 5 6
6 1 9 | 4 8 5 | 3 2 7
2 3 5 | 1 7 6 | 4 8 9
------+-------+------
5 7 8 | 2 6 1 | 9 3 4
3 4 1 | 8 9 7 | 5 6 2
9 2 6 | 5 4 3 | 8 7 1
------+-------+------
4 5 3 | 7 2 9 | 6 1 8
8 6 2 | 3 1 4 | 7 9 5
1 9 7 | 6 5 8 | 2 4 3
Backtrack was called 1 times and failed 0 times
```

### Medium

```
############# Sudoku medium #############
8 7 5 | 9 3 6 | 1 4 2
1 6 9 | 7 2 4 | 3 8 5
2 4 3 | 8 5 1 | 6 7 9
------+-------+------
4 5 2 | 6 9 7 | 8 3 1
9 8 6 | 4 1 3 | 2 5 7
7 3 1 | 5 8 2 | 9 6 4
------+-------+------
5 1 7 | 3 6 9 | 4 2 8
6 2 8 | 1 4 5 | 7 9 3
3 9 4 | 2 7 8 | 5 1 6
Backtrack was called 3 times and failed 0 times
```

<div style="page-break-after: always;"></div>

### Hard

```
############## Sudoku hard ##############
1 5 2 | 3 4 6 | 8 9 7
4 3 7 | 1 8 9 | 6 5 2
6 8 9 | 5 7 2 | 3 1 4
------+-------+------
8 2 1 | 6 3 7 | 9 4 5
5 4 3 | 8 9 1 | 7 2 6
9 7 6 | 4 2 5 | 1 8 3
------+-------+------
7 9 8 | 2 5 3 | 4 6 1
3 6 5 | 9 1 4 | 2 7 8
2 1 4 | 7 6 8 | 5 3 9
Backtrack was called 12 times and failed 4 times
```

### Very hard

```
############ Sudoku very hard ############
4 3 1 | 8 6 7 | 9 2 5
6 5 2 | 4 9 1 | 3 8 7
8 9 7 | 5 3 2 | 1 6 4
------+-------+------
3 8 4 | 9 7 6 | 5 1 2
5 1 9 | 2 8 4 | 7 3 6
2 7 6 | 3 1 5 | 8 4 9
------+-------+------
9 4 3 | 7 2 8 | 6 5 1
7 6 5 | 1 4 3 | 2 9 8
1 2 8 | 6 5 9 | 4 7 3
Backtrack was called 68 times and failed 57 times
```

It makes sense that backtrack was called increasing number of times as the sudoku boards grew harder. This is because there are more legal moves to do at the start and a guess are then more likely to be wrong.

The easy sudoku called backtrack only once, and failed 0 times. This is because one call on inference was enough to make all arcs consistent.

The medium board called backtrack three times, but still failed zero. This is again because the board are still relatively easy, and the algorithm only needed to "guess" what number to put 2 times (it tried with a number, found that a constaint was broken, backtracked and guessed a new number to put). Since it failed zero times, all guesses was correct.

The hard board had to do 11 guesses (backtrackings) and failed 4 times. This means that out of those 11 guesses, 4 was wrong, and it had to remove this move for these variables, and keep on going.

The very hard sudoku called backtrack 68 times, and failed 57 of these. Why this is, I have explained above.
