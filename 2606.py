import sys

n = int(input())
m = int(input())

visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]
cnt = 0

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(v):
    global cnt
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            cnt += 1
    return cnt

print(dfs(1))