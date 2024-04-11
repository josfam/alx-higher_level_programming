#!/usr/bin/node

const fs = require('fs');
const firstFile = process.argv[2];
const secondFile = process.argv[3];
const outputFile = process.argv[4];

const firstText = fs.readFileSync(firstFile, 'utf8');
const secondText = fs.readFileSync(secondFile, 'utf8');
const concatedText = firstText + secondText;

try {
  fs.writeFileSync(outputFile, concatedText);
} catch (err) {
  console.log(`There was an error writing to ${outputFile}`);
}
