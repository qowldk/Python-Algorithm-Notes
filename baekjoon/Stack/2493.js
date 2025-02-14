const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");


const N = parseInt(input[0]);
const tops = input[1].split(" ").map(Number);

const stack = [];
const answer = [];

for (let i = 0; i < N; i++) {
  while (stack.length && tops[stack[stack.length - 1]] < tops[i]) {
    stack.pop();
  }

  if (stack.length && tops[stack[stack.length - 1]] > tops[i]) {
    answer.push(stack[stack.length - 1] + 1);
  }

  if (stack.length == 0) {
    answer.push(0);
  }

  stack.push(i);
}

console.log(answer.join(" "));
