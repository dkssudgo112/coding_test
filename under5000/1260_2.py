
from queue import PriorityQueue

def bfs(graph, start):
    queue = list()
    visited = list()

    queue.append(start)
    while queue:

        a = queue.pop(0)
        
        if a not in visited:
            visited.append(a)
            if a in graph:
                queue.extend(graph[a])
    return visited

def dfs(graph, start):
    stack = [start]
    visited = []

    while stack:

        a = stack.pop()
        
        if a not in visited:
            visited.append(a)
            print(a)
            if a in graph:
                for neighbor in graph[a]:
                    if neighbor not in visited:
                        stack.append(neighbor)
                        dfs(graph, neighbor)
                



if __name__ == "__main__":
    graph ={}
    graph2 = {}
    n, m, v = map(int, input().split())
    for i in range(m):
        a, b = map(str, input().split())

        if not a in graph:
            graph[a] = list()
            graph[a].append(b)

            graph2[a] = list()
            graph2[a].append(b)
        else:
            graph[a].append(b)
            graph2[a].append(b)
            graph[a].sort()
            graph2[a].sort()
            print(graph)
        if not b in graph:
            graph[b] = list()
            graph[b].append(a)
            graph2[b] = list()
            graph2[b].append(a)
        else:
            graph[b].append(a)
            graph2[b].append(a)
            graph[b].sort()
            graph2[b].sort()

    l1 = dfs(graph,str(v))
    bfs(graph2, str(v))

    print(*l1)


