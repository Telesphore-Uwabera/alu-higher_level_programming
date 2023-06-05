#!/usr/bin/node

// incrementAndCall.js
function incrementAndCall(number, theFunction) {
  number++;
  theFunction(number);
}

// Example usage
function myFunction(number) {
  console.log("Number:", number);
}

incrementAndCall(5, myFunction);
