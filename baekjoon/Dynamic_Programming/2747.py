n = int(input())

arr = [0, 1]

def dp(n) :
  if n == 0 :
    return 0
  elif n == 1 :
    return 1
  else :
    for i in range(2, n+1) :
      arr.append(arr[i-1] + arr[i-2])
    return arr[n]

print(dp(n))
