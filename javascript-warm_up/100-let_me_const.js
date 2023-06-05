#!/usr/bin/node

let myVar = 40;

function updateMyVar() {
  myVar = 333;
}

console.log(myVar);
updateMyVar();
console.log(myVar);
