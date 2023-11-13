#!/usr/bin/node

const num1 = Number(process.argv[2]);
const num2 = Number(process.argv[3]);

function add (a, b) {
  let sum = 0;

  if (a === undefined || b === undefined) {
    console.log('NaN');
  } else {
    sum = a + b;
  }
  return sum;
}
console.log(add(num1, num2));
