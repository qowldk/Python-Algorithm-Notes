import sys
input = sys.stdin.readline

N = int(input())

nums = [1, 5, 10, 50]
temp = []
s = set()

def dfs(start) :
  if len(temp) == N :
    s.add(sum(temp))
    return

  for i in range(start, 4) :
    temp.append(nums[i])
    dfs(i)
    temp.pop()

dfs(0)
print(len(s))
