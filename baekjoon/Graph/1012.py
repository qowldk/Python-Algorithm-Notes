import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y) :
  graph[x][y] = 0 
  for i in range(4) :
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >= 0 and nx < N and ny >= 0 and ny <M and graph[nx][ny] == 1 :
      dfs(nx, ny)

T = int(input())

for i in range(T) :
  M, N, K = map(int, input().split())
  
  graph = [[0 for i in range(M)] for j in range(N)]
  for i in range(K) :
    u, v = map(int, input().split())
    graph[v][u] = 1

  cnt = 0 

  for i in range(N) :
    for j in range(M) :
      if graph[i][j] == 1 :
        dfs(i, j)
        cnt += 1

  print(cnt)
