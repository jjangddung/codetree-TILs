n,m = map(int , input().split())



graph = [[] for _ in range(n+1)]

visited = [False for _ in range(n+1)]



for _ in range(m) :
    start, end = map(int, input().split())

    graph[start].append(end)
    graph[end].append(start)

root_vertex = 1

count = 0


def dfs(vertex) :
    global count
    for curr_v in graph[vertex] :
        if not visited[curr_v] :
            count +=1
            visited[curr_v] = True
            dfs(curr_v)


root_vertex = 1
# print(root_vertex)
visited[root_vertex] = True
dfs(root_vertex)
print(count)