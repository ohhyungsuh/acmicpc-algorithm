n = int(input())
map = [list(map(int, input())) for _ in range(n)]
result = ""

def check(x, y, size):
    v = map[x][y]
    
    for i in range(x, x+size):
        for j in range(y, y+size):
            if map[i][j] != v:
                return False
    return True

def resize(x, y, size):
    global result
    if check(x, y, size):
        result += str(map[x][y])
        return

    result += "("
    
    size = size // 2
    resize(x, y, size)
    resize(x, y+size, size)
    resize(x+size, y, size)
    resize(x+size, y+size, size)
    
    result += ")"
    
resize(0, 0, n)
print(result)