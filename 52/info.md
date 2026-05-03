# N-Queens Diagonal Trick: Why It Actually Works

For this problem, the diagonal formulas aren't just magic, they're based on actual coordinate geometry.

## The Setup

Take this 4x4 grid with row/column indices:

```
    0   1   2   3
 0  .   .   .   .
 1  .   .   .   .
 2  .   .   .   .
 3  .   .   .   .
```

## The Math Behind the Magic

### Why (row - col) for Positive Diagonals?

Positive diagonals go down-right (↘). Every square on the same diagonal maintains a constant difference between row and column. For every +1 in row, you get +1 in col:

Main diagonal:
- (0,0): 0 - 0 = 0
- (1,1): 1 - 1 = 0
- (2,2): 2 - 2 = 0
- (3,3): 3 - 3 = 0

Another diagonal:
- (0,2): 0 - 2 = -2
- (1,3): 1 - 3 = -2

See the pattern? All positions on the same positive diagonal share the same (row - col) value.

### Why (row + col) for Negative Diagonals?

Negative diagonals go down-left (↙). For every +1 in row, you get -1 in col. The sum stays constant:

- (0,3): 0 + 3 = 3
- (1,2): 1 + 2 = 3
- (2,1): 2 + 1 = 3
- (3,0): 3 + 0 = 3

## Visual Example

Place a queen at (1,1):

```
    0   1   2   3
 0  .   .   ×   .   <- (0,2): neg diag = 2
 1  .   Q   .   .   <- Queen at (1,1)
 2  ×   .   ×   .   <- (2,0): neg = 2, (2,2): pos = 0
 3  .   .   .   ×   <- (3,3): pos diag = 0
```

The queen at (1,1) attacks:
- Row 1 (all columns)
- Column 1 (all rows)
- Positive diagonal where (row - col) = 0: includes (0,0), (2,2), (3,3)
- Negative diagonal where (row + col) = 2: includes (0,2), (2,0)

## Why This Is Genius

1. **O(1) Diagonal Checks**: Instead of looping through the board to check diagonals, you just check if a value exists in a set.

2. **Natural Indexing**: For an n×n board:
   - Positive diagonals: indices range from -(n-1) to (n-1)
   - Negative diagonals: indices range from 0 to 2(n-1)
   - Total: 2n-1 diagonals of each type

3. **No Coordinate Storage**: You don't need to store actual (row,col) pairs - just their computed diagonal index.

## The Mathematical Foundation

This works because diagonal movement in a grid follows linear equations:
- Positive diagonal: y = x + c (slope = 1)
- Negative diagonal: y = -x + c (slope = -1)

The formulas (row - col) and (row + col) are rearrangements to isolate the constant `c` that defines each unique diagonal line.

