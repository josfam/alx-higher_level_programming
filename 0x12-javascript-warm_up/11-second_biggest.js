#!/usr/bin/node

const argLen = process.argv.length - 2;
const numsToSort = process.argv.slice(2);

if (argLen <= 1) {
  console.log(0);
} else {
  // make strings into ints and sort them
  const numsAsInts = numsToSort.map((x) => parseInt(x));
  numsAsInts.sort();
  console.log(numsAsInts[numsAsInts.length - 2]);
}
