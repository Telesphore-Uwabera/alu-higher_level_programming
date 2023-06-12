#!/usr/bin/node

const request = require('request');
const fs = require('fs');

if (process.argv.length > 3) {
  const url = process.argv[2];
  const filePath = process.argv[3];

  request.get(url, (error, response, body) => {
    if (error) {
      console.error(`An error occurred while making the request: ${error}`);
    } else if (response.statusCode !== 200) {
      console.error(`Error: ${response.statusCode} - ${response.statusMessage}`);
    } else {
      fs.writeFile(filePath, body, 'utf8', (err) => {
        if (err) {
          console.error(`An error occurred while writing to the file: ${err}`);
        } else {
          console.log(`The contents of the webpage have been saved to ${filePath}`);
        }
      });
    }
  });
} else {
  console.log('Please provide the URL and file path as arguments.');
}
