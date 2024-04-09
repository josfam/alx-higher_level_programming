#!/usr/bin/node

const firstAsNum = parseInt(process.argv[2]);

if (isNaN(firstAsNum)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + firstAsNum);
}
