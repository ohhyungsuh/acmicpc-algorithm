from sys import stdin

n = int(stdin.readline())

stair = [0 for i in range(n+2)]
dp = [0 for i in range(n+2)]

for i in range(1, n+1):
    stair[i] = int(stdin.readline())

dp[0] = stair[0]
dp[1] = stair[1]
dp[2] = stair[1] + stair[2]

# for i in range(3, n):
#     dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])

for i in range(3, n+2):
    dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i]) 

print(dp[n])