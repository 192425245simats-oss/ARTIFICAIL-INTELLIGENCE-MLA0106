# Alpha-Beta Pruning implementation

def alphabeta(node, depth, alpha, beta, maximizingPlayer):
    
    # If leaf node (no children)
    if depth == 0 or not isinstance(node, list):
        return node
    
    if maximizingPlayer:
        maxEval = float('-inf')
        for child in node:
            eval = alphabeta(child, depth-1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            
            if beta <= alpha:   # Beta cut-off
                break
        return maxEval
    
    else:
        minEval = float('inf')
        for child in node:
            eval = alphabeta(child, depth-1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            
            if beta <= alpha:   # Alpha cut-off
                break
        return minEval


# Example Tree (like your image)
# Leaf values at bottom
tree = [
            [ [3, 3], [5, 9] ],
            [ [0, 1], [4, 5] ]
       ]

depth = 3
result = alphabeta(tree, depth, float('-inf'), float('inf'), True)

print("Optimal value:", result)
