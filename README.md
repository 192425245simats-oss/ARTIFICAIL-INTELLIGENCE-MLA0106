min max 1
START
FUNCTION minimax(t, m)
    IF t is not a list THEN
        RETURN t
    ENDIF
    IF m = TRUE THEN
        RETURN maximum of minimax(child, FALSE) 
               for each child in t
    ELSE
        RETURN minimum of minimax(child, TRUE) 
               for each child in t
    ENDIF
END FUNCTION

SET tree = [[[8,3],[5,9]], [[0,1],[4,5]]]
PRINT minimax(tree, TRUE)
END


BFS
START
FUNCTION BFS(graph, start)
    CREATE queue and add start
    CREATE visited set and add start
    CREATE empty result list
    WHILE queue is not empty DO
        node ← remove front element from queue
        ADD node to result

        FOR each neighbor in graph[node] DO
            IF neighbor not in visited THEN
                ADD neighbor to visited
                ADD neighbor to queue
            ENDIF
        END FOR
    END WHILE
    RETURN result
END FUNCTION
CALL BFS for each graph and PRINT result
END


DFS
START
FUNCTION DFS(graph, node, visited, result)
    IF visited is empty THEN
        CREATE empty visited set
        CREATE empty result list
    ENDIF
    ADD node to visited
    ADD node to result
    FOR each neighbor in graph[node] DO
        IF neighbor not in visited THEN
            CALL DFS(graph, neighbor, visited, result)
        ENDIF
    END FOR
    RETURN result
END FUNCTION
CALL DFS for each graph and PRINT result
END


A**
START

FUNCTION A_STAR(start, goal)
    OPEN ← priority queue with (start)
    g[start] ← 0
    WHILE OPEN not empty
        current ← node with lowest f
        IF current = goal RETURN path using parents
        FOR each neighbor of current
            temp ← g[current] + cost
            IF neighbor not visited OR temp < g[neighbor]
                g[neighbor] ← temp
                f ← temp + heuristic[neighbor]
                ADD neighbor to OPEN
                parent[neighbor] ← current
        END FOR
    END WHILE
END

ALPHA BETA
START
FUNCTION ALPHABETA(node, depth, alpha, beta, isMax)
    IF depth = 0 OR node is a value THEN
        RETURN node
    ENDIF
    IF isMax = TRUE THEN
        value ← -∞
        FOR each child in node DO
            value ← MAX(value, ALPHABETA(child, depth-1, alpha, beta, FALSE))
            alpha ← MAX(alpha, value)
            IF beta ≤ alpha THEN BREAK   // Beta cut-off
        END FOR
        RETURN value
    ELSE
        value ← +∞
        FOR each child in node DO
            value ← MIN(value, ALPHABETA(child, depth-1, alpha, beta, TRUE))
            beta ← MIN(beta, value)
            IF beta ≤ alpha THEN BREAK   // Alpha cut-off
        END FOR
        RETURN value
    ENDIF
END FUNCTION
CALL ALPHABETA(tree, depth, -∞, +∞, TRUE)
PRINT result
END


WATER JUG
START
Insert (12,0,0) into queue Q
WHILE Q not empty
    Remove (a,b,c)
    IF (a=6 AND b=6) PRINT solution and STOP
    FOR each possible pour i → j
        Generate new state and add to Q if not visited
END WHILE
END


PROLOG


Facts & Rules

Define facts for male, female and parent relationships

Create rule: father(X,Y) if X is parent of Y and X is male

Create rule: mother(X,Y) if X is parent of Y and X is female

Return true if rule conditions satisfy

18) Family Tree

Define parent relationships

Create rule: grandparent(X,Y) if X is parent of Z

Check if Z is parent of Y

If both true, return true

19) Append Lists

If first list is empty, result is second list

Otherwise take head of first list

Recursively append tail with second list

Add head to result

20) Reverse List

If list is empty, return empty

Separate head and tail

Recursively reverse tail

Append head at end of reversed tail

21) Member

Check if element equals head of list

If yes, return true

Otherwise check in tail recursively

Stop when found or list ends

22) Length of List

If list is empty, length = 0

Otherwise ignore head

Recursively find length of tail

Add 1 to result

23) Concatenate

If first list empty, result is second list

Take head of first list

Recursively concatenate tail with second list

Add head to result

24) Delete Element

If head equals element, remove it

Return remaining tail

Otherwise keep head

Recursively delete from tail

25) Permutation

If list empty, permutation is empty

Select one element from list

Remove selected element

Recursively permute remaining elements

26) Subset

If subset list empty, return true

Take first element of subset

Check if it is member of main list

Recursively check remaining elements

27) Graph Path

Define edges between nodes

Path exists if direct edge present

Otherwise check intermediate node

Recursively search until destination found

28) Factorial

If N = 0, return 1

Otherwise reduce N by 1

Recursively compute factorial(N-1)

Multiply N with result

29) Fibonacci

If N = 0 return 0

If N = 1 return 1

Otherwise compute fib(N-1) and fib(N-2)

Add both results

30) Animal Classification

Define animal facts

Create rule: mammal(X) if X is animal

Check if given object matches rule

Return true if satisfied



