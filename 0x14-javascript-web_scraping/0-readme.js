#!/usr/bin/node
/*
 * Reads and prints contents of a file
 * content must be read in utf-8
 */

const fs = require('fs');
const { argv } = process;
if (argv.length < 3) {
  console.error('Usage: ./0-readme.js <filepath>');
  process.exit(1);
}

const filepath = argv[2];
fs.readFile(filepath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
