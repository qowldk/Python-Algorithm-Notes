n = int(input())

arr = [-1, -1, 1, -1, 2, 1, 3, 2, 4, 3, 2]
for i in range(11, n+1) :
  arr.append(arr[i-5] + 1)
print(arr[n])
