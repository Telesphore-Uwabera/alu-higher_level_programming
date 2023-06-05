#!/usr/bin/node
// 13-add.js
exports.add = function(a, b) {
  return a + b;
};

// 13-main.js
const { add } = require('./13-add');

console.log(add(4, 85));
console.log(add(93, -4));
console.log(add(0, 89));
