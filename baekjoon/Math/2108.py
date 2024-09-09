from collections import deque
import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
arr = []

for _ in range(N) :
  n = int(input())
  arr.append(n)

arr.sort()

print(round(sum(arr)/N))
print(arr[N//2])

counter = Counter(arr).most_common()
if len(counter) > 1 and counter[0][1] == counter[1][1] :
  print(counter[1][0])
else :
  print(counter[0][0])

print(arr[N-1]- arr[0])
