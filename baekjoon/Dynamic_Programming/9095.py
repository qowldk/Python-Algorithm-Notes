import sys
input = sys.stdin.readline

arr = [0, 1, 2, 4]
for i in range(4, 12) :
  arr.append(arr[i-1] + arr[i-2] + arr[i-3] )

T = int(input())
for _ in range(T) :
  n = int(input())
  print(arr[n])
