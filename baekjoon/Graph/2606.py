import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
network = int(input())

arr = [[] for i in range(N+1)]
visited = [0 for i in range(N+1)]

for i in range(network) :
  u, v = map(int, input().split())
  arr[u].append(v)
  arr[v].append(u)

def bfs(R) :
  global cnt
  visited[R] = 1
  queue.append(R)
  while queue :
    u = queue.popleft()
    for x in arr[u] :
      if visited[x] == 0 :
        cnt += 1
        visited[x] = 1
        queue.append(x)

cnt = 0
queue = deque([])
bfs(1)

print(cnt)
