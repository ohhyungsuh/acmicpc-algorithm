from sys import stdin
from collections import deque

def bfs():
    while q:
        x, y, z = q.popleft()
        
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and tomatoes[nz][nx][ny] == 0:
                q.append((nx, ny, nz))
                tomatoes[nz][nx][ny] = tomatoes[z][x][y] + 1



m, n, h = map(int, stdin.readline().split())
dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
tomatoes = []
q = deque()

for i in range(h):
    tm = [list(map(int, stdin.readline().split())) for _ in range(n)]
    tomatoes.append(tm)
    for j in range(n):
        for k in range(m):
            if tm[j][k] == 1:
                q.append((j, k, i)) # 행 열 높이

if len(q) == 0:
    print(-1)
    exit(0)
    
bfs()
result = 0
for h in tomatoes:
    for i in h:
        for j in i:
            if j == 0:
                print(-1)
                exit(0)
        result = max(result, max(i))
print(result-1)

