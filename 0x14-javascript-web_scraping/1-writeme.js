#!/usr/bin/node
/*
 * Writes a string to a file
 * content must be writen in utf-8
 */

const fs = require('fs');
const { argv } = process;
if (argv.length < 4) {
  console.error('Usage: ./1-writeme.js <filepath> <string>');
  process.exit(1);
}

const filepath = argv[2];
const stringtoadd = argv[3];
fs.writeFile(filepath, stringtoadd, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
