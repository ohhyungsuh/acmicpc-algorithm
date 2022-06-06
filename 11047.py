n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))
    
coins.sort(reverse=True)

ans = 0
for i in range(n):
    ans += k // coins[i]
    k = k % coins[i]

print(ans)