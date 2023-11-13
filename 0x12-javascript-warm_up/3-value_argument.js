#!/usr/bin/node

const { argv } = process;

argv.forEach((val, index) => {
  if (index === 1 && typeof argv[2] === 'undefined') { console.log('No argument'); } else if (index !== 0 && index !== 1) { console.log(val); }
});
