from copy import deepcopy

ALIVE = 1
DEAD = 0

class LifeBoard:
    """Fixed-size Game of Life board."""
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[DEAD for _ in range(cols)] for _ in range(rows)]

    # -------------------------
    # Setup helpers
    # -------------------------
    def clear(self):
        self.grid = [[DEAD for _ in range(self.cols)] for _ in range(self.rows)]

    def set_cells(self, live_cells):
        """live_cells: iterable of (r, c) tuples inside bounds."""
        self.clear()
        for r, c in live_cells:
            if 0 <= r < self.rows and 0 <= c < self.cols:
                self.grid[r][c] = ALIVE

    def place_pattern(self, top, left, pattern):
        """
        pattern: list of strings ('.#' or 'O .' style). Non-dot/space counts as alive.
        Example:
            pattern = [
              ".#.",
              ".#.",
              ".#."
            ]
        """
        for dr, row in enumerate(pattern):
            for dc, ch in enumerate(row):
                r, c = top + dr, left + dc
                if 0 <= r < self.rows and 0 <= c < self.cols:
                    self.grid[r][c] = ALIVE if ch not in ('.', ' ', '0') else DEAD

    # -------------------------
    # Game logic
    # -------------------------
    def neighbors(self, r, c):
        cnt = 0
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                rr, cc = r + dr, c + dc
                # Fixed borders: off-grid counts as DEAD (ignored)
                if 0 <= rr < self.rows and 0 <= cc < self.cols:
                    cnt += self.grid[rr][cc] == ALIVE
        return cnt

    def step(self):
        """Advance one generation and return True if anything changed."""
        nxt = deepcopy(self.grid)
        changed = False

        for r in range(self.rows):
            for c in range(self.cols):
                n = self.neighbors(r, c)
                if self.grid[r][c] == ALIVE:
                    if n < 2 or n > 3:
                        nxt[r][c] = DEAD
                        changed = True
                else:
                    if n == 3:
                        nxt[r][c] = ALIVE
                        changed = True
        self.grid = nxt
        return changed

    def is_empty(self):
        return all(cell == DEAD for row in self.grid for cell in row)

    # -------------------------
    # Display
    # -------------------------
    def __str__(self):
        # Pretty print: alive = '■', dead = '·'
        return "\n".join(
            "".join('■' if cell == ALIVE else '·' for cell in row)
            for row in self.grid
        )

class LifeGame:
    """Runner for the fixed-size board."""
    def __init__(self, rows=20, cols=40):
        self.board = LifeBoard(rows, cols)

    def run(self, generations=50, stop_when_static=True, show=True):
        """
        Run for N generations or until static/extinct (if stop_when_static=True).
        """
        last_snapshot = None
        for gen in range(generations):
            if show:
                print(f"\nGeneration {gen}")
                print(self.board)

            changed = self.board.step()

            # Stop conditions
            if stop_when_static:
                snap = tuple(tuple(row) for row in self.board.grid)
                if not changed or snap == last_snapshot or self.board.is_empty():
                    if show:
                        print(f"\nStopped at generation {gen+1} (static/empty).")
                        print(self.board)
                    break
                last_snapshot = snap

# -------------------------
# Demo: a few classic patterns
# -------------------------
if __name__ == "__main__":
    game = LifeGame(rows=15, cols=30)

    # Choose an initial state by uncommenting one:

    # 1) Still life: Block (stays forever)
    # pattern = [
    #   "##",
    #   "##"
    # ]
    # game.board.place_pattern(5, 5, pattern)

    # 2) Oscillator: Blinker (period 2)
    # pattern = [
    #   ".#.",
    #   ".#.",
    #   ".#."
    # ]
    # game.board.place_pattern(5, 10, pattern)

    # 3) Glider (moves diagonally; fixed borders will eventually clip it)
    pattern = [
      ".#.",
      "..#",
      "###"
    ]
    game.board.place_pattern(2, 2, pattern)

    # 4) Lightweight spaceship (LWSS) – wider pattern
    # pattern = [
    #   ".#..#",
    #   "....#",
    #   "#...#",
    #   "..###"
    # ]
    # game.board.place_pattern(6, 10, pattern)

    game.run(generations=200, stop_when_static=False, show=True)



from collections import Counter

class SparseLife:
    """
    Sparse (infinite-ish) Game of Life using a set of live cells.
    Borders expand naturally; we just cap coordinates to +/- MAX_COORD
    to avoid runaway memory issues.
    """
    NEI = [(dx, dy) for dx in (-1,0,1) for dy in (-1,0,1) if not (dx==0 and dy==0)]

    def __init__(self, live_cells=None, max_coord=10_000):
        self.live = set(live_cells or [])
        self.max = max_coord

    def step(self):
        counts = Counter()
        # Count neighbors of every live cell and its neighbors
        for (x, y) in self.live:
            for dx, dy in self.NEI:
                counts[(x+dx, y+dy)] += 1

        nxt = set()
        # Apply rules
        for cell, n in counts.items():
            # Birth
            if n == 3 and cell not in self.live:
                if self._in_bounds(cell):
                    nxt.add(cell)
        for cell in self.live:
            n = counts.get(cell, 0)
            # Survival
            if n in (2, 3):
                if self._in_bounds(cell):
                    nxt.add(cell)

        changed = (nxt != self.live)
        self.live = nxt
        return changed

    def _in_bounds(self, cell):
        x, y = cell
        return -self.max <= x <= self.max and -self.max <= y <= self.max

    def bbox(self, pad=1):
        if not self.live:
            return (0, 0, 0, 0)
        xs = [x for x, _ in self.live]
        ys = [y for _, y in self.live]
        return (min(xs)-pad, min(ys)-pad, max(xs)+pad, max(ys)+pad)

    def __str__(self):
        if not self.live:
            return "(empty)"
        x0, y0, x1, y1 = self.bbox()
        # Safety cap on printed size
        if (x1-x0+1) * (y1-y0+1) > 2000:
            return f"(too big to print: {x1-x0+1}x{y1-y0+1} area)"
        rows = []
        for y in range(y0, y1+1):
            row = []
            for x in range(x0, x1+1):
                row.append('■' if (x, y) in self.live else '·')
            rows.append("".join(row))
        return "\n".join(rows)

# -------------------------
# Demo: Sparse glider
# -------------------------
if __name__ == "__main__":
    # Coordinates (x, y), y grows downward for printing convenience
    glider = {(1,0), (2,1), (0,2), (1,2), (2,2)}
    life = SparseLife(glider)

    for gen in range(40):
        print(f"\n[Sparse] Generation {gen}")
        print(life)
        life.step()
