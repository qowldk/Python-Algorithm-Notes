N, K = map(int, input().split())
athletics = list(map(int, input().split()))
used = []
weight = 500
count = 0

def dfs() :
  if len(used) == N :
    global count
    count += 1
    return 

  for i in range(N) :
    global weight
    if (weight + athletics[i] - K) >= 500 and i not in used :
      weight += athletics[i] - K 
      used.append(i)
      dfs()
      weight = weight - athletics[i] + K
      used.pop()
dfs()
print(count)
