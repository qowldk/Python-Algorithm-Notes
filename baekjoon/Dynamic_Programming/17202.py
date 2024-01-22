A = list(map(int, input()))
B = list(map(int, input()))

arr = []
for i in range(16) :
  if i%2 == 0 :
    arr.append(A[i//2])
  else : arr.append(B[i//2])

end = 15
while end != 1 :
  for i in range(end) :
    arr[i] = (arr[i] + arr[i+1]) % 10
  end -= 1

print(arr[0], arr[1], sep='')
