from sys import stdin
from collections import deque

def bfs(i, j, apart):
    n = len(apart)
    q = deque()
    q.append((i, j))
    apart[i][j] = 0
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <n and 0 <= ny <n:
                if apart[nx][ny] == 1:
                    q.append((nx, ny))
                    apart[nx][ny] = 0
                    cnt += 1
    return cnt

n = int(stdin.readline())
apart = []
result = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(n):
    apart.append(list(map(int, stdin.readline().strip())))
    
for i in range(n):
    for j in range(n):
        if apart[i][j] == 1:
            result.append(bfs(i, j, apart))
            
result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])