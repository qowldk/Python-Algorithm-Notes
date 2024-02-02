def dfs(R) :
  global cnt
  visited[R] = cnt
  for x in arr[R] :
    if visited[x] == 0 :
      cnt += 1
      dfs(x)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N, M, R = map(int, input().split())

arr = [[] for i in range(N+1)] 
visited = [0] * (N+1)
cnt = 1

for i in range(M) :
  u, v = map(int, input().split())
  arr[u].append(v)
  arr[v].append(u)

for i in range(N+1) :
  arr[i].sort(reverse=True)

dfs(R)

for i in range(1, len(visited)) :
  print(visited[i])
