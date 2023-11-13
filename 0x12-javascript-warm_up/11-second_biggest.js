#!/usr/bin/node

const { argv } = process;

if (argv.length > 3) {
  let biggest = parseInt(argv[2], 10);
  let secondBiggest = parseInt(argv[2], 10);
  for (let i = 3; i < argv.length; i++) {
    const current = parseInt(argv[i], 10);
    if (current > biggest) {
      secondBiggest = biggest;
      biggest = current;
    } else if (current > secondBiggest && current < biggest) {
      secondBiggest = current;
    }
  }
  console.log(secondBiggest);
} else {
  console.log(0);
}
