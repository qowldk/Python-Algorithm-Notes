temp = []

def dfs() :
    global max_val

    if len(temp) == N :
        total = 0
        for i in range(N-1) :
            total += abs(temp[i] - temp[i+1])
        max_val = max(total, max_val)
        return 

    for i in range(N) :
        if not check[i] :
            check[i] = True
            temp.append(arr[i])
            dfs()
            temp.pop()
            check[i] = False


N = int(input())
arr = list(map(int, input().split()))
check = [False] * N

max_val = 0
dfs()
print(max_val)
