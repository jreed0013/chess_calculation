# Description:
Algorithm to estimate how many moves can be made in a single game of chess

# Process:
Finds the permutation of options when a certain amount of pieces ranging from 2-32 (min and max amount of pieces at one time in a game). Multiplies this number by the product of the amount of pieces available to move and an estimation of how many moves the average piece can make at any given point in a game of chess.

# ources of error in estimation:
- Does not account for moves that are not possible to make (ie. moving a king into checkmate)
- Assumes each piece can only move three different ways. I figured this was a safe estimation as pawns can only make 1 move (unless taking something) and most other pieces can make anywhere from 2-8 moves per turn (not counting displacement). Including displacement this number could be 16. This estimates pieces aside from pawns to have an average of 5 possible moves on any given turn. (unless there is an unbalanced number of pawns and non-pawns).