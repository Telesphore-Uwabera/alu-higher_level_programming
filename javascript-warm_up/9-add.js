#!/usr/bin/node

function add (a, b) {
  const sum = a + b;
  console.log(sum);
}

const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

add(arg1, arg2);
