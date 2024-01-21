N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

visited = [False] * N 
s = set()
temp = []

def dfs() :
  global temp
  if len(temp) == M :
    s.add(tuple(temp))
    return

  for i in range(N) :
    if not visited[i] :
      temp.append(arr[i])
      visited[i] = True
      dfs()
      temp.pop()
      visited[i] = False

dfs()

for result in sorted(s) :
  print(*result)
