#!/usr/bin/node

// executeXTimes.js
function executeXTimes(x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

// Example usage
function myFunction() {
  console.log("Executing the function");
}

executeXTimes(5, myFunction);
