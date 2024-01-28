n = int(input())

if n == 1 :
  print(1) 
elif n == 2 :
  print(2)
else : 
  arr = [0, 1, 2]
  for i in range(3, n+1) :
    arr.append(arr[i-1] + arr[i-2])
  print(arr[n] % 10007)
