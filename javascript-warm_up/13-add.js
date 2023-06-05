#!/usr/bin/node

exports.add = function(a, b) {
  return a + b;
};
const { add } = require('./13-add');

console.log(add(4, 85));
console.log(add(93, -4));
console.log(add(0, 89));
