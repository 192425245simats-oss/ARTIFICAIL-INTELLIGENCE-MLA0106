from collections import deque

def bfs(graph, start):
    q = deque([start])
    visited = set([start])
    result = []
    while q:
        node = q.popleft()
        result.append(str(node))
        for i in graph[node]:
            if i not in visited:
                visited.add(i)
                q.append(i)
    return " ".join(result)

g1 = {1:[2,7],2:[3,6],3:[4,5],4:[],5:[9],6:[],7:[8,10],8:[],9:[],10:[]}

g2 = {'A':['B','C'],'B':['D','E'],'C':['F','G'],
      'D':[],'E':[],'F':[],'G':[]}


g3 = {0:[1],1:[2],2:[3,4],3:[5],4:[5],5:[7],
      6:[4],7:[6]}


g4 = {1:[2,3],2:[5,6],3:[4,7],4:[8],
      5:[],6:[],7:[8],8:[]}

print("BFS Graph1:", bfs(g1,1))
print("BFS Graph2:", bfs(g2,'A'))
print("BFS Graph3:", bfs(g3,0))
print("BFS Graph4:", bfs(g4,1))
