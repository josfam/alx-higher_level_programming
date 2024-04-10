#!/usr/bin/node

exports.esrever = function (list) {
  const reversed = [];
  for (const element of list) {
    reversed.unshift(element);
  }
  return reversed;
};
