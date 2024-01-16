import sys
input = sys.stdin.readline

arr = [list(map(int, input().rstrip().split())) for _ in range(9) ]
blank = []

for i in range(9) :
  for j in range(9) :
    if arr[i][j] == 0 :
      blank.append((i,j))

def row_check(x, a) :
  for j in range(9) :
    if arr[x][j] == a :
      return False
  return True

def column_check(y, a) :
  for i in range(9) :
    if arr[i][y] == a :
      return False
  return True

def box_check(x, y, a) :
  nx = x // 3 * 3
  ny = y // 3 * 3

  for i in range(3) :
    for j in range(3) :
      if arr[nx + i][ny + j] == a :
        return False
  return True

def dfs(idx) :
  if idx == len(blank) :
    for i in range(9) :
      print(*arr[i])
    exit(0)

  for i in range(1, 10) :
    x = blank[idx][0]
    y = blank[idx][1]

    if row_check(x, i) and column_check(y, i) and box_check(x, y, i) :
      arr[x][y] = i
      dfs(idx+1)
      arr[x][y] = 0

dfs(0)
