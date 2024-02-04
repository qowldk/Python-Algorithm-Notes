def bfs(R) :
  global cnt
  visited[R] = cnt
  queue.append(R)
  while queue :
    u = queue.popleft()
    for x in arr[u] :
      if visited[x] == 0 :
        cnt += 1
        visited[x] = cnt
        queue.append(x)

import sys
input = sys.stdin.readline
from collections import deque

N, M, R = map(int, input().split())

arr = [[] for i in range(N+1)] 
visited = [0] * (N+1)
cnt = 1
queue = deque([])

for i in range(M) :
  u, v = map(int, input().split())
  arr[u].append(v)
  arr[v].append(u)

for i in range(N+1) :
  arr[i].sort()

bfs(R)

for i in range(1, len(visited)) :
  print(visited[i])
