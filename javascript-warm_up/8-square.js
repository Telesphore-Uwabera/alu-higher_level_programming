#!/usr/bin/node

function printSquare(size) {
  const num = parseInt(size);

  if (isNaN(num)) {
    console.log('Missing size');
    return;
  }

  for (let i = 0; i < num; i++) {
    let row = '';
    for (let j = 0; j < num; j++) {
      row += 'X';
    }
    console.log(row);
  }
}

const size = process.argv[2];
printSquare(size);
