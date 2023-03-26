
def bfs(graph, start):
    queue = list()
    visited = list()

    queue.append(start)
    while queue:
        print(queue)
        a = queue.pop(0)
        if a not in visited:
            visited.append(a)
            if a in graph:
                queue.extend(graph[a])


    return visited

def dfs(graph, start):
    queue = list()
    visited = list()

    queue.append(start)
    while queue:

        a = queue.pop(0)
        if a not in visited:
            
            visited.append(a)
            if a in graph:
                graph[a].extend(queue)
                queue= (graph[a])

    return visited


if __name__ == "__main__":
    graph ={}
    graph2 = {}
    n, m, v = map(int, input().split())
    for i in range(m):
        a, b = map(str, input().split())
        print(a,b)
        if not a in graph:
            graph[a] = list(b)
            print(graph[a])
            graph2[a] = list(b)
        else:
            graph[a].append(b)
            graph2[a].append(b)
            graph[a].sort()
            graph2[a].sort()
        if not b in graph:
            graph[b] = list(a)
            graph2[b] = list(a)
        else:
            graph[b].append(a)
            graph2[b].append(a)
            graph[a].sort()
            graph2[a].sort()

    l1 = dfs(graph,str(v))
    l2 = bfs(graph2, str(v))

    print(*l1)


    print(*l2)

