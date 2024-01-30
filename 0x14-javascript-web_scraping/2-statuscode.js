#!/usr/bin/node
/*
 * Displays status code of a GET request
 */

const request = require('request');
const { argv } = process;
if (argv.length < 3) {
  console.error('Usage: ./2-statuscode.js <link>');
  process.exit(1);
}

const link = argv[2];
request.get(link, (err, response) => {
  if (err) {
    console.error(err);
  }
  console.log(`code: ${response.statusCode}`);
});
