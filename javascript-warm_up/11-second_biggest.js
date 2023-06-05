#!/usr/bin/node

function findSecondBiggest (args) {
  if (args.length <= 1) {
    return 0;
  }

  let biggest = Number.MIN_SAFE_INTEGER;
  let secondBiggest = Number.MIN_SAFE_INTEGER;

  for (let i = 0; i < args.length; i++) {
    const num = parseInt(args[i]);
    if (!isNaN(num)) {
      if (num > biggest) {
        secondBiggest = biggest;
        biggest = num;
      } else if (num > secondBiggest && num < biggest) {
        secondBiggest = num;
      }
    }
  }

  return secondBiggest;
}

const args = process.argv.slice(2);
const result = findSecondBiggest(args);
console.log(result);
