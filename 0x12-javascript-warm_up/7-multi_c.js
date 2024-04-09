#!/usr/bin/node

const argLen = process.argv.length - 2;
const printCount = parseInt(process.argv[2]);

if (argLen === 0) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < printCount; i++) {
    console.log('C is fun');
  }
}
