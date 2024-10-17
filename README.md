# checkm8
Terminal Chess.

### 1. **Basic Moves**:
These are standard moves without capturing.

- **Pawn Moves**:
  1. **e2 e4**: Pawn moves two squares forward.
  2. **d2 d4**: Pawn moves two squares forward.
  3. **e2 e3**: Pawn moves one square forward.
  4. **d2 d3**: Pawn moves one square forward.

- **Knight Moves**:
  1. **g1 f3**: Knight moves from g1 to f3.
  2. **b1 c3**: Knight moves from b1 to c3.

- **Bishop Moves**:
  1. **f1 c4**: Bishop moves from f1 to c4 (typically).
  2. **c1 e3**: Bishop moves from c1 to e3.

- **Rook Moves**:
  1. **a1 a3**: Rook moves from a1 to a3.
  2. **h1 h3**: Rook moves from h1 to h3.

- **Queen Moves**:
  1. **d1 d4**: Queen moves from d1 to d4.
  2. **d1 h5**: Queen moves from d1 to h5.

- **King Moves**:
  1. **e1 e2**: King moves from e1 to e2.

---

### 2. **Capture Moves**:
Capturing means you take one of your opponent's pieces by landing on their square.

- **Pawn Captures**:
  1. **e4 d5**: Pawn captures a piece on d5.
  2. **d4 e5**: Pawn captures a piece on e5.

- **Knight Captures**:
  1. **f3 g5**: Knight captures a piece on g5.
  2. **c3 d5**: Knight captures a piece on d5.

- **Bishop Captures**:
  1. **c4 f7**: Bishop captures a piece on f7.
  2. **e3 d4**: Bishop captures a piece on d4.

- **Rook Captures**:
  1. **a3 a7**: Rook captures a piece on a7.
  2. **h3 h7**: Rook captures a piece on h7.

- **Queen Captures**:
  1. **d4 d5**: Queen captures a piece on d5.
  2. **h5 g7**: Queen captures a piece on g7.

- **King Captures**:
  1. **e2 d3**: King captures a piece on d3.

---

### 3. **Special Moves**:

- **Castling**:
  1. **Kingside Castling**:
     - White: **e1 g1** (King and rook move).
     - Black: **e8 g8**.
  2. **Queenside Castling**:
     - White: **e1 c1**.
     - Black: **e8 c8**.

- **Pawn Promotion**:
  - If a pawn reaches the opposite side of the board (8th rank for White, 1st rank for Black), it can be promoted:
    1. **e7 e8q**: Pawn promotes to a queen.
    2. **e7 e8r**: Pawn promotes to a rook.
    3. **e7 e8b**: Pawn promotes to a bishop.
    4. **e7 e8n**: Pawn promotes to a knight.

---

### 4. **Possible Moves from the Initial Position**:

If we start with the initial chess position, here’s the list of all possible **legal moves** you can make as White. At the start, White can move pawns and knights. These are the **legal moves** in **UCI format** from the initial position:

```
e2e3
e2e4
d2d3
d2d4
g1f3
g1h3
b1c3
b1a3
```

### Explanation:
- **e2e3, e2e4**: Move the pawn from e2 to e3 (1 square forward) or e4 (2 squares forward).
- **d2d3, d2d4**: Move the pawn from d2 to d3 or d4.
- **g1f3, g1h3**: Move the knight from g1 to f3 or h3.
- **b1c3, b1a3**: Move the knight from b1 to c3 or a3.

### How You Can "Play Better":
To improve your chess game against the AI:
1. **Control the Center**: Always try to place your pawns and pieces in the center of the board early (e.g., e4, d4).
2. **Develop Your Pieces**: Move your knights and bishops out early to active positions (e.g., g1 f3 or f1 c4).
3. **Castle Early**: Safeguard your king by castling as soon as possible.
4. **Watch for Captures**: Try to capture your opponent’s pieces if they leave them unprotected. For example, move a knight or pawn to take an opponent’s piece.

---
