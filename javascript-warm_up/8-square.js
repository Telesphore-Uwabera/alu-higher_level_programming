#!/usr/bin/node

const arg = process.argv[2];
const size = parseInt(arg);

if (!isNaN(size)) {
  if (size > 0) {
    for (let i = 0; i < size; i++) {
      let line = '';
      for (let j = 0; j < size; j++) {
        line += 'X';
      }
      console.log(line);
    }
  } else {
    console.log('Missing size');
  }
} else {
  console.log('Missing size');
}

