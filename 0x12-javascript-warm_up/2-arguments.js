#!/usr/bin/node

const argArray = process.argv;

if (argArray.length === 2) {
  console.log('No argument');
} else if (argArray.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
