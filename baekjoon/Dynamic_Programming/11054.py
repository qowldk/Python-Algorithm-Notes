N = int(input())
lst = [0] + list(map(int, input().split()))
lst_r = [0] + lst[::-1]

dp = [0] * (N+1)
dp2 = [0] * (N+1)
result = [0] * (N+1)

for i in range(1, N+1) :
  mx = 0
  for j in range(0, i) :
    if lst[i] > lst[j] :
      mx = max(mx, dp[j])
  dp[i] = mx + 1

for i in range(1, N+1) :
  mx = 0
  for j in range(0, i) :
    if lst_r[i] > lst_r[j] :
      mx = max(mx, dp2[j])
  dp2[i] = mx + 1

for i in range(1, N+1) :
  result[i] = dp[i] + dp2[N-i+1] - 1

print(max(result))
