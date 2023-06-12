#!/usr/bin/node
const fs = require('fs');

function readFile(filePath) {
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      console.error(`An error occurred while reading the file: ${err}`);
    } else {
      console.log(data);
    }
  });
}
