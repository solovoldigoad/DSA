from collections import deque

def bfs(graph, start):
    visited = set()
    q = deque([start])

    visited.add(start)

    while q:
        node = q.popleft()

        print(node)

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append(nei)