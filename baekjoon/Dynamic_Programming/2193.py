N = int(input())

arr = [[0] * 2 for _ in range(N+2)]
arr[1][1] = 1
arr[2][0] = 1

for i in range(3, N+1) :
    arr[i][0] = arr[i-1][1] + arr[i-1][0]
    arr[i][1] = arr[i-1][0]
    
print(arr[N][0] + arr[N][1])
    
