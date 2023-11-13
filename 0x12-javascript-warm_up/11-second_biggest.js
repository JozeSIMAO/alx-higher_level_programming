#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

function findSecondLargest (arr) {
  if (arr.length <= 1) {
    console.log(0);
  } else {
    const sortedUniqueNumbers = [...new Set(arr)].sort((a, b) => b - a);
    console.log(sortedUniqueNumbers[1]);
  }
}

findSecondLargest(args);
