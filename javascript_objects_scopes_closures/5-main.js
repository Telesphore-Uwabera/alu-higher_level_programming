const Square = require('./5-square');

const s1 = new Square(4);
console.log('Original Square:');
s1.print();

console.log('After Doubling:');
s1.double();
s1.print();
