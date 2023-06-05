#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  let square = '';

  for (let i = 0; i < size; i++) {
    square += 'X'.repeat(size) + '\n';
  }

  console.log(square);
}
