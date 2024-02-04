import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
from collections import deque

def dfs(R) :
  visited2[R] = 1
  print(R, end=" ")
  for x in arr[R] :
    if visited2[x] == 0 :
      dfs(x)

def bfs(R) :
  visited[R] = 1
  print(R, end=" ")
  queue.append(R)
  while queue :
    u = queue.popleft()
    for x in arr[u] :
      if visited[x] == 0 :
        visited[x] = 1
        print(x, end=" ")
        queue.append(x)

N, M, R = map(int, input().split())

arr = [[] for i in range(N+1)]
visited = [0] * (N+1)
visited2 = [0] * (N+1)
queue = deque([])

for i in range(M) :
  u, v = map(int, input().split())
  arr[u].append(v)
  arr[v].append(u)

for i in range(N+1) :
  arr[i].sort()

dfs(R)
print()
bfs(R)
