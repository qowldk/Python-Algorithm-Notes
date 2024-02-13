N = int(input())

graph = []
for i in range(N) :
  graph.append(list(map(int, input())))

cnt = []
nums = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y) :
  global nums
  nums += 1
  graph[x][y] = 0
  for i in range(4) :
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >= 0 and nx < N and ny >= 0 and ny < M and graph[nx][ny] == 1 :
      dfs(nx, ny)

for i in range(N) :
  for j in range(N) :
    if graph[i][j] == 1 :
      dfs(i, j)
      cnt.append(nums)
      nums = 0

cnt.sort()
print(len(cnt))
for i in range(len(cnt)) :
  print(cnt[i])
