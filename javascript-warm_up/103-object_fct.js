#!/usr/bin/node

// incrementAndCall.js
function incrementAndCall(number, theFunction) {
  number = incr(number);
  theFunction(number);
}

function incr(number) {
  return number + 1;
}

// Example usage
function myFunction(number) {
  console.log("Number:", number);
}

incrementAndCall(5, myFunction);
