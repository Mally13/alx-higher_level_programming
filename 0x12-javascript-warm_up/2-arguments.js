#!/usr/bin/node

const len = process.argv.length;

len === 2 ? console.log('No argument') : len === 3 ? console.log('Argument found') : console.log('Arguments found');
