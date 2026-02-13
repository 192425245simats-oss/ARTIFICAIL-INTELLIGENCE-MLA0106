def alphabeta(tree,depth,alpha,beta,maximizing):
    if depth==0 or not isinstance(tree,list):
        return tree
    if maximizing:
        v=float('-inf')
        for child in tree:
            v=max(v,alphabeta(child,depth-1,alpha,beta,False))
            alpha=max(alpha,v)
            if beta<=alpha:
                break
        return v
    else:
        v=float('inf')
        for child in tree:
            v=min(v,alphabeta(child,depth-1,alpha,beta,True))
            beta=min(beta,v)
            if beta<=alpha:
                break
        return v

tree=[[[3,5],[6,9]],[[1,2],[0,-1]]]
print(alphabeta(tree,3,float('-inf'),float('inf'),True))
