#!/usr/bin/node
const { dict } = require('./101-data.js');

const sortedDict = {};
for (const userId in dict) {
  const occurrence = dict[userId];
  if (sortedDict[occurrence]) {
    sortedDict[occurrence].push(userId);
  } else {
    sortedDict[occurrence] = [userId];
  }
}

console.log(sortedDict);
