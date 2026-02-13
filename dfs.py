def dfs(graph, node, visited=None, result=None):
    if visited is None:
        visited = set()
        result = []
    visited.add(node)
    result.append(str(node))
    for i in graph[node]:
        if i not in visited:
            dfs(graph, i, visited, result)
    return " ".join(result)

g1 = {1:[2,7],2:[3,6],3:[4,5],4:[],5:[9],6:[],7:[8,10],8:[],9:[],10:[]}

g2 = {'A':['B','C'],'B':['D','E'],'C':['F','G'],
      'D':[],'E':[],'F':[],'G':[]}

g3 = {0:[1],1:[2],2:[3,4],3:[5],4:[5],5:[7],
      6:[4],7:[6]}

g4 = {1:[2,3],2:[5,6],3:[4,7],4:[8],
      5:[],6:[],7:[8],8:[]}

print("DFS Graph1:", dfs(g1,1))
print("DFS Graph2:", dfs(g2,'A'))
print("DFS Graph3:", dfs(g3,0))
print("DFS Graph4:", dfs(g4,1))
