#!/usr/bin/node

const argsLen = process.argv.length - 2; // 2 reserved for system items
if (argsLen === 0) {
  console.log('No argument');
} else if (argsLen === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
