temp = []

def dfs(start) :
  if len(temp) == 6 :
    print(*temp)
    return
  
  for i in range(start, k) :
    temp.append(S[i])
    dfs(i+1)
    temp.pop()


while (True) :
  s = list(map(int, input().split()))
  k = s[0]
  if k == 0 :
    break
  S = s[1:]
  dfs(0)
  print()
