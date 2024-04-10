#!/usr/bin/node

const dataDict = require('./101-data').dict;

const groupedData = {};
for (const [key, val] of Object.entries(dataDict)) {
  if (Object.hasOwn(groupedData, val)) {
    groupedData[val].push(key);
  } else {
    groupedData[val] = [key];
  }
}
console.log(groupedData);
