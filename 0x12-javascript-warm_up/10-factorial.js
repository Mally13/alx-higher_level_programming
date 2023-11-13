#!/usr/bin/node

const base = process.argv[2];

function factorize (n) {
  if (isNaN(n) || n === 1 || n === 0) {
    return (1);
  }
  return (n * factorize(n - 1));
}
console.log(factorize(base));
