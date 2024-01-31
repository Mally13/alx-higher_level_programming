#!/usr/bin/node
/**
 * Gets the contents of a webpage and stores it in a file.
 */
const request = require('request');
const fs = require('fs');
const { argv } = process;

// Check if both URL and file path are provided as arguments
if (argv.length !== 4) {
  console.error('Usage: node script.js <URL> <file_path>');
  process.exit(1);
}

request.get(argv[2], (err, response, body) => {
  if (err) {
    console.error(err);
  }
  const content = body;
  fs.writeFile(argv[3], content, 'utf-8', (error) => {
    if (err) {
      console.error(error);
    }
  });
});
