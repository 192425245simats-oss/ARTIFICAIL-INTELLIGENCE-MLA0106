from collections import deque

def water_jug_12_8_5():
    visited = set()
    q = deque([(12, 0, 0)])  # (12L, 8L, 5L)

    while q:
        a, b, c = q.popleft()

        if a == 6 and b == 6:
            print("Solution Found:", (a, b, c))
            return

        if (a, b, c) in visited:
            continue
        visited.add((a, b, c))

        capacities = (12, 8, 5)
        jugs = [a, b, c]

        # Try pouring from i → j
        for i in range(3):
            for j in range(3):
                if i != j:
                    new = list(jugs)
                    pour = min(jugs[i], capacities[j] - jugs[j])
                    new[i] -= pour
                    new[j] += pour
                    q.append(tuple(new))

water_jug_12_8_5()
