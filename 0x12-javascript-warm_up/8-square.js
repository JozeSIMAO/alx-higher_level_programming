#!/usr/bin/node

const sizeSquare = process.argv[2];
if (typeof sizeSquare === 'undefined' || isNaN(sizeSquare)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < sizeSquare; i++) {
    let row = '';
    for (let j = 0; j < sizeSquare; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
