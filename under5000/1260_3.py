def BFS(V, node, visited):
    visited[V] = 1
    print(V, end=' ')
    queue = [V]

    while(queue):
        a = queue.pop(0)
        for i in node[a]:
            if visited[i] == 0:
                visited[i] = 1
                print(i, end=' ')
                queue.append(i)

def DFS(V, node, visited):
    visited[V] = 1
    print(V, end=' ')
    for i in node[V]:
        if visited[i] == 0:
            DFS(i, node, visited)


if __name__ == "__main__":

    N, M, V = map(int, input().split())
    node =[[]for i in range(N+1)]
    visited = [0]*(N+1)
    dfs = []
    bfs = []

    for i in range(M):
        a, b = map(int, input().split())
        node[a].append(b)
        node[b].append(a)

    for j in range(N+1):
        node[j].sort()

    DFS(V, node, visited)

    for i in range(N+1):
        visited[i] = 0 
    print()
    BFS(V, node, visited)