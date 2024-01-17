import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

s = []

def dfs() :
  if len(s) == M :
    print(' '.join(map(str, s)))
    return
  
  for i in range(1, N + 1) :
    if arr[i-1] not in s :
      s.append(arr[i-1])
      dfs()
      s.pop()

dfs()
