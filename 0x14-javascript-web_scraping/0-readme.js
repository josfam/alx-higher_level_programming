#!/usr/bin/node

const fs = require('fs');
const filename = process.argv[2];

// read file synchronously
try {
  const text = fs.readFileSync(filename, 'utf-8');
  console.log(text);
} catch (err) {
  console.log(err);
}
