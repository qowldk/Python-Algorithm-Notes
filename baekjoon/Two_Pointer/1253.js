const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

const N = parseInt(input[0]);
const A = input[1].split(" ").map(Number);

let good_cnt = 0;

A.sort((a, b) => a - b);

for (let i = 0; i < N; i++) {
  let start = 0;
  let end = N - 1;
  const target = A[i];

  while (start < end) {
    if (A[start] + A[end] < target) {
      start++;
    } else if (A[start] + A[end] > target) {
      end--;
    } else {
      if (start != i && end != i) {
        good_cnt++;
        break;
      }
      if (start === i) {
        start++;
      } else {
        end--;
      }
    }
  }
}

console.log(good_cnt);
