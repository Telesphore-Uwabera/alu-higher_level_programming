#!/usr/bin/node
const fs = require('fs');

// Read the paths of the source files and the destination file from command-line arguments
const [, , fileA, fileB, fileC] = process.argv;

// Read the contents of the source files
const content1 = fs.readFileSync(fileA, 'utf8');
const content2 = fs.readFileSync(fileB, 'utf8');

// Concatenate the contents of the source files
const concatenatedContent = content1 + content2;

// Write the concatenated content to the destination file
fs.writeFileSync(fileC, concatenatedContent);

console.log(`Files ${fileA} and ${fileB} have been concatenated to ${fileC}.`);
