#!/usr/bin/node
const { argv } = require('node:process');

if (isNaN(+argv[2])) { console.log('Not a number'); } else {
  const first = parseInt(argv[2], 10);
  console.log(first);
}