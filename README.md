## Mars Rover
This is a Mars Rover script written in Python.

### Input required:
The script takes multi line user input with the following information:
- a grid size ( m x n where m is height and n is width)
- a single line of rover data:
    - coordinates (x, y)
    - orientation (N, E, S, W)
    - movements 'LRF'

This input  takes the format:
```
4 8
(2, 3, E) LFRFF
(0, 2, N) FFLFRFF
```

### What it does:
The script moves one or more robots around Mars.
- Each robot can move forward one space (F), rotate left by 90 degrees (L), or rotate
right by 90 degrees (R).
- If a robot moves off the grid, it is marked as ‘lost’ and its last valid grid position and
orientation is recorded.
- It outputs the final position

### Next Steps: 
- Write some tests
- Validation for user input
- refactor