from heapq import heappush, heappop

# Graph (node : [(neighbor, cost)])
graph = {
    'S': [('A', 3), ('D', 4)],
    'A': [('B', 4), ('D', 5)],
    'B': [('C', 4)],
    'D': [('E', 2)],
    'E': [('F', 4), ('B', 8)],
    'F': [('G', 3.5)],
    'C': [],
    'G': []
}

# Heuristic values h(n)
h = {
    'S': 11.5,
    'A': 10.1,
    'B': 8,
    'C': 3.4,
    'D': 9.2,
    'E': 7.1,
    'F': 3.5,
    'G': 0
}

def astar(start, goal):
    open_list = []
    heappush(open_list, (0, start))
    
    g = {start: 0}
    parent = {}

    while open_list:
        _, current = heappop(open_list)

        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1]

        for neighbor, cost in graph[current]:
            temp_g = g[current] + cost

            if neighbor not in g or temp_g < g[neighbor]:
                g[neighbor] = temp_g
                f = temp_g + h[neighbor]
                heappush(open_list, (f, neighbor))
                parent[neighbor] = current

    return None


# Run A*
path = astar('S', 'G')
print("Optimal Path:", path)
