#!/usr/bin/node

const fs = require('fs');
const filename = process.argv[2];
const textToWrite = process.argv[3];

// write file synchronously
try {
  fs.writeFileSync(filename, textToWrite + '\n', 'utf-8');
} catch (err) {
  console.log(err);
}
