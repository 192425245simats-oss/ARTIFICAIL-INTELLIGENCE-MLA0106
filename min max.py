def minimax(t,m):
    if not isinstance(t,list):
        return t
    if m:
        return max(minimax(c,False) for c in t)
    else:
        return min(minimax(c,True) for c in t)

tree=[[[8,3],[5,9]],[[0,1],[4,5]]]
print(minimax(tree,True))
