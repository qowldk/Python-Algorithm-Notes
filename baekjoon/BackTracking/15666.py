N, M = map(int, input().split())
nums = set(map(int, input().split()))
nums = sorted(list(nums))

def dfs(start) :
    if len(s) == M :
        print(*s)
    else :
        for i in range(start, len(nums)) :
            s.append(nums[i])
            dfs(i)
            s.pop()

s = []
dfs(0)
