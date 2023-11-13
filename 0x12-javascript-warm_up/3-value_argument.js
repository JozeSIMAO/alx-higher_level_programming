#!/usr/bin/node

const argsArray = process.argv;

if (argsArray[2] === undefined) {
  console.log('No argument');
} else {
  console.log(argsArray[2]);
}
