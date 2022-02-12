from sys import stdin

def chk(x, y, n):
    color = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                chk(x, y, n//3)
                chk(x + n//3, y, n//3)
                chk(x + 2*n//3, y, n//3)
                chk(x, y + n//3, n//3)
                chk(x + n//3, y + n//3, n//3)
                chk(x + 2*n//3, y + n//3, n//3)
                chk(x, y + 2*n//3, n//3)
                chk(x + n//3, y + 2*n//3, n//3)
                chk(x + 2*n//3, y + 2*n//3, n//3)
                return
    if color == -1:
        whatPaper[0] += 1
    elif color == 0:
        whatPaper[1] += 1
    else:
        whatPaper[2] += 1
        
n = int(input())
whatPaper = [0, 0, 0]
paper = [list(map(int, stdin.readline().split())) for _ in range(n)]
chk(0, 0, n)
for i in range(3):
    print(whatPaper[i])


                        

