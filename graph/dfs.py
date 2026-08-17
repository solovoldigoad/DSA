class Solution:
    # Function to perform DFS traversal
    def dfs(self, v, adj, visited, result):
        # Mark current node as visited
        visited[v] = True

        # Store node in result
        result.append(v)

        # Traverse all neighbours
        for u in adj[v]:
            if not visited[u]:
                self.dfs(u, adj, visited, result)


def main():
    # Number of vertices
    V = 5

    # Adjacency list
    adj = [[] for _ in range(V)]
    adj[0] = [1, 2]
    adj[1] = [0, 3]
    adj[2] = [0, 4]
    adj[3] = [1]
    adj[4] = [2]

    # Visited array
    visited = [False] * V

    # Result list
    result = []

    # Create object
    sol = Solution()

    # Run DFS from node 0
    sol.dfs(0, adj, visited, result)

    # Print traversal
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
