from collections import deque

def water_jug_5_3():
    visited = set()
    q = deque([(0, 0)])  # (5L, 3L)

    while q:
        x, y = q.popleft()

        if x == 4:
            print("Solution Found:", (x, y))
            return

        if (x, y) in visited:
            continue
        visited.add((x, y))

        # Possible operations
        states = [
            (5, y),        # Fill 5L
            (x, 3),        # Fill 3L
            (0, y),        # Empty 5L
            (x, 0),        # Empty 3L
            (x - min(x, 3 - y), y + min(x, 3 - y)),  # Pour 5→3
            (x + min(y, 5 - x), y - min(y, 5 - x))   # Pour 3→5
        ]

        for state in states:
            if state not in visited:
                q.append(state)

water_jug_5_3()
