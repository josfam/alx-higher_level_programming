#!/usr/bin/node

const argLen = process.argv.length - 2;
const numsToSort = process.argv.slice(2);

if (argLen <= 1) {
  console.log(0);
} else {
  numsToSort.sort();
  console.log(numsToSort[numsToSort.length - 2]);
}
