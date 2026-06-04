from functions import addEdge
from collections import deque

def bfs01(adj):
    v = len(adj)
    visited  = [False] * v
    res = []

    src = 0
    q = deque()
    visited[src] = True
    q.append(src)

    while q:
        curr = q.popleft()
        res.append(curr)

        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)
    
    return res

if __name__ == "__main__":
    V = 5
    adj = []
    
    # creating adjacency list
    for i in range(V):
        adj.append([])
        
    addEdge(adj, 1, 2)
    addEdge(adj, 1, 0)
    addEdge(adj, 2, 0)
    addEdge(adj, 2, 3)
    addEdge(adj, 2, 4)

    res = bfs01(adj)

    for node in res:
        print(node, end=" ")

    print()