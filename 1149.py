from sys import stdin

n = int(stdin.readline())

home = []

for _ in range(n):
    home.append(list(map(int, stdin.readline().split())))

for i in range(1, n):
    home[i][0] = min(home[i-1][1], home[i-1][2]) + home[i][0]
    home[i][1] = min(home[i-1][0], home[i-1][2]) + home[i][1]
    home[i][2] = min(home[i-1][0], home[i-1][1]) + home[i][2]

print(min(home[n-1][0], home[n-1][1], home[n-1][2]))